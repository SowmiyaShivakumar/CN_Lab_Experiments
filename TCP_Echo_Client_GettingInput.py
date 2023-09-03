from socket import *

s = socket(AF_INET, SOCK_STREAM)

s.connect(("127.0.0.1",8000)) # Connect

while True:

    op = input("Enter a string:")
    
    s.send(op.encode('utf-8')) # Send request

    if (op=='Bye' or op=='bye'):

        break
    
    #data = s.recv(100).decode()# Get response

s.close()
