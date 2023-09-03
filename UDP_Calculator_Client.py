import socket

client_socket =socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

addr = ("127.0.0.1", 12000)

while True:

    n1 = input("Enter input1: ")

    n2 = input("Enter input2: ")

    op = input("Enter operator: ")

    client_socket.sendto(n1.encode('utf-8'), addr)

    client_socket.sendto(n2.encode('utf-8'), addr)

    client_socket.sendto(op.encode('utf-8'), addr)

    if op not in ('+','-','*','/'):

        break
    
client_socket.close()
