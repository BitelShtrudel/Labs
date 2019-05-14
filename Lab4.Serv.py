import socket
import re

sock = socket.socket()
sock.bind(('', 9000))
sock.listen(1)
serv, addr = sock.accept()
while True:
    print('Ожидание соединения...')
    data = serv.recv(34000)
    print('Соединение установлено.')
    data = data.decode()
    data = re.findall(r'\d+', data)
    a = float(data[0])
    b = float(data[1])
    c = float(data[2])
    f = float(data[3])
    d = float(data[4])

    try:
        result = (abs(a-b*c*d**3+(c**5-a**2)/a+f**3*(a-213)))
        result = 'Ответ = ' + str(result)
        serv.send(result.encode())
    except:
        result = "Sorry, but you cant devide by 0"
        serv.send(result.encode())
