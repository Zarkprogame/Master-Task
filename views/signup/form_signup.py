from views.signup.form_signup_designer import FormSignupDesigner
from controllers.auth_user_controller import AuthUserController
from models.models import Auth_User
from tkinter import messagebox
import util.encoding_decoding as end_dec
from tkinter import *

class FormSignup(FormSignupDesigner):

    def __init__(self):
        self.auth_controller = AuthUserController()
        super().__init__()

    def register(self):
        if self.user.get() == "" or self.password.get() == "":
            messagebox.showerror(message="You cant Register if the field is Empty", title="Message")
        else:
            if (self.isConfirmationPassword()):
                if (self.verification(self.password.get())):
                    user = Auth_User()
                    user.username = self.user.get()
                    user.state = True
                    with open('./img/logo.png', 'rb') as f:
                        image = f.read()
                    user.profile = image
                    user_db: Auth_User = self.auth_controller.getUserByUsername(self.user.get())
                    if not (self.isUserRegister(user_db)):
                        user.password = end_dec.encrypted(self.password.get())
                        self.auth_controller.insertUser(user)
                        messagebox.showinfo(message="The User has been Register!", title='Message')
        self.root.destroy()

    def isConfirmationPassword(self):
        status: bool = True
        if (self.password.get() != self.confirmation.get()):
            status = False
            messagebox.showerror(message="The Passwords dont match", title="Message")
            self.password.delete(0, END)
            self.confirmation.delete(0, END)
        return status
    
    def isUserRegister(self, user: Auth_User):
        status: bool = False
        if(user != None):
            status = True
            messagebox.showerror(message='The User Already Exists')
        return status
    
    def verification(self, password):
        if len(password) < 8:
            messagebox.showerror("Info", "The Password is too Short")
            return False
        elif len(password) > 20:
            messagebox.showerror("Info", "The Password is too Long")
            return False

        special_chars = "!@#$%^&*()_+=-[]{};:'\",.<>/?"
        esp_char = any(char in special_chars for char in password)
        if not esp_char:
            messagebox.showerror("Info", "The password need at least one Special Character")
            return False
        
        num = any(char.isdigit() for char in password)
        if not num:
            messagebox.showerror("Info", "The password need at least one Number")
            return False

        tiene_mayuscula = any(char.isupper() for char in password)
        if not tiene_mayuscula:
            messagebox.showerror("Info", "The password need at least one Capital Letter")
            return False

        return True
        