def get_facebook_auth_url(user_id):
    return f"https://www.facebook.com/v18.0/dialog/oauth?state={user_id}"
