
import socket                   # Import socket module

conn = socket.socket()             # Create a socket object
host = '127.0.0.1'     
port = 60000                    # Reserve a port for your service.

conn.connect((host, port))
data = conn.recv(1024)
print('message from Server=', (data))

number=input("Enter number")
conn.send(bytes(str(number),'utf8'))

data = conn.recv(1024)
print('message from Server=', (data))

conn.close()
print('connection closed')