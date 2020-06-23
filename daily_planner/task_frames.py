import tkinter as tk
from datetime import datetime, date, timedelta

from task import Task
import db


class TaskSlot:
    """"""
    task_dict = {}

    def __init__(self, root, name=None, head='task',
                 body='description'):
        """"""
        self.root = root
        self.name = name
        self.head = head
        self.body = body
        self.sub_win = None
        self.frame = tk.Frame(self.root, bd=5, relief='sunken')
        self.lab = tk.Label(self.frame, text=self.head)
        self.lab.pack(side=tk.LEFT)
        tk.Button(self.frame, text='O', command=self.put_off).pack(side=tk.RIGHT)
        tk.Button(self.frame, text='V', command=self.done).pack(side=tk.RIGHT)
        tk.Button(self.frame, text='text', command=self.text).pack(side=tk.RIGHT)

        if not self.name:
            self.name = hash(datetime.now())
            self.task_dict[self.name] = Task(self.head, self.body)
            db.db_write(self.task_dict)

    def exit(self):
        """"""
        self.sub_win.forget(window=self.sub_win)
        self.sub_win = None

    def text(self):
        """"""
        if not self.sub_win:
            self.sub_win = tk.Toplevel()
            self.sub_win.protocol('WM_DELETE_WINDOW', self.exit)

            flag = True
            self.h_var = tk.StringVar()

            def foo(*args):
                nonlocal flag
                self.change(headline, description)
                add.forget()
                flag = True

            add = tk.Button(
                self.sub_win, text='add',
                command=(lambda: foo(headline, description))
            )

            def app(*args):
                nonlocal flag
                if flag:
                    add.pack(side=tk.LEFT)
                    flag = False

            tk.Label(self.sub_win, text='headline').pack(anchor=tk.NW)
            headline = tk.Entry(self.sub_win, textvariable=self.h_var)
            headline.pack(anchor=tk.NW, fill=tk.BOTH)
            headline.insert(0, self.task_dict[self.name].head)
            self.h_var.trace('w', app)

            tk.Label(self.sub_win, text='description').pack(anchor=tk.NW)
            description = tk.Text(self.sub_win, width=30, height=10)
            description.pack(fill=tk.BOTH)
            description.insert(1.0, self.task_dict[self.name].body)
            description.bind('<Key>', lambda event: app())

            tk.Button(
                self.sub_win, text='exit', command=self.exit
            ).pack(side=tk.RIGHT)

    def change(self, head, body):
        """"""
        self.task_dict[self.name].head = head.get()
        self.task_dict[self.name].body = body.get(0.1, tk.END)
        self.lab.config(text=head.get())
        db.db_write(self.task_dict)

    def done(self):
        """"""
        del self.task_dict[self.name]
        db.db_write(self.task_dict)
        self.frame.destroy()

    def put_off(self):
        """"""
        ...


