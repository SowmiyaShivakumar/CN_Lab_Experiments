import socket

server_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

server_socket.bind(('', 12000))

while True:

  n1, address = server_socket.recvfrom(1000)
    
  n1 = n1.decode()

  n2, address = server_socket.recvfrom(1000)
    
  n2 = n2.decode()

  op, address = server_socket.recvfrom(1000)
    
  op = op.decode()

  res = None
  
  if op=='+':

      res=int(n1)+int(n2)

  elif op=='-':

      res=int(n1)-int(n2)

  elif op=='*':

      res=int(n1)*int(n2)

  elif op=='/':

      if(n2=='0'):

          res='Division by zero is not possible'

      else:

          res=int(n1)/int(n2)

  else:

      print("Invalid Operator")

      break

  print("Result: ",res)

server_socket.close()
