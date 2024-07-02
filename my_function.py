import json
def lambda_handler(event, context):
    try:
        # Get the HTTP body from the event
        http_body = event['body']

        # Parse the JSON data
        data = json.loads(http_body)

        # Access the 'first_name' property from the JSON
        first_name = data.get('first_name', 'Unknown')

        return {
            'statusCode': 200,
            'body': json.dumps({'message': f'Hello, {first_name}!'})
        }
    except KeyError as e:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': 'Missing required parameter'})
        }
    except json.JSONDecodeError as e:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': 'Invalid JSON format'})
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': e+'Internal server error'})
        }
