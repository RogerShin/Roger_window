import os
os.system('clear')
import tkinter as tk
from tkinter import ttk

class Window(tk.Tk):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.title("pack1")
        # 設定視窗大小
        self.geometry('300x200')
        # mac 筆電情況下，需使用tk不能用ttk，如果使用ttk， pack中的fill='both' 執行後會無任何變化
        tk.Button(self, text = "Top").pack(fill = 'both', expand = 1)
        tk.Button(self, text = "Middle").pack(fill = 'both', expand = 1)
        tk.Button(self, text = "Bottom").pack(fill= 'both', expand = 1)

if __name__ == '__main__':
    window:Window = Window()
    window.mainloop()