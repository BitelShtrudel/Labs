k=int(input())
sp=[]
if k<9:
    print ("Вы ввели недопустимое значение")
for i in range(k):
    sp.append(int(input()))
print(k)
i=0
while i<(len(sp)):
    if int(sp[i])%2==0:
        sp.remove(sp[i])
    else:
        i+=1
sp.append('')
sp.append('')
sp.append('')
sp.append('')
sp.append('')
print(sp)
