import json
import random

def lambda_handler(event, context):
    quotes = [
        "Cloud engineering is 10% coding and 90% figuring out why the IAM role failed.",
        "Automation is not a luxury; it is a necessity.",
        "Keep your infrastructure as code and your coffee strong."
    ]
    
    return {
        'statusCode': 200,
        'body': json.dumps({
            'message': random.choice(quotes),
            'status': 'Success'
        })
    }
