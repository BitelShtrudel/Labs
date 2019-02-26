import math

a = int(input())
b = int(input())
c = int(input())
d = int(input())
f = int(input())
try:
    print (abs(a-b*c*d**3+(c**5-a**2)/a+f**3*(a-213)))
except ZeroDivisionError:
    print ("Calculation isn't possible")
