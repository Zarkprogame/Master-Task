from tkinter import *
from tkinter import messagebox
from models.models import Auth_User
from views.login.form_login_designer import FormLoginDesigner
from views.master.form_master_designer import FormMasterDesigner
from controllers.auth_user_controller import AuthUserController
from views.signup.form_signup import FormSignup
import util.encoding_decoding as end_dec
import sqlalchemy as db
from sqlalchemy.orm import Session
from models.models import Auth_User

class LoginForm(FormLoginDesigner):

    def __init__(self):
        self.auth_controller = AuthUserController()
        self.engine = db.create_engine('sqlite:///database/login.sqlite', echo=False, future=True)
        self.session = Session(bind=self.engine)
        self.tries = 3
        super().__init__()

    def check(self):
        user_db: Auth_User = self.auth_controller.getUserByUsername(self.user.get())
        if self.isUser(user_db):
            self.isPassword(self.password.get(), user_db)

    def userSignup(self):
        FormSignup()

    def isUser(self, user: Auth_User):
        status: bool = True
        if user == None:
            status = False
            messagebox.showerror(message='The User doesnt Exists, Please Sign Up', title='Message')
        return status

    def isPassword(self, password: str, user: Auth_User):
        b_password = end_dec.decrypt(user.password)
        if user.state:
            if (password == b_password):
                self.root.destroy()
                FormMasterDesigner(user.id, user.username, LoginForm)
            else:
                if user.username == 'root':
                    messagebox.showerror(message=f'The Password is Incorrect', title='Message')
                else:
                    self.tries -= 1
                    messagebox.showerror(message=f'The Password is Incorrect, you have {self.tries} attemps', title='Message')
                    if self.tries == 0:
                        #desabilitar usuario
                        user = self.session.query(Auth_User).get(user.id)
                        user.state = not user.state
                        self.session.add(user)
                        self.session.commit()
                        messagebox.showerror(message='This User is  Disabled for many attemps, contact an admin', title='Message')
        else:
            messagebox.showerror(message='This User is Disabled, contact an admin', title='Message')