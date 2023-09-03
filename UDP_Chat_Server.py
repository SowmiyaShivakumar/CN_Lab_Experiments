import socket

server_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

server_socket.bind(('', 12000))

while True:

  message, address = server_socket.recvfrom(1000)
    
  message = message.decode()

  if(message=='Bye' or message=='bye'):

      print(message)

      break

  print("Received message: ",message)

  data = input("Enter a message: ")

  if(data=='Bye' or data=='bye'):

      server_socket.sendto(data.encode('utf-8'),address)

      break

  server_socket.sendto(data.encode('utf-8'),address)

server_socket.close()
