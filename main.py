import tkinter as tk
from tkinter import messagebox, ttk
from styling import *
import os
import json

window = tk.Tk()
window.title("To-do List")
window.geometry("300x400")
style = ttk.Style()
style.theme_use("clam")
style.configure("Tall.Treeview", rowheight=48, font=("Arial", 11))

def todo():
    file_path = os.path.join(os.path.dirname(__file__), "tasks.json")
    if not os.path.exists(file_path):
        with open(file_path, "w") as file:
            json.dump([], file)

    ttk.Label(window, text="Enter task:", font=font_normal).pack()
    input = ttk.Entry(window)
    input.pack()

    tasks = []

    def add_task():
        task_entry = input.get()
        if task_entry:
            task_data = {}
            with open(file_path, "r") as file:
                data = json.load(file)
            max_id = 1 if not data else max(data, key=lambda x: x.get("id", float("-inf")))["id"] + 1
            task_data = {"id": max_id, "task": task_entry, "status": "In-Progress"}
            data.append(task_data)
            tasks.append(task_data)
            with open(file_path, "w") as file:
                json.dump(data, file)
            task_listbox.insert('', tk.END, iid=len(data)-1, values=(task_data["id"], task_data["task"], task_data["status"]))
            input.delete(0, tk.END)

    ttk.Button(window, text="Submit", command=add_task).pack()
    ttk.Label(window, text="Tasks:",  font=font_normal).pack()

    task_listbox_frame = tk.Frame(window)
    task_listbox_frame.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)
    task_listbox = ttk.Treeview(task_listbox_frame, columns=["id", "task", "status"], show="headings", style="Tall.Treeview")
    task_listbox.heading("id", text="ID")
    task_listbox.heading("task", text="Task")
    task_listbox.heading("status", text="Status")
    task_listbox.column("id", width=90, minwidth=75, stretch=False, anchor='center')
    task_listbox.column("task", anchor='center')
    task_listbox.column("status", width=200, minwidth=150, stretch=False, anchor='center')
    task_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    scrollbar = tk.Scrollbar(task_listbox_frame, orient=tk.VERTICAL)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    task_listbox.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=task_listbox.yview)

    def get_tasks():
        if os.path.exists(file_path):
            with open(file_path, "r") as file:
                tasks.extend(json.load(file))
            for i, item in enumerate(tasks):
                task_listbox.insert('', tk.END, iid=i, values=(item["id"], item["task"], item["status"]))

    get_tasks()

    def delete_task():
        selected = task_listbox.selection()
        if selected:
            for item in selected:
                task_to_delete = tasks[int(item)]
                tasks.pop(int(item))
                task_listbox.delete(item)
                messagebox.showinfo("Task Deleted", f"Deleted task: {task_to_delete["id"]}")
            with open(file_path, "w") as file:
                json.dump(tasks, file)
    
    window.bind("<Return>", lambda event: add_task())
    window.bind("<Delete>", lambda event: delete_task())

    window.mainloop()

if __name__ == "__main__":
    try:
        todo()
    except KeyboardInterrupt:
        print("Program stopped by user")