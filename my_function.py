import json
import logging
import cv2
import pandas as pd
import mediapipe as mp
import numpy as np

def lambda_handler(event, context):
    try:
        # Get the HTTP body from the event
        http_body = event['body']
        logging.info(f"Received HTTP body: {http_body}")

        # Parse the JSON data
        data = json.loads(http_body)
        logging.info(f"Parsed JSON data: {data}")

        # Access the 'first_name' property from the JSON
        first_name = data.get('first_name', 'Unknown')

        versions = f'OpenCV: {cv2.__version__}, Pandas: {pd.__version__}, Mediapipe: {mp.__version__}, Numpy: {np.__version__}'

        return {
            'statusCode': 200,
            'body': json.dumps({'message': f'Hello, {first_name}!', 'versions': versions})
        }
    except KeyError as e:
        logging.error(f"KeyError: {str(e)}")
        return {
            'statusCode': 400,
            'body': json.dumps({'error': 'Missing required parameter'})
        }
    except json.JSONDecodeError as e:
        logging.error(f"JSONDecodeError: {str(e)}")
        return {
            'statusCode': 400,
            'body': json.dumps({'error': 'Invalid JSON format'})
        }
    except Exception as e:
        logging.error(f"Unexpected error: {str(e)}")
        return {
            'statusCode': 200,
            'body': json.dumps({'error': 'There is an Internal server error'})
        }
