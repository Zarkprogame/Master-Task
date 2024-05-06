from tkinter import *
from tkinter import ttk
from tkinter.font import BOLD
import util.generic as utl

class FormSignupDesigner:

    def register():
        pass

    def __init__(self):
        self.root = Toplevel()
        self.root.title('Signup')
        self.root.geometry('800x500')
        self.root.config(bg='#fcfcfc')
        self.root.resizable(0,0)
        utl.root_center(self.root, 800, 500)

        logo = utl.read_img("./img/logo.png", (200, 200))

        # Logo Frame
        logo_frame = Frame(self.root, bd=0, width=300, relief=SOLID, padx=10, pady=10, bg='#F87474')
        logo_frame.pack(side="left", expand=NO, fill=BOTH)
        lblImg = Label(logo_frame, image=logo, bg='#F87474')
        lblImg.place(x=0, y=0, relwidth=1, relheight=1)

        # Form Frame
        form_frame = Frame(self.root, bd=0, relief=SOLID, bg='#fcfcfc')
        form_frame.pack(side='right', expand=YES, fill=BOTH)

        # Form Frame Top
        form_frame_top = Frame(form_frame, height=50, bd=0, relief=SOLID, bg='black')
        form_frame_top.pack(side='top', fill=X)
        title = Label(form_frame_top, text='Sign Up Master Task', font=('Times', 30), fg='#666a88', pady=50)
        title.pack(expand=YES, fill=BOTH)

        # Form Frame Fill
        form_frame_fill = Frame(form_frame, height=50, bd=0, relief=SOLID, bg='#fcfcfc')
        form_frame_fill.pack(side='bottom', expand=YES, fill=BOTH)

        lbl_user = Label(form_frame_fill, text='User', font=('Times', 16), fg='#666a88', bg='#fcfcfc', anchor='w')
        lbl_user.pack(fill=X, padx=20, pady=5)
        self.user = ttk.Entry(form_frame_fill, font=('Times', 14))
        self.user.pack(fill=X, padx=20, pady=10)

        lbl_password = Label(form_frame_fill, text='Password', font=('Times', 16), fg='#666a88', bg='#fcfcfc', anchor='w')
        lbl_password.pack(fill=X, padx=20, pady=5)
        self.password = ttk.Entry(form_frame_fill, font=('Times', 14))
        self.password.pack(fill=X, padx=20, pady=10)
        self.password.config(show="*")

        lbl_confirmation = Label(form_frame_fill, text='Confirmation', font=('Times', 16), fg='#666a88', bg='#fcfcfc', anchor='w')
        lbl_confirmation.pack(fill=X, padx=20, pady=5)
        self.confirmation = ttk.Entry(form_frame_fill, font=('Times', 14))
        self.confirmation.pack(fill=X, padx=20, pady=10)
        self.confirmation.config(show="*")

        btnSignup = Button(form_frame_fill, text='SignUp User', font=('Times', 15), bg='#F87474', bd=0, fg='#fcfcfc', command=self.register)
        btnSignup.pack(fill=X, padx=20, pady=20)
        self.root.bind("<Return>", (lambda event: self.register()))

        self.root.mainloop()

