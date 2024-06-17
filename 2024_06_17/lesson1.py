import tkinter as tk
from tkinter import ttk, Misc

# 繼承ttk.Frame
class Example(ttk.Frame):
    def __init__(self, master:Misc, **kwargs):
        super().__init__(master=master, **kwargs)
        master.title('Lines')
        # 寫法 1:
        self.configure({'borderwidth':2, 'relief':'groove'})
        # 寫法 2:
        # self.config({'borderwidth':2, 'relief':'groove'})
        # 寫法 3:
        # self['borderwidth']=2
        # self['relief']='groove'
        # 畫線
        canvas = tk.Canvas(self)
        canvas.create_line(15, 30, 200, 30)
        canvas.create_line(300, 35, 300, 200, dash=(8, 2))
        canvas.create_line(55, 85, 155, 85, 105, 180, 55, 85)
        canvas.pack(expand=True, fill='both')
        self.pack(expand=True, fill='both')


def main():
    window = tk.Tk()
    window.title("Frame的繼承")
    Example(window)
    window.geometry("400x250")
    window.mainloop()

if __name__ == '__main__':
    main()