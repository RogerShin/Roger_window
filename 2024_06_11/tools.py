from tkinter import Frame, Misc
from tkinter.simpledialog import Dialog
from tkinter import ttk
import tkinter as tk

class CustomMessagebox(Dialog):
    def __init__(self, parent:Misc, title, name:str, bmi:float, status:str, advice:str):
        self.parent = parent
        self.name = name
        self.bmi = bmi
        self.status = status
        self.advice = advice
        super().__init__(parent = parent, title = title)
    
    def body(self, master: Frame):
        # 創建對話框主體, 返回應具有初始焦點的控件
        contain_frame = ttk.Frame(master, style='input.TFrame')
        contain_frame.pack(pady=10, padx=30)

        # 姓名
        label_name = tk.Label(contain_frame, text="姓名:")
        label_name.grid(row=0, column=0, padx=5, pady=5, sticky=tk.E)

        self.value_name = tk.Label(contain_frame, text=self.name)
        self.value_name.grid(row=0, column=1, padx=5, pady=5)

        # BMI
        label_bmi = ttk.Label(contain_frame, text="BMI值:")
        label_bmi.grid(row=1, column=0, padx=5, pady=5, sticky=tk.E)

        self.value_bmi = ttk.Label(contain_frame, text= f"{self.bmi:.2f}")
        self.value_bmi.grid(row=1, column=1, padx=5, pady=5)

        # status
        label_status = ttk.Label(contain_frame, text="狀態:")
        label_status.grid(row=2, column=0, padx=5, pady=5, sticky=tk.E)

        self.value_status = ttk.Label(contain_frame, text= self.status)
        self.value_status.grid(row=2, column=1, padx=5, pady=5)

        # advice
        label_advice = ttk.Label(contain_frame, text="建議:")
        label_advice.grid(row=3, column=0, padx=5, pady=5, sticky=tk.E)

        self.value_advice = ttk.Label(contain_frame, text= self.advice)
        self.value_advice.grid(row=3, column=1, padx=5, pady=5)

    def apply(self):
        # 當用戶按下確定時處裡數據
        self.parent.name_value.set('')
        self.parent.height_value.set('')
        self.parent.weight_value.set('')