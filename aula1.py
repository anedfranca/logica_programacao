#calculadora
n1= int (input ("Digite um numero: "))
n2= int (input ("Digite outro numero: "))

operacao= int (input ('''Selecione a operação:
                    1- SOMA
                    2- SUBTRACAO
                    3- DIVISAO
                    4-MULTIPLICACAO:  '''))


if (operacao == 1):
    print (n1+n2)

elif (operacao == 2):
    print (n1-n2)

elif (operacao == 3):
    print (n1/n2)

elif (operacao == 4):
    print (n1*n2)



''' faça um programa que verifique a idade de uma pessoa 
e determine a sua faixa etaria'''

idade= int (input ('Digite sua idade: '))

if (idade<=0.6):
    print ('Recém-nascido')
    
elif (idade>=0.6 and idade<=1):
    print ('Bebê')

elif (idade>=1 and idade<=10):
    print ('criança')
    
elif (idade>10 and idade<=14):
    print ('Pré-adolescente')

elif (idade>14 and idade<=18):
    print ('Adolescente')

elif (idade>18 and idade<=60):
    print ('Adulto')

''' // DIVISÃO INTEIRA
 != DIFERENTE/NEGAÇÃO'''


'''carteira de habilitacao
A- MOTO
B- CARRO
AB- CARRO E MOTO
C- VEICULOS PESADOS
D- VEICULOS ARTICULADOS'''

categoria = input ("Digite sua categoria de habilitação: ")

if (categoria == 'A'):
    print ('Você está habilitado a pilotar somente motos!')

elif (categoria == 'B'):
    print ('Você está habiitado a dirigir somente carros!')

elif (categoria == 'AB'):
    print ('Você está habiitado a pilotar motos e dirigir carros!')

elif (categoria == 'C'):
    print ("Você está habilitado a dirigir veiculos pesados e carros!")

elif (categoria == 'D'):
    print ('Você está habilitado  dirigir veiculos articulados e carros!')

''' AND- E
OR- OU '''