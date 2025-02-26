from flask import Flask, jsonify
import boto3
import os

app = Flask(__name__)

# Configurar DynamoDB
dynamodb = boto3.resource(
    'dynamodb',
    region_name=os.getenv('AWS_REGION', 'us-east-1')
)
table_name = os.getenv('DYNAMODB_TABLE', 'VisitorCounter')
table = dynamodb.Table(table_name)

@app.route('/')
def home():
    # Incrementar contador
    response = table.update_item(
        Key={'id': 'visitor_count'},
        UpdateExpression='ADD count :inc',
        ExpressionAttributeValues={':inc': 1},
        ReturnValues='UPDATED_NEW'
    )
    return jsonify({"visits": response['Attributes']['count']})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
