import os
import os.path
import sys

gl_list = []
def main_menu():
    c="8"
    while c !="0":
        print('''
        0 - Выход из программы
        1 - Подсчет количества файлов в директории
        2 - Вывод информации о товарах, отсортированных по количеству
        3 - Сортировка 2 + увеличение ццены на товары, указанные пользавателем
        4 - 3 задание + сохранение
        ''')
        c=input("\n" + "Введите команду" + " ")
        while c not in ["1", "2", "3", "4", "0"]:
            c=input("Нет такой команды. Введите 1,2,3,4,0 \n")
        if c == "0":
            sys.exit()
        if c == "1":
            k_failov()
            exit()
        if c == "2":
            sortirovka()
            exit()
        if c == "3":
            increase()
            exit()
        if c == "4":
            save(gl_list)
            exit()
def exit():
    r = input("Продолжить?")
    while r not in ("да", "yes", "Y", "1", "нет", "no", "N", "0"):
        print ("Ошибка")
        r = input ("Продолжить?")
    if r in ["да", "yes", "Y", "1"]:
        main_menu()
    elif r in ["нет", "no", "N", "0"]:
        sys.exit()

def k_failov():
    a = input("Введите директорию \n")
    files = os.listdir(a)
    c = len(files)
    print("В папке" + str(c) + "файла(ов)")

def sortirovka():
    global gl_list

    text_file = open('products.txt', 'r')
    lines = text_file.readlines()
    for i in range(0, len(lines)):
        list1 = lines[i].strip()
        list1 = list1.split(";")
        lines[i] = list1
    new_list = sorted(lines, key=lambda j: j[2], reverse=True)
    for i in range(0, len(new_list)):
        print(new_list[i][0].ljust(5) + " " + new_list[i][1].ljust(21) + " " + new_list[i][2].ljust(6) + " " + new_list[i][3].ljust(10))
    gl_list = new_list
    text_file.close()
    return gl_list

def increase():
    sortirovka()
    text_file = open('products.txt', 'r')
    lines = text_file.readlines()
    for i in range(0, len(lines)):
        list1 = lines[i].strip()
        list1 = list1.split(";")
        lines[i] = list1
    print(lines)
    a = input("Введите через запятую номера товаров, в которых нужно увеличить цену\n")
    a = a.split(",")
    c = input("Введите число, на которое нужно увеличить цену.\n")
    for j in range(0, len(a)):
        n = int(a[j])
        k = int(lines[n][2])
        k = k + int(c)
        lines[n][2] = str(k)
    print(lines)
    text_file.close()
    return gl_list

def save(gl_list):
    gl_list = increase()
    f = input('''Где сохранить?
1. Новый файл
2. Старый файл
''')
    while f not in ['1','2']:
        f = input('Введите 1 или 2')
    if f == "2":
        with open('products.txt','w') as f:
            i = 0
            while i<len(gl_list):
                string = ';'.join(gl_list[i])
                f.write(string+'\n')
                i+=1
    elif f == "1":
        link=input ('Введите путь к директории: \n')
        with open(link+"\products.txt","w") as f:
            i = 0
            while i < len(gl_list):
                string = ';'.join(gl_list[i])
                f.write(string + '\n')
                i+=1
    print('Сохранено')
main_menu()







