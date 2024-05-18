from tkinter import *
from views.master.about.about_designer import AboutDesigner
from views.master.about.aboutUs.form_AboutUs_designer import FormAboutUsDesigner
from views.master.about.PQRS.form_PQRS_designer import FormPQRSDesigner
from views.master.about.terms.form_Terms_designer import FormTermsConditionsDesigner
from views.master.about.questions.form_questions_designer import FormFAQDesigner
from views.master.about.contact.form_contact_designer import FormContactDesigner

class About(AboutDesigner):
    def __init__(self, main_body, id):
        self.id = id
        super().__init__(main_body)
        self.main_body = main_body
        self.side_menu_controls()

    def side_menu_controls(self):
        menu_width = 20
        menu_height = 2

        self.btnAboutUs = Button(self.AboutFrame, font=('roborto', 15), bg='#f1faff')
        self.btnPQRS = Button(self.AboutFrame, font=('roborto', 15), bg='#f1faff')
        self.btnTerms = Button(self.AboutFrame, font=('roborto', 15), bg='#f1faff')
        self.btnContact = Button(self.AboutFrame, font=('roborto', 15), bg='#f1faff')
        self.btnQuestions = Button(self.AboutFrame, font=('roborto', 15), bg='#f1faff')

        btn_info = [
            ('About Us', self.btnAboutUs, self.open_form_aboutUs),
            ('PQRS', self.btnPQRS, self.open_form_pqrs),
            ('Terms and Conditions', self.btnTerms, self.open_form_terms),
            ('Contact Us', self.btnContact, self.open_form_contact),
            ('Frequent Questions', self.btnQuestions, self.open_form_questions)
        ]

        for text, btn, command in btn_info:
            self.btn_menu_config(btn, text, menu_width, menu_height, command)

    def btn_menu_config(self, btn, text, menu_width, menu_height, command):
        btn.config(text=text, anchor='w', bd=0, fg='black', width=menu_width, height=menu_height, command=command)
        btn.pack(side='top', fill='x')
        self.bind_hover_events(btn)
        
    def bind_hover_events(self, btn):
        btn.bind("<Enter>", lambda event:self.on_enter(event, btn))
        btn.bind("<Leave>", lambda event:self.on_leave(event, btn))
    
    def on_enter(self, event, btn):
        btn.config(bg='#ebd8d0', fg='black')
        
    def on_leave(self, event, btn):
        btn.config(bg='#f1faff', fg='black')

    def open_form_aboutUs(self):
        self.clean_panel(self.main_body)
        FormAboutUsDesigner(self.main_body, About, self.id)

    def open_form_pqrs(self):
        self.clean_panel(self.main_body)
        FormPQRSDesigner(self.main_body, About, self.id)

    def open_form_terms(self):
        self.clean_panel(self.main_body)
        FormTermsConditionsDesigner(self.main_body, About, self.id)

    def open_form_contact(self):
        self.clean_panel(self.main_body)
        FormContactDesigner(self.main_body, About, self.id)

    def open_form_questions(self):
        self.clean_panel(self.main_body)
        FormFAQDesigner(self.main_body, About, self.id)

    def clean_panel(self, panel):
        for widget in panel.winfo_children():
            widget.destroy()