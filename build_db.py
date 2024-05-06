import sqlalchemy as db
import models.models as models
import util.encoding_decoding as end_dec

# engine = db.create_engine('sqlite:///database/login.sqlite', echo=True, future=True)
# models.Base.metadata.create_all(engine)


def create_database_with_user():
    engine = db.create_engine('sqlite:///database/login.sqlite', echo=True, future=True)
    models.Base.metadata.create_all(engine)

    password = end_dec.encrypted('admin')
    default_user = models.Auth_User(username='root', password=password, state=True)
    
    with db.orm.Session(engine) as session:
        session.add(default_user)
        session.commit()

if __name__ == "__main__":
    create_database_with_user()