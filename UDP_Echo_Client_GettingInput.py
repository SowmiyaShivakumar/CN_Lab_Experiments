import socket

client_socket =socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

addr = ("127.0.0.1", 12000)

while True:

    message = input("Enter a string: ")

    client_socket.sendto(message.encode('utf-8'), addr)

    if(message=='Bye' or message=='bye'):

        break

client_socket.close()
