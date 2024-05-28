import os
import tkinter as tk
os.system("cls")

def get_names() -> list[str]:
    with open('names.txt', encoding='utf-8') as files:
        content:str = files.read()
    names:list[str] = content.split()
    return names

class Window(tk.Tk):
    def __init__(self, title:str = "Hello! Tkinter!"):
        super().__init__()
        # 多做一些事
        self.title(title)

if __name__ == '__main__':
    names:list[str] = get_names()
    window:Window = Window(title = "我是第一個GUI程式")
    window.mainloop()
    