from socket import *

s = socket(AF_INET,SOCK_STREAM)

s.bind(("",8000))

s.listen(5)

c,a = s.accept()

print("Received connection from", a)

while True: 

   data=c.recv(100).decode()

   print("Received message: ",data)

   if(data=='Bye' or data=='bye'):

       break

   msg = input("Enter a message: ")

   if(msg=='Bye' or msg=='bye'):

        c.send(msg.encode('utf-8'))

   c.send(msg.encode('utf-8'))

c.close()
