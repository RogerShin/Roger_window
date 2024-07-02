import os
import tkinter as tk
from tkinter import ttk
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
        # 視窗大小
        # self.geometry('300x300')
        # 寫到視窗內的內容
        label:ttk.Label = ttk.Label(self,
                                    text = "Hello! World!",
                                    font = ('Arial', 20, 'bold'),
                                    foreground = 'red')
        label.pack(padx = 100, pady = 40)
        
if __name__ == '__main__':
    names:list[str] = get_names()
    window:Window = Window(title = "我是第一個GUI程式")
    window.mainloop()
    