from fastapi import APIRouter, Request

router = APIRouter()


@router.get("/integration.json")
def get_integration_json(request: Request):
    base_url = str(request.base_url).rstrip("/")
    return {
        "data": {
            "date": {
                "created_at": "2025-02-16",
                "updated_at": "2025-02-16"
            },
            "descriptions": {
                "app_name": "Telex-Uppercase",
                "app_description": "Automatically converts all messages to UPPERCASE. "
                                   "This integration ensures consistency in text formatting "
                                   "and enhances readability for Telex channels.",
                "app_logo": "https://i.imgur.com/lZqvffp.png",
                "app_url": f"{base_url}/integration.json",
                "background_color": "#ffffff"
            },
            "is_active": True,
            "integration_type": "modifier",
            "key_features": [
                "Automatically convert all messages to UPPERCASE.",
                "Ensures uniform formatting and readability in discussions.",
                "Instantly processes incoming messages within 1 second.",
                "Lightweight and optimized for high-speed text transformation.",
                "Supports multi-channel integrations across various Telex workspaces.",
                "No manual activation required after setup—works in real-time."
            ],
            "author": "Emmy",
            "integration_category": "Communication & Collaboration",
            "settings": [
                {
                    "label": "enableUppercase",
                    "type": "checkbox",
                    "description": "Enable or disable automatic uppercase conversion.",
                    "default": True,
                    "required": True
                },
                {
                    "label": "customUppercaseWords",
                    "type": "text",
                    "description": "Enter specific words to always convert to uppercase.",
                    "default": "No",
                    "required": False
                },
                {
                    "label": "excludeWords",
                    "type": "text",
                    "description": "Comma-separated words that should NOT be converted to uppercase.",
                    "default": "",
                    "required": False
                },
                {
                    "label": "notifyOnConversion",
                    "type": "checkbox",
                    "description": "Send a notification when a message is converted.",
                    "default": False,
                    "required": False
                },
                {
                    "label": "logConversions",
                    "type": "checkbox",
                    "description": "Log all converted messages for reference.",
                    "default": False,
                    "required": False
                }
            ],
            "permissions": {
                "events": [
                    "Transform messages into UPPERCASE in real-time.",
                    "Allow customization of specific words to stay lowercase.",
                    "Send notifications upon message conversion if enabled.",
                    "Enable logging for auditing purposes."
                ]
            },
            "target_url": f"{base_url}/format-message",
            "tick_url": ""
        }
    }