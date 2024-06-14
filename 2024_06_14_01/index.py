
from ttkthemes import ThemedTk
import tkinter as tk
from tkinter import ttk, messagebox
import ubikedata

class Window(ThemedTk):
    # 自定義
    def __init__(self, theme:str='arc', **kwargs):
        # 呼叫父類別
        super().__init__(theme=theme, **kwargs)
        try:
            self.__data = ubikedata.load_data()
        except Exception as e:
            messagebox.showwarning(title='警告',message=str(e))

        @property
        def data(self) -> list[dict]:
            return self.__data




def main():
    window = Window(theme='breeze')
    window.mainloop()

if __name__ == '__main__':
    main()