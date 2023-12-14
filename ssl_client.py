import socket

client  = socket.socket(socket.AF_INET , socket.SOCK_STREAM)

client.connect((socket.gethostname(),5000))

done = False
try:
    while not done:
        client.send(input('Client : ').encode('utf-8'))
        msg = client.recv(1024).decode('utf-8')
        if msg == 'quit':
            done = True
        else:
            print(msg)

except:
    pass

client.close()