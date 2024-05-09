import io
from tkinter import *
from tkinter import font
from tkinter import messagebox
from config import *
from PIL import Image, ImageTk
import util.generic as utl
import sqlalchemy as db
from sqlalchemy.orm import Session
from views.master.form_construction import FormConstruction
from views.master.todo.form_todo import FormTodo
from views.master.admin.form_admin import FormAdmin
from views.master.settings.settings import Settings
from controllers.auth_user_controller import Auth_User

class FormMasterDesigner(Tk):
    def __init__(self, id, username, login_form):
        self.engine = db.create_engine('sqlite:///database/login.sqlite', echo=False, future=True)
        self.session = Session(bind=self.engine)
        self.id = id
        self.username = username
        self.login_form = login_form
        super().__init__()
        self.logo = utl.read_img("./img/logoLetters.png", (510, 136))
        self.img = utl.read_img("./img/construction.png", (100, 100))
        self.config_window()
        self.panels()
        self.top_main_controls()
        self.side_menu_controls()
        self.body_controls()

    def config_window(self):
        self.title("Panel")
        self.iconbitmap("./img/logo.ico")
        w, h = 1024 , 600
        self.minsize(800, 590)
        utl.root_center(self, w, h)

    def panels(self):
        self.top_bar = Frame(self, bg=TOP_BAR_COLOR, height=50)
        self.top_bar.pack(side=TOP, fill='both')

        self.side_menu = Frame(self, bg=SIDE_MENU_COLOR, width=150)
        self.side_menu.pack(side="left", fill='both', expand=False)

        self.main_body = Frame(self, bg=MAIN_BODY_COLOR, width=150)
        self.main_body.pack(side='right', fill='both', expand=True)

    def top_main_controls(self):
        self.lblTitle = Label(self.top_bar, text='Master Task')
        self.lblTitle.config(fg='#fff', font=("Roboto", 15), bg=TOP_BAR_COLOR, pady=10, width=16)
        self.lblTitle.pack(side='left')

        self.menu_img = utl.read_img("./img/menu.png", (30,30))

        self.btnSideMenu = Button(self.top_bar, image=self.menu_img, bd=0, bg=TOP_BAR_COLOR, command=self.toogle_panel)
        self.btnSideMenu.pack(side='left')

        self.lblInfo = Label(self.top_bar, text=self.username)
        self.lblInfo.config(fg='#fff', font=("Roboto", 10), bg=TOP_BAR_COLOR, padx=5, width=10)
        self.lblInfo.pack(side='right')
    
    def side_menu_controls(self):
        menu_width = 20
        menu_height = 2
        font_awesome = font.Font(family='FontAwesome', size=15)

        user = self.session.query(Auth_User).get(self.id)
        img_profile = ImageTk.PhotoImage(Image.open(io.BytesIO(user.profile)).resize((100, 100), Image.ADAPTIVE))

        self.profile_image = img_profile

        self.lblPerfil = Label(self.side_menu, image=img_profile, bg=SIDE_MENU_COLOR)
        self.lblPerfil.pack(side=TOP, pady=10)

        self.btnAdmin = Button(self.side_menu)
        self.btnTodo = Button(self.side_menu)
        self.btnSchedule = Button(self.side_menu)
        self.btnNotes = Button(self.side_menu)
        self.btnMemofiches = Button(self.side_menu)
        self.btnSettings = Button(self.side_menu)
        self.btnSignoff = Button(self.side_menu)

        btn_info = [
            ('Admin', "\uf109", self.btnAdmin, self.open_form_admin),
            ('Todo', "\uf109", self.btnTodo, self.open_form_Todo),
            ('Schedule', "\uf109", self.btnSchedule, self.open_form_construction),
            ('Notes', "\uf109", self.btnNotes, self.open_form_construction),
            ('Memofiches', "\uf109", self.btnMemofiches, self.open_form_construction),
            ('Settings', "\uf109", self.btnSettings, self.open_form_settings),
            ('Signoff', "\uf109", self.btnSignoff, self.signOff)
        ]

        for text, icon, btn, comand in btn_info:
            if self.username != "root" and text == "Admin":
                pass
            else:
                self.btn_menu_config(btn, text, icon, font_awesome, menu_width, menu_height, comand)

    def body_controls(self):
        lblImg = Label(self.main_body, image=self.logo, bg=MAIN_BODY_COLOR)
        lblImg.place(x=0, y=0, relwidth=1, relheight=1)

    def btn_menu_config(self, btn, text, icon, font_awesome, menu_width, menu_height, comand):
        btn.config(text=f" {icon}  {text}", anchor='w', font=font_awesome, bd=0, bg=SIDE_MENU_COLOR, fg='white', width=menu_width, height=menu_height, command=comand)
        btn.pack(side=TOP)
        self.bind_hover_events(btn)
        
    def bind_hover_events(self, btn):
        btn.bind("<Enter>", lambda event:self.on_enter(event, btn))
        btn.bind("<Leave>", lambda event:self.on_leave(event, btn))
    
    def on_enter(self, event, btn):
        btn.config(bg=HOVER_MENU_COLOR, fg='white')
        
    def on_leave(self, event, btn):
        btn.config(bg=SIDE_MENU_COLOR, fg='white')

    def toogle_panel(self):

        if self.side_menu.winfo_ismapped():
            self.side_menu.pack_forget()
        else:
            self.side_menu.pack(side='left', fill='y')
        
    def open_form_construction(self):
        self.clean_panel(self.main_body)
        FormConstruction(self.main_body, self.img)

    def clean_panel(self, panel):
        for widget in panel.winfo_children():
            widget.destroy()

    def open_form_Todo(self):
        self.clean_panel(self.main_body)
        FormTodo(self.main_body, self.id)

    def signOff(self):
        answer = messagebox.askokcancel("Sign Off","Are you sure that you want to exit?")
        if answer:
            messagebox.showinfo("Info", "Session has been closed")
            self.destroy()
            self.login_form()

    def open_form_admin(self):
        self.clean_panel(self.main_body)
        FormAdmin(self.main_body)

    def open_form_settings(self):
        self.clean_panel(self.main_body)
        Settings(self.main_body, self.id)