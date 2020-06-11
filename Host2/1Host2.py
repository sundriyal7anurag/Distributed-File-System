# Import socket module 
import socket 
  
def Main(): 
    # local host IP '127.0.0.1' 
    host = '127.0.0.1'
    # Define the port on which you want to connect 
    port = 12345
  
    c = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
  
    # connect to server on local computer 
    c.connect((host,port)) 
  
    # message you send to server 
    message = input('Enter host name')
    c.send(message.encode('ascii')) 
    data1 = c.recv(10)
    strings=str(data1,'utf8')
    filesize=int(strings)
    message =" filesize Received "
    c.send(message.encode('ascii')) 
    while True:
        j=c.recv(5) #FileNumber 
        if not j : 
            break
        strings2=str(j,'utf8')
        file_num=int(strings2)
        message =" fileNumber Received "
        c.send(message.encode('ascii')) 
        data=c.recv(filesize) #data
        if not data : 
            break
        if len(data)==0:
            break
        with open('DataHost2/received_file'+str(file_num), 'wb') as f:
            print('data=%s', (data))
            f.write(data)
        f.close()
    print('Received from the server :') 
        

    c.close() 
  
if __name__ == '__main__': 
    Main() 