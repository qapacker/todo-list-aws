import json
import decimalencoder
import todoList


def get(event, context):
    try:
        item_id = event.get('pathParameters', {}).get('id')
        if not item_id:
            raise ValueError("Missing 'id' in pathParameters")

        item = todoList.get_item(item_id)

        if item:
            response = {
                "statusCode": 200,
                "body": json.dumps(item, cls=decimalencoder.DecimalEncoder),
                "headers": {
                    "Content-Type": "application/json"
                }
            }
        else:
            response = {
                "statusCode": 404,
                "body": json.dumps({"error": "Item not found"}),
                "headers": {
                    "Content-Type": "application/json"
                }
            }

    except Exception as e:
        print("ERROR:", str(e))
        response = {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)}),
            "headers": {
                "Content-Type": "application/json"
            }
        }

    return response
