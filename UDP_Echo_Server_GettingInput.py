import socket

server_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

server_socket.bind(('', 12000))

while True:

  message, address = server_socket.recvfrom(1000)

  print("Received connection from ",address)
  
  message = message.decode()

  if(message=='Bye' or message=='bye'):

      print(message)

      break

  print(message)

server_socket.close()
