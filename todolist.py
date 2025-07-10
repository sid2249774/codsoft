import tkinter as tk
from tkinter import simpledialog, messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.tasks = []

        self.frame = tk.Frame(root)
        self.frame.pack()

        self.task_listbox = tk.Listbox(self.frame, width=50, height=15)
        self.task_listbox.pack()

        self.entry = tk.Entry(self.frame, width=50)
        self.entry.pack()

        self.add_button = tk.Button(self.frame, text="Add Task", command=self.add_task)
        self.add_button.pack(side="left")

        self.update_button = tk.Button(self.frame, text="Update Task", command=self.update_task)
        self.update_button.pack(side="left")

        self.delete_button = tk.Button(self.frame, text="Delete Task", command=self.delete_task)
        self.delete_button.pack(side="left")

    def add_task(self):
        task = self.entry.get()
        if task:
            self.tasks.append(task)
            self.refresh()

    def update_task(self):
        selected = self.task_listbox.curselection()
        if selected:
            index = selected[0]
            new_task = simpledialog.askstring("Update Task", "Enter new task:", initialvalue=self.tasks[index])
            if new_task:
                self.tasks[index] = new_task
                self.refresh()

    def delete_task(self):
        selected = self.task_listbox.curselection()
        if selected:
            index = selected[0]
            del self.tasks[index]
            self.refresh()

    def refresh(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
