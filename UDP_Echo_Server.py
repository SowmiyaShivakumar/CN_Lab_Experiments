import socket

server_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

server_socket.bind(('', 12000))

while True:

  message, address =server_socket.recvfrom(1024)

  print("Received connection from ",address)

  message = message.decode()

  server_socket.sendto(message.encode('utf-8'),address)

  break

server_socket.close()
