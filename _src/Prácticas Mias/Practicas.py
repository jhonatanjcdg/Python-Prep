print("Digite el primer número")
n1 = input("Digite el primer número: ")
print("Digite el segundo número")
n2 = input
print("Digite la operación que desea realizar:(+,-,*,/)")
op = input
result = 0
signo = ""
if(op == '+'):
    signo = '+'
    result = n1+n2
elif(op == '-'):
    signo = '-'
    result = n1-n2
elif(op == '*'):
    signo = '*'
    result = n1*n2
elif(op == '/'):
    signo = '/'
    result = n1/n2
else:
    print("No digitó ninguno de los signos propuestos")
    SystemExit
print("El resultado de",n1,signo,n2,'es:',result)