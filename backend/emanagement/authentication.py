def user_authentication_rule(user):
    return True if user is not None and user.is_active and not user.outstandingtoken_set.exists() else False