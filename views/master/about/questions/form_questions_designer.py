from tkinter import *

class FormFAQDesigner():
    def __init__(self, main_body, settings_panel, id):
        self.id = id
        self.settings = settings_panel
        self.main_body = main_body

        # Frame de navegación
        self.frameNavBar = LabelFrame(main_body, bd=0, bg='#f1faff')
        self.frameNavBar.pack(side='top', expand=NO, fill='both')

        self.btnBack = Button(self.frameNavBar, text='Back', font=('Roboto', 12), bg='#03D92D', bd=0, command=self.back_button)
        self.btnBack.pack(side='left', padx=10, pady=5)

        # Frame de Preguntas Frecuentes
        self.frameFAQ = LabelFrame(main_body, text='Frequent Questions', font=('Roboto', 15), bg='#f1faff')
        self.frameFAQ.pack(side='top', expand=NO, fill='both', padx=10, pady=5)
        self.frameFAQ.grid_columnconfigure(1, weight=1)

        # Pregunta 1
        frameQuestion1 = LabelFrame(self.frameFAQ, text='How can I reset my password?', bg='#f1faff', font=('Roboto', 11))
        frameQuestion1.pack(fill='both', expand=True, padx=10, pady=10)

        lblAnswer1 = Label(frameQuestion1, text="To reset your password, go to the Settings page and click 'Profile'", bg='#f1faff', font=('Roboto', 11))
        lblAnswer1.pack(fill='both', expand=True, padx=5, pady=5)

        # Pregunta 2
        frameQuestion2 = LabelFrame(self.frameFAQ, text='How can I contact customer service?', bg='#f1faff', font=('Roboto', 11))
        frameQuestion2.pack(fill='both', expand=True, padx=10, pady=10)

        lblAnswer2 = Label(frameQuestion2, text="You can contact our customer service by sending an email to zarkprogame@gmail.com", bg='#f1faff', font=('Roboto', 11))
        lblAnswer2.pack(fill='both', expand=True, padx=5, pady=5)

        # Pregunta 3
        frameQuestion3 = LabelFrame(self.frameFAQ, text='How can I change my profile photo?', bg='#f1faff', font=('Roboto', 11))
        frameQuestion3.pack(fill='both', expand=True, padx=10, pady=10)

        lblAnswer3 = Label(frameQuestion3, text="To customize your profile photo, go to the settings page and click 'Photo'", bg='#f1faff', font=('Roboto', 11))
        lblAnswer3.pack(fill='both', expand=True, padx=5, pady=5)

        # Pregunta 4
        frameQuestion4 = LabelFrame(self.frameFAQ, text='How can I change my username?', bg='#f1faff', font=('Roboto', 11))
        frameQuestion4.pack(fill='both', expand=True, padx=10, pady=10)

        lblAnswer4 = Label(frameQuestion4, text="To change your username, go to the Settings page and click 'Profile'", bg='#f1faff', font=('Roboto', 11))
        lblAnswer4.pack(fill='both', expand=True, padx=5, pady=5)

        # Pregunta 5
        frameQuestion5 = LabelFrame(self.frameFAQ, text='How can I delete my account?', bg='#f1faff', font=('Roboto', 11))
        frameQuestion5.pack(fill='both', expand=True, padx=10, pady=10)

        lblAnswer5 = Label(frameQuestion5, text="At the moment there is no way to Delete your account", bg='#f1faff', font=('Roboto', 11))
        lblAnswer5.pack(fill='both', expand=True, padx=5, pady=5)

    def back_button(self):
        self.clean_panel(self.main_body)
        self.settings(self.main_body, self.id)

    def clean_panel(self, panel):
        for widget in panel.winfo_children():
            widget.destroy()
