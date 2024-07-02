import ubikedata
from ttkthemes import ThemedTk

class Window(ThemedTk):
    def __init__(self, theme:str|None, **kwargs):
        super().__init__(**kwargs)
        try:
            ubike:list[dict] = ubikedata.load_data()
        except Exception as error:
            print(error)
        else:
            print(ubike)

def main():
    window = Window(theme='arc')
    window.mainloop()

if __name__ == '__main__':
    main()