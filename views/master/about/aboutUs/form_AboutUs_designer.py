from tkinter import *

class FormAboutUsDesigner():
    def __init__(self, main_body, settings_panel, id):
        self.id = id
        self.settings = settings_panel
        self.main_body = main_body

        self.frameNavBar = LabelFrame(main_body, bd=0, bg='#f1faff')
        self.frameNavBar.pack(side='top', expand=NO, fill='both')

        self.btnBack = Button(self.frameNavBar, text='Back', font=('Roborto', 12), bg='#03D92D', bd=0, command=self.back_button)
        self.btnBack.pack(side='left', padx=10, pady=5)

        self.frameIntro = LabelFrame(main_body, text='Introduction', font=('Roborto', 15), bg='#f1faff')
        self.frameIntro.pack(side='top', expand=NO, fill='both', padx=10, pady=5)
        self.frameIntro.grid_columnconfigure(1, weight=1)

        self.framevision = LabelFrame(main_body, text='Vision', font=('Roborto', 15), bg='#f1faff')
        self.framevision.pack(side='top', expand=NO, fill='both', padx=10, pady=5)
        self.framevision.grid_columnconfigure(1, weight=1)

        self.framemision = LabelFrame(main_body, text='Mision', font=('Roborto', 15), bg='#f1faff')
        self.framemision.pack(side='top', expand=NO, fill='both', padx=10, pady=5)
        self.framemision.grid_columnconfigure(1, weight=1)

        lblintro = Label(self.frameIntro, text="""
            Master Task is an innovative application designed to help you manage and organize your daily tasks
             efficiently. Our tool is ideal for individuals and teams looking to optimize
             your productivity, keeping all your tasks, notes, and activities perfectly organized
             In one single place. With Master Task, you will be able to focus on what really matters and achieve your goals.
             objectives more easily.
            """, bg='#f1faff', font=('Roborto', 11))
        lblintro.pack(fill='both', expand=True, padx=2, pady=2)

        lblvision = Label(self.framevision, text="""
            At Master Task, our vision is to be the world's leading platform for task management and organization.
             personal and professional. We want to empower millions of people around the world, providing them with the
             tools necessary to lead a more organized, productive and satisfying life. We aspire to be
             synonymous with efficiency and simplicity, revolutionizing the way people manage their time and their
             responsibilities.
            """, bg='#f1faff', font=('Roborto', 11))
        lblvision.pack(fill='both', expand=True, padx=2, pady=2)

        lblmision = Label(self.framemision, text="""
            Our mission at Master Task is to provide an intuitive and powerful application that simplifies task management
             and note taking, significantly improving the productivity and quality of life of our users.
             We are committed to continually developing our platform, integrating the latest technologies and
             recommended practices, to deliver an exceptional user experience. We believe that, with the tools
             Right, everyone has the potential to achieve their goals and maximize their daily performance.
            """, bg='#f1faff', font=('Roborto', 11))
        lblmision.pack(fill='both', expand=True, padx=2, pady=2)


    def back_button(self):
        self.clean_panel(self.main_body)
        self.settings(self.main_body, self.id)

    def clean_panel(self, panel):
        for widget in panel.winfo_children():
            widget.destroy()

        