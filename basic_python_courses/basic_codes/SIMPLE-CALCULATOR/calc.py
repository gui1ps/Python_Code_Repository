import math

def somar(val1,val2):
    print(val1,'+',val2,'=',(float(val1)+float(val2)))

def sub(val1,val2):
    print(val1,'-',val2,'=',(float(val1)-float(val2)))

def multiplicar(val1,val2):
    print(val1,'X',val2,'=',(float(val1)*float(val2)))

def dividir(val1,val2):
    print(val1,':',val2,'=',(float(val1)/float(val2)))

def potencia(val1,val2):
    print(val1,'^',val2,'=',(float(val1)**float(val2)))

def media(val1,val2):
    print('media entre',val1,'e',val2,'=',((float(val1)+float(val2))/2))

def quad(val1):
    print('/',val1,'=',(math.sqrt(float(val1))))

def cosn(val1):
    print('cos',val1,'=',(math.cos(float(val1))))

def seno(val1):
    print('sen',val1,'=',(math.sin(float(val1))))

def tang(val1):
    print('tan',val1,'=',(math.tan(float(val1))))



val1=input('Insira o primeiro valor: ')
if val1=='pi':
    val1=math.pi

op=input('''
Operação Símbolo de entrada	Exemplo de saída
adição	           +	         10 + 5 = 15.0
subtração	   -	          10 - 5 = 5.0
multiplicação	   x	         10 x 5 = 50.0
divisão	           :	          10 : 5 = 2.0
potenciação	   ^	        10^5 = 10000.0
média aritmética  media	    media entre 10 e 5 = 7.5 
raiz quadrada	   /	             / 9 = 3.0
cosseno	          cos	           cos 0 = 1.0
seno	          sen	           sen 0 = 0.0
tangente	  tan	           tan 0 = 0.0

Operação que você deseja realizar: ''')

if op=='+':
    val2=input('Insira o segundo valor: ')
    somar(val1,val2)
elif op=='-':
    val2=input('Insira o segundo valor: ')
    sub(val1,val2)
elif op=='X' or op=='x':
    val2=input('Insira o segundo valor: ')
    multiplicar(val1,val2)
elif op==':':
    val2=input('Insira o segundo valor: ')
    dividir(val1,val2)
elif op=='^':
    val2=input('Insira o segundo valor: ')
    potencia(val1,val2)
elif op=='media':
    val2=input('Insira o segundo valor: ')
    media(val1,val2)
elif op=='/':
    quad(val1)
elif op=='cos':
    cosn(val1)
elif op=='sen':
    seno(val1)
elif op=='tan':
    tang(val1)
