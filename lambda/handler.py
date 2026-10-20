def lambda_handler(event, context):
    name = event.get("name","world")
    return{
        "statusCode": 200,
        "message": f"Hello, {name}!"
    }