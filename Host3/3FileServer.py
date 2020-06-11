import socket                   # Import socket module

port = 60000                   # Reserve a port for your service.
s = socket.socket()             # Create a socket object
host = ""    # Get local machine name
s.bind((host, port))            # Bind to the port
s.listen(5)                     # Now wait for client connection.

print ('Server listening....')


c, addr = s.accept()     # Establish connection with client.
print ('Got connection from', str(addr))
data = c.recv(1024)
print('Server received', repr(data))
message="which packet do you want?"
c.send(message.encode('ascii'))

data1 = c.recv(10)
strings=str(data1,'utf8')

filename='DataHost3/received_file'+str(strings)
f = open(filename,'rb')
l = f.read(1024)
while (l):
    c.send(l)
    print('Sent ',repr(l))
    l = f.read(1024)
f.close()

print('Done sending')
c.close()
print('connection closed')

