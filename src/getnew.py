import json
import decimalencoder
import boto3
import todoList

dynamodb = boto3.resource('dynamodb')
translate = boto3.client(service_name='translate',
                         region_name='us-east-1', use_ssl=True)


def getnew(event, context):
    # create a response
    item = todoList.get_translate(event['pathParameters']['id'],
                                  event['pathParameters']['lg'])
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
    