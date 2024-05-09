import io
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sqlalchemy as db
from sqlalchemy.orm import Session
from models.models import Auth_User
import util.encoding_decoding as end_dec

class FormProfileDesigner():
    def __init__(self, main_body, settings_panel, id):
        self.id = id
        self.engine = db.create_engine('sqlite:///database/login.sqlite', echo=False, future=True)
        self.session = Session(bind=self.engine)
        self.settings = settings_panel
        self.main_body = main_body

        self.frameNavBar = LabelFrame(main_body, bd=0, bg='#f1faff')
        self.frameNavBar.pack(side='top', expand=NO, fill='both')

        self.btnBack = Button(self.frameNavBar, text='Back', font=('Roborto', 12), bg='#03D92D', bd=0, command=self.back_button)
        self.btnBack.pack(side='left', padx=10, pady=5)

        self.frameusername = LabelFrame(main_body, text='Change Username', font=('Roborto', 15), bg='#f1faff')
        self.frameusername.pack(side='top', expand=NO, fill='both', padx=10, pady=5)
        self.frameusername.grid_columnconfigure(1, weight=1)

        user = self.session.query(Auth_User).get(self.id)

        self.lbl_user = Label(self.frameusername, text=f'Previus: {user.username}', font=('Times', 14), fg='#666a88', bg='#f1faff', anchor='w')
        self.lbl_user.pack(fill=X, padx=20, pady=5)
        self.user = ttk.Entry(self.frameusername, font=('Times', 14))
        self.user.pack(fill=X, padx=20, pady=5)
        self.user.focus()

        self.btnSend = Button(self.frameusername, text='Send', font=('Roborto', 11), bg='#03D92D', bd=0, command=self.changeUsername)
        self.btnSend.pack(side='top', padx=20, pady=(5,10), fill='both')

        self.framepassword = LabelFrame(main_body, text='Change Password', font=('Roborto', 15), bg='#f1faff')
        self.framepassword.pack(side='top', expand=NO, fill='both', padx=10, pady=5)
        self.framepassword.grid_columnconfigure(1, weight=1)

        # password = self.session.query(Auth_User).get(self.id)

        self.lbl_password = Label(self.framepassword, text='Password: ', font=('Times', 14), fg='#666a88', bg='#f1faff', anchor='w')
        self.lbl_password.pack(fill=X, padx=20, pady=5)
        self.password = ttk.Entry(self.framepassword, font=('Times', 14))
        self.password.pack(fill=X, padx=20, pady=5)
        self.password.config(show='*')

        self.lblNewPassword = Label(self.framepassword, text='New Password: ', font=('Times', 14), fg='#666a88', bg='#f1faff', anchor='w')
        self.lblNewPassword.pack(fill=X, padx=20, pady=5)
        self.newPassword = ttk.Entry(self.framepassword, font=('Times', 14))
        self.newPassword.pack(fill=X, padx=20, pady=5)
        self.newPassword.config(show='*')

        self.lblConfirmPassword = Label(self.framepassword, text='Confirm Password: ', font=('Times', 14), fg='#666a88', bg='#f1faff', anchor='w')
        self.lblConfirmPassword.pack(fill=X, padx=20, pady=5)
        self.ConfirmPassword = ttk.Entry(self.framepassword, font=('Times', 14))
        self.ConfirmPassword.pack(fill=X, padx=20, pady=5)
        self.ConfirmPassword.config(show='*')

        self.btnSend = Button(self.framepassword, text='Send', font=('Roborto', 12), bg='#03D92D', bd=0, command=self.changePassword)
        self.btnSend.pack(side='top', padx=20, pady=(5,10), fill='both')

    def back_button(self):
        self.clean_panel(self.main_body)
        self.settings(self.main_body, self.id)

    def clean_panel(self, panel):
        for widget in panel.winfo_children():
            widget.destroy()

    def changeUsername(self):
        user = self.session.query(Auth_User).get(self.id)
        username = self.session.query(Auth_User).filter_by(username=self.user.get()).first()
        if not (self.isUserRegister(username)):
            user.username = self.user.get()
            self.session.add(user)
            self.session.commit()
            messagebox.showinfo("Info", "The name was Successfully Changed!!")
            self.clean_panel(self.main_body)
            FormProfileDesigner(self.main_body, self.settings, self.id)
            messagebox.showinfo("Info", "The Side's Top Name will apear in the next Log In!!")

    def isUserRegister(self, user: Auth_User):
        status: bool = False
        if(user != None):
            status = True
            messagebox.showerror(message='The Username Already Exists')
        return status
    
    def changePassword(self):
        user = self.session.query(Auth_User).get(self.id)
        b_password = end_dec.decrypt(user.password)
        if b_password == self.password.get():
            pass
        else:
            messagebox.showerror("Info", "Your Password is Wrong")




    def isConfirmationPassword(self):
        status: bool = True
        if (self.newPassword.get() != self.ConfirmPassword.get()):
            status = False
            messagebox.showerror(message="The Passwords dont match", title="Message")
            self.newPassword.delete(0, END)
            self.ConfirmPassword.delete(0, END)
        return status