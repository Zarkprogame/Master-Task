import sqlalchemy as db
from models.models import Auth_User
from sqlalchemy.orm import Session

class AuthUserController():
    def __init__(self):
        self.engine = db.create_engine('sqlite:///database/login.sqlite', echo=False, future=True)

    def getUserByUsername(self, user_name: str):
        user: Auth_User = None
        with Session(self.engine) as session:
            user = session.query(Auth_User).filter_by(username=user_name).first()
        return user

    def insertUser(self, user: Auth_User):
        with Session(self.engine) as session:
            session.add(user)
            session.commit()