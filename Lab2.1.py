k=input()
k=k.split()
k2=""
for i in range(len(k)):
    if k[i].endswith('ов'):
        k2=k2+k[i]+''
print(k2)