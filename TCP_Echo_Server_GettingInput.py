from socket import *

s = socket(AF_INET,SOCK_STREAM)

s.bind(("",8000))

s.listen(5)

c,a = s.accept()

print("Received connection from", a)

while True:
  
  data=c.recv(100).decode()

  if (data=='Bye' or data=='bye'):

      print(data)

      break

  print(data)

c.close()
