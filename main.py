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

if __name__ == "__main__":
    todo()