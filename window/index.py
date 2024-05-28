import os
os.system("cls")

def get_names() -> list[str]:
    with open('names.txt', encoding='utf-8') as files:
        content:str = files.read()
    names:list[str] = content.split()
    return names

if __name__ == '__main__':
    names:list[str] = get_names()
    print(names)
