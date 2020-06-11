import socket                   # Import socket module

port = 60000                   # Reserve a port for your service.
s = socket.socket()             # Create a socket object
host = ""    # Get local machine name
s.bind((host, port))            # Bind to the port
s.listen(5)                     # Now wait for client connection.

print ('Server listening....')

conn, addr = s.accept()     # Establish connection with client.
print ('Got connection from', str(addr))

mes='which packet do you want?'
conn.send(mes.encode('ascii'))

data1 = conn.recv(50)
strings=str(data1,'utf8')
packetnumber=int(strings)
print("message from client=")
print("packetnumber is="+str(packetnumber))

if packetnumber%2==0:
  mes='Go to Host 2 or Host 4'
else:
  mes='Go to Host 1 or Host 3'

conn.send(mes.encode('ascii'))
conn.close()