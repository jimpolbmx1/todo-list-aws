import json
import boto3
import decimalencoder
import todoList

dynamodb = boto3.resource('dynamodb')
translate = boto3.client('translate')


def getnew(event, context):
    # create a response
    leng = event['pathParameters']['lg']
    ID = event['pathParameters']['id']
    item = todoList.get_translate(ID, leng)
    if item:
        response = {
            "statusCode": 200,
            "body": json.dumps(item,
                               cls=decimalencoder.DecimalEncoder)
        }
    else:
        response = {
            "statusCode": 404,
            "body": ""
        }
    return response
