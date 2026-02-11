import os

BOT_TOKEN = os.getenv("BOT_TOKEN")

ALLOWED_USER_IDS = [
    int(x) for x in os.getenv("ALLOWED_USER_IDS", "").split(",") if x
]

ALLOWED_GROUP_IDS = [
    int(x) for x in os.getenv("ALLOWED_GROUP_IDS", "").split(",") if x
]

MASTER_KEY = os.getenv("MASTER_KEY").encode()

BASE_URL = os.getenv("BASE_URL")  # Railway public URL
