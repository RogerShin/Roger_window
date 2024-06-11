from tkinter import Frame, Misc
from tkinter.simpledialog import Dialog
from tkinter import ttk
import tkinter as tk

class CustomMessagebox(Dialog):
    def __init__(self, parent:Misc, title, name:str, bmi:float, status:str, advice:str):
        self.name = name
        self.bmi = bmi
        self.status = status
        self.advice = advice
        super().__init__(parent = parent, title = title)
    
    def body(self, master: Frame):
        # 創建對話框主體, 返回應具有初始焦點的控件
        input_frame = ttk.Frame(self, width=100, height=100, style='input.TFrame')
        input_frame.pack(pady=10, padx=30)

        # 姓名
        label_name = tk.Label(input_frame, text="姓名:")
        label_name.grid(row=0, column=0, padx=5, pady=5, sticky=tk.E)

        self.value_name = tk.Label(input_frame, text=self.name)
        self.value_name.grid(row=0, column=1, padx=5, pady=5)

        # BMI
        label_bmi = ttk.Label(input_frame, text="BMI:")
        label_bmi.grid(row=1, column=0, padx=5, pady=5, sticky=tk.E)

        self.value_bmi = ttk.Label(input_frame, text= f"{self.bmi:.2f}")
        self.value_bmi.grid(row=1, column=1, padx=5, pady=5)

        # status
        label_status = ttk.Label(input_frame, text="體重 (kg):")
        label_status.grid(row=2, column=0, padx=5, pady=5, sticky=tk.E)

        self.value_status = ttk.Label(input_frame, text= self.status)
        self.value_status.grid(row=2, column=1, padx=5, pady=5)

        # advice
        label_advice = ttk.Label(input_frame, text="建議:")
        label_advice.grid(row=3, column=0, padx=5, pady=5, sticky=tk.E)

        self.value_advice = ttk.Label(input_frame, text= self.advice)
        self.value_advice.grid(row=3, column=1, padx=5, pady=5)

        return