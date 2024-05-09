import io
from tkinter import *
from tkinter import filedialog, messagebox
import sqlalchemy as db
from sqlalchemy.orm import Session
from PIL import Image, ImageTk
from config import MAIN_BODY_COLOR
from models.models import Auth_User

class FormPhotoDesigner():
    def __init__(self, main_body, settings_panel, id):
        self.id = id
        self.engine = db.create_engine('sqlite:///database/login.sqlite', echo=False, future=True)
        self.session = Session(bind=self.engine)
        self.settings = settings_panel
        self.main_body = main_body
        self.frameNavBar = LabelFrame(main_body, bd=0, bg='#f1faff')
        self.frameNavBar.pack(side='top', expand=NO, fill='both')
        self.frameNavBar.grid_rowconfigure(1, weight=1)

        self.btnBack = Button(self.frameNavBar, text='Back', font=('Roborto', 12), bg='#03D92D', bd=0, command=self.back_button)
        self.btnBack.pack(side='left', padx=10, pady=5)

        self.framePhoto = LabelFrame(main_body, text='Change Photo', font=('Roborto', 20), bg='#f1faff')
        self.framePhoto.pack(side='top', expand=NO, fill='both', padx=10, pady=10)
        self.framePhoto.grid_columnconfigure(1, weight=1)

        user = self.session.query(Auth_User).get(self.id)
        img_profile = ImageTk.PhotoImage(Image.open(io.BytesIO(user.profile)).resize((200, 200), Image.ADAPTIVE))
        self.profile_image = img_profile
        self.lblPerfil = Label(self.framePhoto, image=img_profile, bg=MAIN_BODY_COLOR)
        self.lblPerfil.pack(side=TOP, pady=10)

        self.btnchange = Button(self.framePhoto, text='Change Photo', font=('Roborto', 12), bg='#9E9E9E', bd=0, command=self.upload_image)
        self.btnchange.pack(side='top', padx=5, pady=5)

    def back_button(self):
        self.clean_panel(self.main_body)
        self.settings(self.main_body, self.id)

    def upload_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.gif")])
        if file_path:
            with open(file_path, "rb") as f:
                image = f.read()
                user = self.session.query(Auth_User).get(self.id)
                user.profile = image
                self.session.add(user)
                self.session.commit()
                messagebox.showinfo("Info", "The Image was Successfully Changed!!")
                messagebox.showinfo("Info", "The Side's Image Profile will apear in the next Log In")
                self.clean_panel(self.main_body)
                FormPhotoDesigner(self.main_body, self.settings, self.id)

    def clean_panel(self, panel):
        for widget in panel.winfo_children():
            widget.destroy()