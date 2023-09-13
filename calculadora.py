X=int(input('digite um numero:'))
Y=int(input('digite um numero:'))

def soma(X,Y):
	    return str(X + Y)
	    
def media(X,Y):
	    return str((X + Y)/2)

def mult(X,Y):
	    return str(X * Y)
	    
def sub(X,Y):
        return str(X - Y)
    
def div(X,Y):   
        return str(X / Y)
        
def div_int(X,Y):
	    return str(X//Y)

def pot_X(X):
	    return str(X**2)
	    
def pot_Y(Y):
	    return str(Y**2)
	    
def pot3_X(X):
	    return str(X**3)
	    	    
def pot3_Y(Y):
	    return str(Y**3)
	    
def raiz_X(X):
	    return str(X**0.5)

def raiz_Y(Y):
	    return str(Y**0.5)
	    
def porc(X,Y):   
        return str(X//100+Y//100)
	    	    	    
   
print('a soma dos numeros é:' + soma(X, Y))
print('a media dos numeros é:' + media(X,Y))
print('a multiplicação dos numeros é:' + mult(X,Y))	    
print('a subtração dos numeros é:' + sub(X,Y))	
print('a divisão dos numeros é:' + div(X,Y))
print('a divisão inteira dos numeros é:' + div_int(X,Y))
print('o primeiro numero elevado ao quadrado é:' + pot_X(X))
print('o segundo numero elevado ao quadrado é:' + pot_Y(Y))
print('o primeiro numero elevado ao cubo é:' + pot3_X(X))
print('o segundo numero elevado ao cubo é:' + pot3_Y(Y))
print('a raiz quadrada do primeiro numero é:' + raiz_X(X))
print('a raiz quadrada do segundo numero é:' + raiz_Y(Y))
print('a porcentagem dos numeros é:' + porc(X, Y))

##################### CALCULO DEFINIDO ######################################

n1 = int(input("digite um número:"))
n2 = int(input("digite um número:"))
operacao = input("digite o calculo que deseja:")

if operacao == 'somar':
 print(f'resultado:{n1 + n2}')
elif operacao == 'dividir':
 print(f'resultado: {n1 // n2}')
elif operacao == 'multiplicar':
 print(f'resultado:{n1 * n2}')
elif operacao == 'subtrair':
 print(f'resultado:{n1 - n2}')
elif operacao == 'exponencial':
 print(f'resultado:{n1 ** n2}')
elif operacao == 'porcentagem':
 print(f'resultado:{n2 * n1/100}')
elif operacao == 'média':
 print(f'resultado:{n1 + n2 /2}')

else:
 print("tipo de calculo ainda não disponivel")
