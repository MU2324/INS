import socket

server = socket.socket(socket.AF_INET , socket.SOCK_STREAM)

server.bind((socket.gethostname(),5000))
server.listen()

client , address = server.accept()

done = False

try:
    while not done:
        msg = client.recv(1024).decode('utf-8')
        if msg == 'quit':
            done = True
        else:
            print(msg)
        client.send(input('Server : ').encode('utf-8'))

except:
    pass

client.close()
server.close()