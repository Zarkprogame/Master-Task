from tkinter import *

class FormAdminDesigner():

    def render_users(self):
        pass

    def enableUser(self, id):
        pass

    def disableUser(self, id):
        pass

    def __init__(self, main_panel):
        self.FrameUserManage = LabelFrame(main_panel, text='Users Management', font=("Roborto", 20), padx=5, pady=5, bd=0)
        self.FrameUserManage.pack(side=TOP, expand=NO, fill='both')
        self.FrameUserManage.grid_columnconfigure(1, weight=1)