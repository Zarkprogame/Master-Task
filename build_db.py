import sqlalchemy as db
import models.models as models
import util.encoding_decoding as end_dec
from util.generic import read_img

def create_database_with_user():
    engine = db.create_engine('sqlite:///database/login.sqlite', echo=True, future=True)
    models.Base.metadata.create_all(engine)

    password = end_dec.encrypted('admin')

    with open('./img/logo.png', 'rb') as f:
        image = f.read()

    # image = read_img('./img/logo.png', (100,100))

    default_user = models.Auth_User(username='root', password=password, profile=image, state=True)
    
    with db.orm.Session(engine) as session:
        session.add(default_user)
        session.commit()

if __name__ == "__main__":
    create_database_with_user()