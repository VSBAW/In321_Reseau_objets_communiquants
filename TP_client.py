import socket
TCP_IP = '127.0.0.1'
TCP_PORT = 55000
BUFFER_SIZE = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
while True:
    message = input("Enter message to send: ")
    s.send(message.encode())
    data = s.recv(BUFFER_SIZE)
    print('received data:', data.decode())
    if message.lower() == 'quit':
        break
s.close()
