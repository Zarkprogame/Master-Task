from tkinter import *
from tkinter import ttk
from tkinter.font import BOLD
import util.generic as utl

class FormLoginDesigner:

    def check(self):
        pass

    def userSignup(self):
        pass

    def __init__(self):
        self.root = Tk()
        self.root.title('LogIn')
        self.root.geometry('800x500')
        self.root.config(bg='#fcfcfc')
        self.root.resizable(0,0)
        utl.root_center(self.root, 800, 500)

        logo = utl.read_img("./img/logo.png", (210, 200))

        # Logo Frame
        logo_frame = Frame(self.root, bd=0, width=300, relief=SOLID, padx=10, pady=10, bg='#3a7ff6')
        logo_frame.pack(side="left", expand=NO, fill=BOTH)
        lblImg = Label(logo_frame, image=logo, bg='#3a7ff6')
        lblImg.place(x=0, y=0, relwidth=1, relheight=1)

        # Form Frame
        form_frame = Frame(self.root, bd=0, relief=SOLID, bg='#fcfcfc')
        form_frame.pack(side='right', expand=YES, fill=BOTH)

        # Form Frame Top
        form_frame_top = Frame(form_frame, height=50, bd=0, relief=SOLID, bg='black')
        form_frame_top.pack(side='top', fill=X)
        title = Label(form_frame_top, text='Log In Master Task', font=('Times', 30), fg='#666a88', pady=50)
        title.pack(expand=YES, fill=BOTH)

        # Form Frame Fill
        form_frame_fill = Frame(form_frame, height=50, bd=0, relief=SOLID, bg='#fcfcfc')
        form_frame_fill.pack(side='bottom', expand=YES, fill=BOTH)

        lbl_user = Label(form_frame_fill, text='User', font=('Times', 16), fg='#666a88', bg='#fcfcfc', anchor='w')
        lbl_user.pack(fill=X, padx=20, pady=5)
        self.user = ttk.Entry(form_frame_fill, font=('Times', 14))
        self.user.pack(fill=X, padx=20, pady=10)
        self.user.focus()

        lbl_password = Label(form_frame_fill, text='Password', font=('Times', 16), fg='#666a88', bg='#fcfcfc', anchor='w')
        lbl_password.pack(fill=X, padx=20, pady=5)
        self.password = ttk.Entry(form_frame_fill, font=('Times', 14))
        self.password.pack(fill=X, padx=20, pady=10)
        self.password.config(show="*")

        btnLogin = Button(form_frame_fill, text='Log In', font=('Times', 15, BOLD), bg='#3a7ff6', bd=0, fg='#fff', command=self.check)
        btnLogin.pack(fill=X, padx=20, pady=20)
        self.password.bind("<Return>", (lambda event: self.check()))

        btnSignup = Button(form_frame_fill, text='SignUp User', font=('Times', 15), bg='#fcfcfc', bd=0, fg='#3a7ff6', command=self.userSignup)
        btnSignup.pack(fill=X, padx=20, pady=20)

        self.root.mainloop()

