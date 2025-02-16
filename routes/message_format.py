from fastapi import APIRouter, Request

router = APIRouter()


@router.post("/format-message")
async def format_message(request: Request):
    data = await request.json()

    print(data)

    message = data.get("message", "")
    channel_id = data.get("channel_id", "")

    print(channel_id)

    modified_message = message.upper()

    response_data = {
        "event_name": "message_formatted",
        "channel_id": channel_id,
        "message": modified_message,
        "status": "success",
        "username": "uppercase-bot"
    }

    return response_data