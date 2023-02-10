from crud import user


def get_user_by_id(user_id: int):
    return user.get_user_by_id(user_id)
