from tkinter import *
from tkinter import messagebox
from tkinter import ttk

class FormPQRSDesigner():
    def __init__(self, main_body, settings_panel, id):
        self.id = id
        self.settings = settings_panel
        self.main_body = main_body

        self.frameNavBar = LabelFrame(main_body, bd=0, bg='#f1faff')
        self.frameNavBar.pack(side='top', expand=NO, fill='both')

        self.btnBack = Button(self.frameNavBar, text='Back', font=('Roboto', 12), bg='#03D92D', bd=0, command=self.back_button)
        self.btnBack.pack(side='left', padx=10, pady=5)

        self.frameForm = LabelFrame(main_body, text='PQRS Form', font=('Roboto', 15), bg='#f1faff')
        self.frameForm.pack(side='top', expand=YES, fill='both', padx=10, pady=10)
        self.frameForm.grid_columnconfigure(1, weight=1)

        self.create_form()

    def create_form(self):
        # Name
        lblName = Label(self.frameForm, text="Name:", font=('Roboto', 12), bg='#f1faff')
        lblName.grid(row=0, column=0, padx=10, pady=5)
        self.entryName = Entry(self.frameForm, font=('Roboto', 14), borderwidth=0)
        self.entryName.grid(row=0, column=1, padx=10, pady=5, sticky=W+E)
        self.entryName.focus()

        # Email
        lblEmail = Label(self.frameForm, text="Email:", font=('Roboto', 12), bg='#f1faff')
        lblEmail.grid(row=1, column=0, padx=10, pady=5)
        self.entryEmail = Entry(self.frameForm, font=('Roboto', 14), borderwidth=0)
        self.entryEmail.grid(row=1, column=1, padx=10, pady=5, sticky=W+E)

        # PQRS Type
        lblType = Label(self.frameForm, text="Type:", font=('Roboto', 12), bg='#f1faff')
        lblType.grid(row=2, column=0, sticky=W, padx=10, pady=5)
        self.typeVar = StringVar()
        self.typeVar.set("Petition")
        options = ["Petition", "Complaint", "Claim", "Suggestion"]
        self.comboBox = ttk.Combobox(self.frameForm, textvariable=self.typeVar, values=options, font=('Roboto', 12), state='readonly')
        self.comboBox.grid(row=2, column=1, padx=10, pady=5, sticky=W)

        # Apply style to the Combobox
        style = ttk.Style()
        style.configure("TCombobox",
                        fieldbackground="white",
                        background="white",
                        relief="flat",
                        borderwidth=0,
                        arrowcolor="black")

        # Message
        lblMessage = Label(self.frameForm, text="Message:", font=('Roboto', 12), bg='#f1faff')
        lblMessage.grid(row=3, column=0, sticky=N, padx=10, pady=5)
        self.textMessage = Text(self.frameForm, font=('Roboto', 12), width=40, height=10, borderwidth=0)
        self.textMessage.grid(row=3, column=1, padx=10, pady=5, sticky=W+E)

        # Submit Button
        self.btnSubmit = Button(self.frameForm, text='Submit', font=('Roboto', 12), bg='#03D92D', bd=0, command=self.submit_pqrs)
        self.btnSubmit.grid(row=4, column=1, padx=10, pady=10, sticky=N)

    def submit_pqrs(self):
        name = self.entryName.get()
        email = self.entryEmail.get()
        pqrs_type = self.typeVar.get()
        message = self.textMessage.get("1.0", END).strip()

        if not name or not email or not message:
            messagebox.showwarning("Input Error", "All fields are required")
            return

        messagebox.showinfo("PQRS Submitted", f"Thank you, {name}! Your {pqrs_type} has been submitted.")
        self.clear_form()

    def clear_form(self):
        self.entryName.delete(0, END)
        self.entryEmail.delete(0, END)
        self.textMessage.delete("1.0", END)
        self.typeVar.set("Petition")

    def back_button(self):
        self.clean_panel(self.main_body)
        self.settings(self.main_body, self.id)

    def clean_panel(self, panel):
        for widget in panel.winfo_children():
            widget.destroy()
