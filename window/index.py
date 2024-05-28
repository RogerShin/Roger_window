import os
os.system("cls")
with open('names.txt', encoding='utf-8') as files:
    content:str = files.read()

names:list[str] = content.split()
# for name in names:
#     print(name)