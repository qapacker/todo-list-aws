import json
import logging
import todoList


def create(event, context):
    if 'body' not in event:
        logging.error("Missing 'body' in event")
        raise Exception("Invalid request format.")

    data = json.loads(event['body'])

    if 'text' not in data:
        logging.error("Validation failed: 'text' is missing")
        raise Exception("Couldn't create the todo item.")

    item = todoList.put_item(data['text'])

    response = {
        "statusCode": 200,
        "body": json.dumps(item)  # Solo serializa una vez aquí
    }
    return response