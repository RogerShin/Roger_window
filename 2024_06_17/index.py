from ttkthemes import ThemedTk
import tkinter as tk
from tkinter import ttk, messagebox, Misc
import ubikedata
from ubikedata import FilterData, Info
from tools import CustomMessagebox

class Window(ThemedTk):
    # 自定義
    def __init__(self, theme:str='arc', **kwargs):
        # 呼叫父類別
        super().__init__(theme=theme, **kwargs)
        self.title("台北市YouBike2.0及時資料")

        try:
            self.__data = ubikedata.load_data()
        except Exception as e:
            messagebox.showwarning(title='警告',message=str(e))

        self._display_interface()
    
    @property
    def data(self) -> list[dict]:
        return self.__data

    def _display_interface(self):
       mainFrame = ttk.Frame(borderwidth=1, relief='groove')
       ttk.Label(mainFrame, text="台北市YouBike2.0及時資料", font=('arial', 25)).pack(pady=(20,10))

       # =================================================
       tableFrame = ttk.Frame(mainFrame)
       columns = ('sna', 'sarea', 'mday', 'ar', 'total', 'rent_bikes', 'retuen_bikes')
       # browse 只能單選
       tree = ttk.Treeview(tableFrame, columns=columns, show='headings', selectmode='browse')

       # define headings
       tree.heading('sna', text='站點')
       tree.heading('sarea', text='行政區')
       tree.heading('mday', text='時間')
       tree.heading('ar', text='地址')
       tree.heading('total', text='總數')
       tree.heading('rent_bikes', text='可借')
       tree.heading('retuen_bikes', text='可還')
       
       # 定義欄位寬度
       tree.column('sarea', width=70, anchor='center')
       tree.column('mday', width=120, anchor='center')
       tree.column('ar', minwidth=100)
       tree.column('total', width=50, anchor='center')
       tree.column('rent_bikes', width=50, anchor='center')
       tree.column('retuen_bikes', width=50, anchor='center')

       # bind使用者的事件
       tree.bind('<<TreeviewSelect>>', self.item_selected)

       # generate sample data
    #    contacts = []
    #    for n in range(1, 100):
    #         contacts.append((f'first {n}', f'last {n}', f'email{n}@example.com'))
        
       # add data to the treeview
       for site in self.data:
            tree.insert('', tk.END, values=(site['sna'], site['sarea'], site['mday'], site['ar'], site['total'],site['rent_bikes'],site['retuen_bikes']))

       tree.grid(row=0, column=0, sticky='nsew')

       scrollbar = ttk.Scrollbar(tableFrame, orient=tk.VERTICAL, command=tree.yview)
       tree.configure(yscroll=scrollbar.set)
       scrollbar.grid(row=0, column=1, sticky='ns')
       tableFrame.pack(expand=True,fill=tk.BOTH, padx=20,pady=20)
       #=====================================================
       pieChartFrame = PieChartFrame(mainFrame)
       pieChartFrame.pack(expand=True, fill='both')
       mainFrame.pack(expand=True,fill=tk.BOTH,padx=10,pady=10)
    
    def item_selected(self, event):
        tree = event.widget
        for selected_item in tree.selection():
            item = tree.item(selected_item)
            record:list = item['values']
            print(record)

class PieChartFrame(ttk.Frame):
    def __init__(self, master:Misc, **kwargs):
        super().__init__(master=master, **kwargs)
        # 寫法 1:
        self.configure({'borderwidth':2, 'relief':'groove'})
        # 寫法 2:
        # self.config({'borderwidth':2, 'relief':'groove'})
        # 寫法 3:
        # self['borderwidth']=2
        # self['relief']='groove'
        # 畫線
        canvas = tk.Canvas(self)
        canvas.create_line(15, 30, 200, 30, fill='black')
        canvas.create_line(300, 35, 300, 200, dash=(8, 2), fill='black')
        canvas.create_line(55, 85, 155, 85, 105, 180, 55, 85, fill='black')
        canvas.pack(expand=True, fill='both')
        self.pack(expand=True, fill='both')



def main(): 
    window = Window(theme='breeze')
    window.mainloop()

if __name__ == '__main__':
    main()