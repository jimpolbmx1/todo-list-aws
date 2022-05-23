import json
import decimalencoder
import os
import boto3

dynamodb = boto3.resource('dynamodb')
translate = boto3.client('translate')


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
    if event['pathParameters']['lg'] == 'en':
        target = 'en'
    elif event['pathParameters']['lg'] == 'fr':
        target = 'fr'
    else:
        target = 'auto'
    finalresult = translate.translate_text(Text=result['Item']['text'],
                                           SourceLanguageCode=source,
                                           TargetLanguageCode=target)
    print(finalresult)
    result['Item']["text"] = finalresult.get('TranslatedText')
    response = {
        "statusCode": 200,
        "body": json.dumps(result['Item'],
                           cls=decimalencoder.DecimalEncoder)
    }
    return response
