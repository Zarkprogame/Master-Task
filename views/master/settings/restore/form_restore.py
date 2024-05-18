import sqlalchemy as db
from sqlalchemy.orm import sessionmaker
from models.models import Todo

class RestoreManager:
    def __init__(self):
        self.engine = db.create_engine('sqlite:///database/login.sqlite', echo=False, future=True)
        self.Session = sessionmaker(bind=self.engine)

    def delete_all_todos(self, user_id):
        session = self.Session()

        try:
            todos_deleted = session.query(Todo).filter(Todo.user_id == user_id).delete()
            session.commit()
            if todos_deleted == 0:
                message = "you don't have To Do to delete"
            else:    
                message = f"{todos_deleted} To Do have been removed from the user with ID {user_id}"
        except Exception as e:
            session.rollback()
            message = f"Error when deleting the To Do of the user with ID {user_id}: {e}"
        finally:
            session.close()

        return message
