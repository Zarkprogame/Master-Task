from tkinter import *

class FormTodoDesigner():

    def detail(self, id):
        pass

    def remove(self, id):
        pass

    def complete(self, id):
        pass

    def renderTodo(self):
        pass

    def addTodo(self):
        pass

    def clearTxt(self):
        pass

    def __init__(self, main_panel):
        self.FrameNewTask = LabelFrame(main_panel, padx=5, pady=5, bd=0)
        self.FrameNewTask.pack(side=TOP, expand=NO, fill='both')
        self.FrameNewTask.grid_columnconfigure(1, weight=1)
        
        lblTask = Label(self.FrameNewTask, text='Task', font=('Roboto', 15))
        lblTask.grid(row=0, column=0)

        self.txtTask = Entry(self.FrameNewTask, borderwidth=0, font=("Roborto", 15))
        self.txtTask.grid(row=0, column=1, sticky=W+E, padx=5)
        self.txtTask.focus()

        lblDetail = Label(self.FrameNewTask, text='Detail', font=('Roboto', 15))
        lblDetail.grid(row=1, column=0)

        self.txtDetail = Entry(self.FrameNewTask, borderwidth=0, font=("Roborto", 15))
        self.txtDetail.grid(row=1, column=1, sticky=W+E, padx=5)
        self.txtDetail.bind('<Return>', lambda x:self.addTodo())

        self.btnAdd = Button(self.FrameNewTask, text='Add',command=self.addTodo, background='#03D92D', borderwidth=0, padx=10, font=('Roboto', 11))
        self.btnAdd.grid(row=1, column=2)

        self.FramePendingTask = LabelFrame(main_panel, text='My Pending Tasks', font=("Roborto", 15), padx=5, pady=5)
        self.FramePendingTask.pack(side='top', expand=NO, fill='both')
        self.FramePendingTask.grid_columnconfigure(0, weight=1)
        self.FramePendingTask.grid_columnconfigure(1, weight=1)

        self.FrameCompletedTask = LabelFrame(main_panel, text='My Completed Tasks', font=("Roborto", 15), padx=5, pady=5)
        self.FrameCompletedTask.pack(side='top', expand=NO, fill='both')
        self.FrameCompletedTask.grid_columnconfigure(0, weight=1)
        self.FrameCompletedTask.grid_columnconfigure(1, weight=1)
        

    
        