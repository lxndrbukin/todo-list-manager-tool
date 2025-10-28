import tkinter as tk
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
    add_task_button = tk.Button(window, text="Submit")
    add_task_button.pack()

    task_listbox = tk.Listbox(window)
    task_listbox.pack()

    window.mainloop()

if __name__ == "__main__":
    todo()