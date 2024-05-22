from backend.apps import User


def fetch_user(token: dict) -> User|None:
    """
    """
    user = User.objects.filter(
        email=token["userinfo"]["email"],
    ).first()

    return user


def create_user(token: dict) -> User:
    """
    """
    user = User.objects.create(
        fullname=token["userinfo"]["name"],
        email=token["userinfo"]["email"],
    )

    return user
