from tkinter import *
from tkinter import messagebox
from util.generic import read_img, root_center
import sqlalchemy as db
from sqlalchemy.orm import Session
from models.models import Auth_User
from views.master.admin.form_admin_designer import FormAdminDesigner

class FormAdmin(FormAdminDesigner):
    def __init__(self, main_panel):
        super().__init__(main_panel)
        self.engine = db.create_engine('sqlite:///database/login.sqlite', echo=False, future=True)
        self.session = Session(bind=self.engine)
        self.render_users()

    def enableUser(self, id):
        def _enableUser():
            user = self.session.query(Auth_User).get(id)
            if user.state == False:
                answer = messagebox.askokcancel("Info", "Are you Sure you want to Enable this User?")
                if answer:
                    user.state = not user.state
                    self.session.add(user)
                    self.session.commit()
                    messagebox.showinfo("Info", "User Successfully Enabled!!")
                    self.render_users()
            else:
                messagebox.showinfo("Info", "This user is already Enabled")
        return _enableUser
    
    def disableUser(self, id):
        def _disableUser():
            user = self.session.query(Auth_User).get(id)
            if user.state == True:
                answer = messagebox.askokcancel("Info", "Are you Sure you want to Disabled this User?")
                if answer:
                    user.state = not user.state
                    self.session.add(user)
                    self.session.commit()
                    messagebox.showinfo("Info", "User Successfully Disabled!!")
                    self.render_users()
            else:
                messagebox.showinfo("Info", "This user is already Disabled")
        return _disableUser

    def render_users(self):
        users = self.session.query(Auth_User).all()

        for widget in self.FrameUserManage.winfo_children():
                widget.destroy()
        
        for i, user in enumerate(users):
            user_id = user.id
            username = user.username
            state = 'Enabled' if user.state else 'Disabled'
            # color = '#555555' if state else '#000000'

            if username == "root":
                continue
            else:
                lblTitleUsername = Label(self.FrameUserManage, text="Username", font=('Roborto', 15))
                lblTitleUsername.grid(row=0, column=0)

                lblTitleState = Label(self.FrameUserManage, text="State", font=('Roborto', 15))
                lblTitleState.grid(row=0, column=1)

                lblTitleActions = Label(self.FrameUserManage, text="Actions", font=('Roborto', 15))
                lblTitleActions.grid(row=0, column=2)

                lblUsername = Label(self.FrameUserManage, text=username, font=('Roborto', 13))
                lblUsername.grid(row=i, column=0)

                lblState = Label(self.FrameUserManage, text=state, font=('Roborto', 13))
                lblState.grid(row=i, column=1)
                
                btnEnable = Button(self.FrameUserManage, text="Enable", background='#03D92D', borderwidth=0, padx=2, font=('Roboto', 11), command=self.enableUser(user_id))
                btnEnable.grid(row=i, column=2, pady=2, padx=15, sticky='e')

                btnDisable = Button(self.FrameUserManage, text="Disable", background='#CB3234', borderwidth=0, padx=2, font=('Roboto', 11), command=self.disableUser(user_id))
                btnDisable.grid(row=i, column=3, pady=2, padx=(5,10), sticky='e')


            

