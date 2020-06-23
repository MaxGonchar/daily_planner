import tkinter as tk
from datetime import date

from task_frames import TaskSlot
import db


class MainWindow(tk.Frame):
    """Main application's window"""

    def __init__(self, window):
        tk.Frame.__init__(self, window)
        self.main_screan()
        self.remember_tasks()

    def main_screan(self):
        """Main frame"""

        self.pack(fill=tk.BOTH, expand=1)
        self.configure(bg='burlywood4')
        #  label for date display
        tk.Label(
            self, text=f'{date.today()}',
            bg='orange4', font='Times 30'
        ).pack(fill=tk.X)

        tk.Button(
            self, text='add task', command=self.add_task
        ).pack(fill=tk.X)

    def add_task(self):
        """"""
        TaskSlot(self).frame.pack(fill=tk.X)

    def remember_tasks(self):
        """"""
        try:
            TaskSlot.task_dict = db.db_read()
            for k, v in TaskSlot.task_dict.items():
                TaskSlot(self, k, v.head, v.body).frame.pack(fill=tk.X)
        except FileNotFoundError:
            pass


def main():
    window = tk.Tk()
    MainWindow(window)
    window.title('Daily Planner')
    window.geometry('365x500')
    window.mainloop()


if __name__ == '__main__':
    main()
