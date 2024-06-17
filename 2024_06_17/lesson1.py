import tkinter as tk
from tkinter import ttk, Misc

# 繼承ttk.Frame
class Example(ttk.Frame):
    def __init__(self, master:Misc, **kwargs):
        super().__init__(master=master, **kwargs)
        master.title('Lines')
        # 寫法 1:
        # self.configure({'borderwidth':2, 'relief':'groove'})
        # 寫法 2:
        # self.config({'borderwidth':2, 'relief':'groove'})
        # 寫法 3:
        # self['borderwidth']=2
        # self['relief']='groove'
        self.pack(expand=True, fill='both')


def main():
    window = tk.Tk()
    window.title("Frame的繼承")
    Example(window)
    window.geometry("400x250")
    window.mainloop()

if __name__ == '__main__':
    main()