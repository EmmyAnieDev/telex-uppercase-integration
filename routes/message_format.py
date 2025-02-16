from fastapi import APIRouter, Request

router = APIRouter()


@router.post("/format-message")
async def format_message(request: Request):
    data = await request.json()
    print(data)

    message = data.get("message", "")

    modified_message = message.upper()

    response_data = {
        "event_name": "message_formatted",
        "message": modified_message,
        "status": "success",
        "username": "uppercase-bot"
    }

    return response_data