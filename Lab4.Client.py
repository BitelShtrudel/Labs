import socket
sock = socket.socket()
sock.connect(('localhost', 9000))

s = []
a = input("Введите a - ")
b = input("Введите b - ")
c = input("Введите c - ")
d = input("Введите d - ")
f = input("Введите f - ")

s.append(a)
s.append(b)
s.append(c)
s.append(d)
s.append(f)
s = str(s)
sock.send(s.encode())

result = sock.recv(34000)
result = result.decode()
sock.close()
print(result)
