from tkinter import *
from config import *

class FormConstruction():

    def __init__(self, main_panel, logo):
        self.top_bar = Frame(main_panel)
        self.top_bar.pack(side=TOP, fill=X, expand=False)

        self.bottom_bar = Frame(main_panel)
        self.bottom_bar.pack(side=BOTTOM, fill='both', expand=True)

        self.lblTitulo = Label(self.top_bar, text='In Construction Page...')
        self.lblTitulo.config(fg='#222d33', font=('Roboto', 30), bg=MAIN_BODY_COLOR)
        self.lblTitulo.pack(side=TOP, fill='both', expand=True)

        self.lblImg = Label(self.bottom_bar, image=logo)
        self.lblImg.place(x=0, y=0, relheight=1, relwidth=1)
        self.lblImg.config(fg='#fff', font=('Roboto', 10), bg=MAIN_BODY_COLOR)

