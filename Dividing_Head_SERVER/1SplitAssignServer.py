import socket  
# import thread module 
from _thread import *
import threading 
import os
import shutil
#x=1

x=1

def split_file():
    global x
    with open("InputFile/text.txt", "r", encoding="utf8") as in_file:
        bytes = in_file.read(50)
        while bytes:
            with open("Packets/data" + str(x)+".txt", 'w', encoding="utf8") as output:
                output.write(bytes)
            bytes = in_file.read(50)
            x += 1
    print("file split operation has been sucessfull")
print_lock = threading.Lock() 
  
# thread function 
def threaded(c): 
    global x
    outputBase = 'Packets/data'
    while True: 
  
        # data received from client 
        data = c.recv(1024) 
        data= data.decode()
        if not data: 
            print('Bye') 
              
            # lock released on exit 
            print_lock.release() 
            break
       
        if(data=="host1"or data=="Host1"or data== "HOST1" or data=="host 1" or data=="Host 1" or data=="HOST 1"):
            w=os.path.getsize(outputBase+str(1)+'.txt')
            print(str(w))
            c.send(bytes(str(w),'utf8'))
            data = c.recv(1024) 
            data= data.decode()
            print("Client's data=")
            print(data)
            x1=x
            if x%2==0:
                x1=x
            else:
                x1+=1
            for y in range(1,x1,2):
                c.send(bytes(str(y),'utf8'))
                data = c.recv(1024) 
                data= data.decode()
                print("Client's data=")
                print(data)
                with open(outputBase+str(y)+'.txt','rb') as f:
                    l = f.read(w)
                    c.send(l)
                    print('file'+str(y))
                    print('data=%s', (l))
                    f.close()

            print('Done sending to host1')

        elif(data=="host2"or data=="Host2"or data=="HOST2" or data=="host 2" or data=="Host 2" or data=="HOST 2"):
            w=os.path.getsize(outputBase+str(1)+'.txt')
            print(str(w))
            c.send(bytes(str(w),'utf8'))
            data = c.recv(1024) 
            data= data.decode()
            print("Client's data=")
            print(data)
            x2=x
            if x%2==0:
                x2+=1
            else:
                x2=x
            for y in range(2,x2,2):
                c.send(bytes(str(y),'utf8'))
                data = c.recv(1024) 
                data= data.decode()
                print("Client's data=")
                print(data)
                with open(outputBase+str(y)+'.txt','rb') as f:
                    l = f.read(w)
                    c.send(l)
                    print('file'+str(y))
                    print('data=%s', (l))
                    f.close()

            print('Done sending to host2')

        elif(data=="host3"or data=="Host3"or data=="HOST3" or data=="host 3" or data=="Host 3" or data=="HOST 3"):
            w=os.path.getsize(outputBase+str(1)+'.txt')
            print(str(w))
            c.send(bytes(str(w),'utf8'))
            data = c.recv(1024) 
            data= data.decode()
            print("Client's data=")
            print(data)
            x3=x
            if x%2==0:
                x3=x
            else:
                x3+=1
            for y in range(1,x3,2):
                c.send(bytes(str(y),'utf8'))
                data = c.recv(1024) 
                data= data.decode()
                print("Client's data=")
                print(data)
                with open(outputBase+str(y)+'.txt','rb') as f:
                    l = f.read(w)
                    c.send(l)
                    print('file'+str(y))
                    print('data=%s', (l))
                    f.close()

            print('Done sending to host3')

        elif(data=="host4"or data=="Host4"or data=="HOST4" or data=="host 4" or data=="Host 4" or data=="HOST 4"):
            w=os.path.getsize(outputBase+str(1)+'.txt')
            print(str(w))
            c.send(bytes(str(w),'utf8'))
            data = c.recv(1024) 
            data= data.decode()
            print("Client's data=")
            print(data)
            x4=x
            if x%2==0:
                x4+=1
            else:
                x4=x
            for y in range(2,x4,2):
                c.send(bytes(str(y),'utf8'))
                data = c.recv(1024) 
                data= data.decode()
                print("Client's data=")
                print(data)
                with open(outputBase+str(y)+'.txt','rb') as f:
                    l = f.read(w)
                    c.send(l)
                    print('file'+str(y))
                    print('data=%s', (l))
                    f.close()

            print('Done sending to host4')
        # lock released on exit 
        print_lock.release() 
        break;
    # connection closed 
    c.close()
    return

  
def Main(): 
    split_file()
    global x
    x-=1
    host = "" 
  
    port = 12345
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    s.bind((host, port)) 
    print("socket binded to port", port) 
  
    # put the socket into listening mode 
    s.listen(5) 
    print("socket is listening") 
  
    # a forever loop until client wants to exit 
    while True: 
  
        # establish connection with client 
        c, addr = s.accept() 
  
        # lock acquired by client 
        print_lock.acquire() 
        print('Connected to :', addr[0], ':', addr[1]) 
  
        # Start a new thread and return its identifier 
        start_new_thread(threaded, (c,)) 
    s.close() 
  
  
if __name__ == '__main__': 
    Main() 










    