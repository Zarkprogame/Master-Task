from tkinter import *
from tkinter import messagebox
import sqlalchemy as db
from models.models import Todo
from sqlalchemy.orm import Session
from util.generic import root_center
from views.master.todo.form_Todo_Designer import FormTodoDesigner

class FormTodo(FormTodoDesigner):
    def __init__(self,main_panel, id):
        super().__init__(main_panel)
        self.engine = db.create_engine('sqlite:///database/login.sqlite', echo=False, future=True)
        self.session = Session(bind=self.engine)
        self.id = id
        self.renderTodo()

    def detail(self, id):
        def _detail():
            topDetail = Toplevel()
            topDetail.title('Detail Task')
            topDetail.resizable(0,0)
            topDetail.iconbitmap("./img/logo.ico")
            root_center(topDetail, 500, 200)

            todo = self.session.query(Todo).get(id)
            name = todo.task
            detail = todo.detail

            topFrame = LabelFrame(topDetail, text=name, padx=5, pady=5, width=200, font=('Roboto', 15))
            topFrame.pack(side='top')

            lblDetail = Label(topFrame, text=detail, width=39, wraplength=290, font=('Roboto', 11))
            lblDetail.grid(row=0, column=0)
        return _detail

    def remove(self, id):
        def _remove():
            answer = messagebox.askokcancel("Delete Task","Are you sure that you want to Delete this Task?")
            if answer:
                todo = self.session.query(Todo).get(id)
                self.session.delete(todo)
                self.session.commit()
                self.renderTodo()
                messagebox.showinfo("Info", "The Task has been Deleted")
            else:
                messagebox.showinfo("Info", "No Task has been Deleted")
        return _remove

    def complete(self, id):
        def _complete():
            todo = self.session.query(Todo).get(id)
            todo.completed = not todo.completed
            self.session.add(todo)
            self.session.commit()
            self.renderTodo()
        return _complete

    def renderTodo(self):
        
        todos = self.session.query(Todo).filter(Todo.user_id == self.id).all()

        for frame in [self.FramePendingTask, self.FrameCompletedTask]:
            for widget in frame.winfo_children():
                widget.destroy()

        for i, todo in enumerate(todos):
            todo_id = todo.id
            name = todo.task
            completed = todo.completed
            color = '#555555' if completed else '#000000'
            frame = self.FrameCompletedTask if completed else self.FramePendingTask

            checkbox = Checkbutton(frame, text=name, fg=color, width=42, anchor='w', font=('Roboto', 11), command=self.complete(todo_id))
            checkbox.grid(row=i, column=0, sticky='w')
            checkbox.select() if completed else checkbox.deselect()

            btnDelete = Button(frame, text='Delete', borderwidth=0, background='#CB3234', padx=3, pady=3, font=('Roboto', 11), command=self.remove(todo_id))
            btnDelete.grid(row=i, column=2, pady=2, sticky='e')

            btnDetail = Button(frame, text='Detail', borderwidth=0, background='#6aa9e9', padx=3, pady=3, font=('Roboto', 11), command=self.detail(todo_id))
            btnDetail.grid(row=i, column=1, pady=2, padx=5, sticky='e')

            self.clearFrame()

    def addTodo(self):
        name = self.txtTask.get()
        detail = self.txtDetail.get()
        todo = Todo(task=name, detail=detail, completed=False, user_id=self.id)
        if not name:
            messagebox.showinfo("Info", 'Give your Task a Title')
        elif not detail:
            messagebox.showinfo("Info", 'Give your Task a Detail')
        elif len(name) < 5:
            messagebox.showinfo("Info", 'This Task name is too Short')
        elif len(detail) < 10:
            messagebox.showinfo("Info", 'This Task detail is too Short')
        elif len(name) > 52:
            messagebox.showinfo("Info", 'This Task name is too long, choose a shorter one')
        elif len(detail) > 200:
            messagebox.showinfo("Info", 'This Task Detail is too long')
        else:
            self.session.add(todo)
            self.session.commit()
            self.session.close()
            self.clearTxt()
            self.renderTodo()
            self.clearTxt() 
        
    def clearTxt(self):
        self.txtTask.delete(0,END)
        self.txtDetail.delete(0,END)

    def clearFrame(self):
        if not self.FrameCompletedTask.winfo_children():
            self.FrameCompletedTask.pack_forget()
        else:
            self.FrameCompletedTask.pack(side='top', expand=NO, fill='both')
