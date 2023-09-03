from socket import *

s = socket(AF_INET, SOCK_STREAM)

s.connect(("127.0.0.1",8000)) 

while True:

    n1 = input("Enter input1: ")

    n2 = input("Enter input2: ")

    op = input("Enter the operator: ")

    if op not in ('+','-','*','/'):

        break

    s.send(str(n1).encode('utf-8')) 

    s.send(str(n2).encode('utf-8'))

    s.send(op.encode('utf-8'))

s.close()
