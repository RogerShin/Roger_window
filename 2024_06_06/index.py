import os
os.system("cls")
from pprint import pprint
import tkinter as tk
from tkinter import ttk, Misc, Frame, Event
from ttkthemes import ThemedTk
from tkinter import messagebox
from tkinter.simpledialog import Dialog
import tools
from datetime import datetime

class Window(ThemedTk):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.title("AQI顯示")
        # self.option_add("*Font", "微軟正黑體 40")
        style = ttk.Style()
        style.configure("Top.TFrame")
        style.configure("Top.TLabel",font=('Helvetica', 25, "bold", "italic"))        
        title_frame = ttk.Frame(self, style='Top.TFrame', borderwidth=2, relief='groove')
        ttk.Label(title_frame, text="全台空氣品質指標(AQI)", style='Top.TLabel').pack(expand=True, fill='y')
        title_frame.pack(ipadx=100, ipady=30, padx=10, pady=10)

        func_frame = ttk.Frame(self, style='Top.TFrame', borderwidth=1, relief='groove')
        ttk.Button(func_frame, text="AQI品質最好的5個", command=self.click1).pack(side='left', expand=True, ipadx=15, ipady=15)
        ttk.Button(func_frame, text="AQI品質最差的5個", command=self.click2).pack(side='left', expand=True, ipadx=15, ipady=15)
        ttk.Button(func_frame, text="pm2.5品質最好的5個", command=self.click3).pack(side='left', expand=True, ipadx=15, ipady=15)
        ttk.Button(func_frame, text="pm2.5品質最差的5個", command=self.click4).pack(side='left', expand=True, ipadx=15, ipady=15)
        func_frame.pack(ipadx=100, ipady=30, padx=10, pady=10)
    
    def download_parse_data(self) -> list[dict] | None:
        try:
            all_data:dict[any] = tools.download_json()
        except Exception as error:
            messagebox.showwarning("出現錯誤", "出現小錯誤, 請稍後再試!")
            return None
        else:
            data:list[dict] = tools.get_data(all_data)
            return data

    def update_data(self):
        if (tools.AQI.aqi_records is None) or (tools.AQI.update_time is None):
           tools.AQI.aqi_records = self.download_parse_data()
           tools.AQI.update_time = datetime.now()
        # 現在時間減去更新時間
        elif((datetime.now() - tools.AQI.update_time).seconds >= 60 * 60):
           tools.AQI.aqi_records = self.download_parse_data()
           tools.AQI.update_time = datetime.now()
    
    def click1(self):
       self.update_data()
       data:list[dict] = tools.AQI.aqi_records
       sorted_data:list[dict] = sorted(data,key = lambda value:value["aqi"])
       best_aqi:list[dict] = sorted_data[:5]
       def abc(value:dict) -> str:
           return f"{value['county']} - {value['site_name']} - aqi:{value['aqi']} - 狀態:{value['status']} - {value['date']}"
       message_data:list[str]= list(map(abc, best_aqi))
       message = "\n".join(message_data)
       ShowInfo(parent=self,title="全台aqi最佳前5個區域", message=message)

    def click2(self):
        self.update_data()
        data:list[dict] = tools.AQI.aqi_records
        sorted_data:list[dict] = sorted(data,key = lambda value:value["aqi"],reverse=True)
        best_aqi:list[dict] = sorted_data[:5]
        def abc(value:dict) -> str:
           return f"{value['county']} - {value['site_name']} - aqi:{value['aqi']} - 狀態:{value['status']} - {value['date']}"
        message_data:list[str]= list(map(abc, best_aqi))
        message = "\n".join(message_data)
        ShowInfo(parent=self,title="全台aqi最差5個區域", message=message)

    def click3(self):
        self.update_data()
        data:list[dict] = tools.AQI.aqi_records
        sorted_data:list[dict] = sorted(data,key = lambda value:value["pm25"])
        best_aqi:list[dict] = sorted_data[:5]
        def abc(value:dict) -> str:
           return f"{value['county']} - {value['site_name']} - pm2.5:{value['pm25']} - 狀態:{value['status']} - {value['date']}"
        message_data:list[str]= list(map(abc, best_aqi))
        message = "\n".join(message_data)
        ShowInfo(parent=self,title="全台pm2.5最佳5個區域", message=message)

    def click4(self):
        self.update_data()
        data:list[dict] = tools.AQI.aqi_records
        sorted_data:list[dict] = sorted(data,key = lambda value:value["pm25"], reverse=True)
        best_aqi:list[dict] = sorted_data[:5]
        def abc(value:dict) -> str:
           return f"{value['county']} - {value['site_name']} - pm2.5:{value['pm25']} - 狀態:{value['status']} - {value['date']}"
        message_data:list[str]= list(map(abc, best_aqi))
        message = "\n".join(message_data)
        ShowInfo(parent=self,title="全台pm2.5最差5個區域", message=message)

class ShowInfo(Dialog):
    def __init__(self, parent:Misc, title:str | None = None, message:str=""):
        # 需在super().__init__前執行
        self.message = message
        super().__init__(parent=parent, title=title)

    def body(self, master:Frame) -> Misc|None:
        text = tk.Text(self, height=8, font=('Helvetica', 15), width=50)
        text.pack(padx=10, pady=10)
        text.insert(tk.INSERT, self.message)
        text.config(state='disabled')
        return None
    
    def apply(self) -> None:
        '''
        使用者按下內建的ok button,會執行的內容
        '''
        print("使用者按下OK了")

    def buttonbox(self) -> None:
        '''
        自訂button
        '''
        box = tk.Frame(self)
        self.ok_button = tk.Button(box, text="確定", width=10, command=self.ok)
        self.ok_button.pack(pady=(20,30), ipady=10)
        box.pack()
    
    def ok(self) -> None:
        print("OK button was clicked!")
        super().ok()

def main():
    '''
    try:
        all_data:dict[any] = tools.download_json()
    except Exception as error:
        print(error)
    else:
        data:list[dict] = tools.get_data(all_data)
        pprint(data)
    '''

window = Window(theme="arc")
window.mainloop()

if __name__ == '__main__':
    main()