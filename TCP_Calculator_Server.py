from socket import *

s = socket(AF_INET,SOCK_STREAM)

s.bind(("",8000))

s.listen(5)

c,a = s.accept()

print("Received connection from", a)

while True:

   n1=c.recv(100).decode()

   n2=c.recv(100).decode()

   op=c.recv(100).decode()

   res = None

   if(op=='+'):

       res = int(n1)+int(n2)

   elif(op=='-'):

       res = int(n1)-int(n2)

   elif(op=='*'):

       res = int(n1)*int(n2)

   elif(op=='/'):

       if(n2=='0'):

           res = 'Division by zero is not possible'

       else:

           res = int(n1)/int(n2)

   else:

       print("Invalid operand")

       break

   print("Result : ",res)

     
c.close()
s.close()
