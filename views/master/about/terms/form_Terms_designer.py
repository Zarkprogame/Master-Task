from tkinter import *

class FormTermsConditionsDesigner():
    def __init__(self, main_body, settings_panel, id):
        self.id = id
        self.settings = settings_panel
        self.main_body = main_body

        # Frame de navegación
        self.frameNavBar = LabelFrame(main_body, bd=0, bg='#f1faff')
        self.frameNavBar.pack(side='top', expand=NO, fill='both')

        self.btnBack = Button(self.frameNavBar, text='Back', font=('Roboto', 12), bg='#03D92D', bd=0, command=self.back_button)
        self.btnBack.pack(side='left', padx=10, pady=5)

        # Frame de Términos y Condiciones
        self.frameTerms = LabelFrame(main_body, text='Términos y Condiciones', font=('Roboto', 15), bg='#f1faff')
        self.frameTerms.pack(side='top', expand=NO, fill='both', padx=10, pady=5)
        self.frameTerms.grid_columnconfigure(1, weight=1)

        lblTerms = Label(self.frameTerms, text="""
            Al usar esta aplicación, aceptas cumplir con los siguientes términos y condiciones:

            1. Uso adecuado: La aplicación debe ser utilizada de manera adecuada y legal.
            2. Privacidad: Respetaremos y protegeremos tu privacidad en todo momento.
            3. Responsabilidad: No nos hacemos responsables por el uso indebido de la aplicación.
            4. Actualización: Nos reservamos el derecho de actualizar estos términos y condiciones en cualquier momento.

            Al utilizar esta aplicación, confirmas que has leído, comprendido y aceptado estos términos y condiciones.
            """, bg='#f1faff', font=('Roboto', 11))
        lblTerms.pack(fill='both', expand=True, padx=2, pady=2)

    def back_button(self):
        self.clean_panel(self.main_body)
        self.settings(self.main_body, self.id)

    def clean_panel(self, panel):
        for widget in panel.winfo_children():
            widget.destroy()
