import json
import decimalencoder
import os
import boto3

dynamodb = boto3.resource('dynamodb')
translate = boto3.client(service_name='translate', region_name='us-east-1', use_ssl=True)


def getnew(event, context):
    # create a response
    table = dynamodb.Table(
                            os.environ['DYNAMODB_TABLE'])
    result = table.get_item(
        Key={
            'id': event['pathParameters']['id']
        }
    )
    source = 'auto'
    if event['pathParameters']['lg'] != '':
        target = event['pathParameters']['lg']
    else:
        raise Exception
    valortraduc = translate.translate_text(Text=result['Item']['text'],
                                           SourceLanguageCode=source,
                                           TargetLanguageCode=target)
    print(valortraduc)
    result['Item']["text"] = valortraduc.get('TranslatedText')
    response = {
        "statusCode": 200,
        "body": json.dumps(result['Item'],
                           cls=decimalencoder.DecimalEncoder)
    }
    return response
