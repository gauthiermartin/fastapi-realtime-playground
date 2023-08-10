from typing import List

from sqlmodel import Session, create_engine

from app.api.models.user import User


def _create_dummy_users() -> List[User]:
    """
    The above code defines a function that creates dummy user objects and saves them to a database.

    Returns:
      The function `_create_dummy_users()` returns a list of `User` objects.
    """
    users = [
        User(first_name="John", last_name="Doe", score=0),
        User(first_name="Jane", last_name="Doe", score=50),
        User(first_name="John", last_name="Smith", score=100),
        User(first_name="Jane", last_name="Smith", score=150),
    ]
    return users


def _save_users_to_db(users: List[User]):
    """
    The function saves a list of User objects to a SQLite database.

    Args:
      users (List[User]): A list of User objects that need to be saved to the database.
    """
    engine = create_engine("sqlite:///database.db", echo=True)
    with Session(engine) as session:
        for user in users:
            session.add(user)
        session.commit()


def apply_fixture():
    """
    The function applies a fixture by creating dummy users and saving them to a database.
    """
    users = _create_dummy_users()
    _save_users_to_db(users)
