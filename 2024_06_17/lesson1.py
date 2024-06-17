import tkinter as tk
from tkinter import ttk, Misc
from PIL import Image, ImageTk

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

class Example1(ttk.Frame):
    def __init__(self, master:Misc, **kwargs):
        super().__init__(master=master, **kwargs)
        master.title('Colors')
        # 寫法 1:
        self.configure({'borderwidth':2, 'relief':'groove'})
        # 寫法 2:
        # self.config({'borderwidth':2, 'relief':'groove'})
        # 寫法 3:
        # self['borderwidth']=2
        # self['relief']='groove'
        # 畫線
        canvas = tk.Canvas(self)
        # 畫方形, 填色
        canvas.create_rectangle(30, 10 ,120, 80, outline='#000', fill='#fb0')
        # 寫字
        canvas.create_text(40, 40, text="中文測試", anchor='nw', fill='#0a0', font=('Arial', 18, 'bold', 'italic'))
        # 畫圓
        canvas.create_oval(150, 10, 200, 60, outline='#000', fill='#1f1', width=2)
        # 畫圖片
        img = Image.open('tvdi.png')
        self.tvdi = ImageTk.PhotoImage(img)
        canvas.create_image(210, 10, anchor='nw', image=self.tvdi)
        canvas.pack(expand=True, fill='both')
        self.pack(expand=True, fill='both')

class Example2(ttk.Frame):
    def __init__(self, master:Misc, **kwargs):
        super().__init__(master=master, **kwargs)
        master.title('')
        # 寫法 1:
        self.configure({'borderwidth':2, 'relief':'groove'})
        # 寫法 2:
        # self.config({'borderwidth':2, 'relief':'groove'})
        # 寫法 3:
        # self['borderwidth']=2
        # self['relief']='groove'
        # 畫線
        canvas = tk.Canvas(self)
        
        canvas.pack(expand=True, fill='both')
        self.pack(expand=True, fill='both')

def main():
    window = tk.Tk()
    window.title("Frame的繼承")
    Example2(window)
    window.geometry("400x400")
    window.mainloop()

if __name__ == '__main__':
    main()