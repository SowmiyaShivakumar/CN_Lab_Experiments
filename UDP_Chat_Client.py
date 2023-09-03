import socket

client_socket =socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

addr = ("127.0.0.1", 12000)

while True:

    message = input("Enter a message: ")

    client_socket.sendto(message.encode('utf-8'), addr)

    if(message=='Bye' or message=='bye'):

        break

    data ,addr= client_socket.recvfrom(1000)

    data = data.decode()

    if(data=='Bye' or data=='bye'):

         print("Received message:",data)

         break

    print("Received message:",data)

client_socket.close()
