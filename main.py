import tkinter as tk
from tkinter import messagebox
import os
import json

window = tk.Tk()
window.title("To-do List")
window.geometry("300x400")

def todo():
    file_path = os.path.join(os.path.dirname(__file__), "tasks.json")
    if not os.path.exists(file_path):
        with open(file_path, "w") as file:
            json.dump([], file)

    input_label = tk.Label(window, text="Enter task:")
    input_label.pack()
    input = tk.Entry(window)
    input.pack()

    tasks = []

    def add_task():
        task_entry = input.get()
        if task_entry:
            with open(file_path, "r") as file:
                data = json.load(file)
            if not data:
                data = [{"id": 1, "task": task_entry, "status": "In-Progress"}]
            else:
                max_id = max(data, key=lambda x: x.get("id", float("-inf")))["id"] + 1
                data.append({"id": max_id, "task": task_entry, "status": "In-Progress"})
            with open(file_path, "w") as file:
                json.dump(data, file)
            task_listbox.insert(tk.END, task_entry)
            input.delete(0, tk.END)

    add_task_button = tk.Button(window, text="Submit", command=add_task)
    add_task_button.pack()

    task_listbox = tk.Listbox(window)
    task_listbox.pack()

    def get_tasks():
        if os.path.exists(file_path):
            with open(file_path, "r") as file:
                tasks.extend(json.load(file))
            for item in tasks:
                task_listbox.insert(tk.END, item["task"])

    get_tasks()
    
    def delete_task():
        selected = task_listbox.curselection()
        if selected:
            task_to_delete = tasks.pop(selected[0])
            task_listbox.delete(selected)
            messagebox.showinfo("Task Deleted", f"Deleted task: {task_to_delete["task"]}")
            with open(file_path, "w") as file:
                json.dump(tasks, file)
    
    window.bind("<Return>", lambda event: add_task())
    window.bind("<Delete>", lambda event: delete_task())

    window.mainloop()

if __name__ == "__main__":
    todo()