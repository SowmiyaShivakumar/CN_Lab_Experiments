from socket import *

s = socket(AF_INET, SOCK_STREAM)

s.connect(("127.0.0.1",8000)) # Connect

while True:

    data = input("Enter a message: ")

    if(data=='Bye' or data=='bye'):

        s.send(data.encode('utf-8'))

        break

    s.send(data.encode('utf-8')) # Send request

    data = s.recv(100).decode()# Get response

    print("Received message: ",data)

s.close()
