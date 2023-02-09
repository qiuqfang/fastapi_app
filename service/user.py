from crud import user


def getUserById(userId: int):
    return user.getUserById(user_id=userId)
