def list(event, context):
    try:
        result = todoList.get_items()
        print("DEBUG - items:", result)
        return {
            "statusCode": 200,
            "body": json.dumps(result, cls=decimalencoder.DecimalEncoder),
            "headers": {
                "Content-Type": "application/json"
            }
        }
    except Exception as e:
        print("ERROR:", str(e))
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)}),
            "headers": {
                "Content-Type": "application/json"
            }
        }