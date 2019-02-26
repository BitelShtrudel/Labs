import random

print ("Введите границы")
a = int(input())
b = int(input())
y = random.randint(a, b)
x = int(input())
while(x!=y):
    if(x>y):
        print("Ответ не верен. Заданное число меньше...")
    else: print("Ответ не верен. Заданное число больше...")
    x=int(input())
print("Это верный ответ!")
