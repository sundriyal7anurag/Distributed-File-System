
import socket                   # Import socket module

c = socket.socket()             # Create a socket object
host = socket.gethostname()     
port = 60000                    # Reserve a port for your service.

c.connect((host, port))
mes='Hello server'
c.send(mes.encode('ascii'))

data = c.recv(1024)
print('message Server=', repr(data))

packetnumber=input("Enter packet number of file you wnt")
c.send(bytes(str(packetnumber),'utf8'))

with open('Data/packet'+str(packetnumber), 'wb') as f:
    print ('file opened')
    while True:
        print('receiving data...')
        data = c.recv(1024)
        print('data=%s', (data))
        if not data:
            break
        # write data to a file
        f.write(data)

f.close()
print('Successfully get the file')
c.close()
print('connection closed')