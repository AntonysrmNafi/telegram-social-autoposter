from config.settings import ALLOWED_GROUP_IDS, ALLOWED_USER_IDS

def allowed(update) -> bool:
    return (
        update.effective_user.id in ALLOWED_USER_IDS
        and update.effective_chat.id in ALLOWED_GROUP_IDS
    )
