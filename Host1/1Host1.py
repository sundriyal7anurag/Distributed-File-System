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
    j=1
    data1 = c.recv(10)
    strings=str(data1,'utf8')
    filesize=int(strings)
    print("Server's data=%s", (data1))
    message =" filesize Received "
    c.send(message.encode('ascii')) 
    
    while True:
        
        j=c.recv(5)# file number 
        if not j : 
            break
        strings2=str(j,'utf8')
        file_num=int(strings2)
        message =" filesNumber Received "
        c.send(message.encode('ascii')) 
        data=c.recv(filesize)
        print("server's data=")
        print(data)
        if not data : 
            print("tshooting"+"8")
            break
        print("tshooting"+"9")
        print(len(data))
        if len(data)==0:
            break
        print("tshooting"+"10")
        with open('DataHost1/received_file'+str(file_num), 'wb') as f:
            print("File's data=%s", (data))
            f.write(data)
        f.close()
    print('Received from the server :') 
    #break
        

    c.close() 
  
if __name__ == '__main__': 
    Main() 