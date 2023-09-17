num= int (input ('Digite um numero: '))

if (num % 2 == 0):
    print('Numero par')

else:
    print ('Numero impar')

'''testando tabela verdade'''
num= int (input ('Digite um numero: '))

if (num % 2 == 0 and num == 10):
    print('Numero par')
elif num != 10:
    print ('Numero diferente de 10')
else:
    print ('Numero impar')

'''operadores logicos
not/or/and '''

#match case
user= input ('Digite seu usuario: ')
password = input ('Senha: ')
match (user == 'Ane' and password == '123'):

    case True:
        print ('Acesso permitido!')
    case False:
        print ('Acesso negado!')

'''LISTA DE EXERCICIO'''
'''FAÇA UM PROGRAMA QUE PEÇA DOIS NUM E IMPRIMA O MAIOR'''
n1= int (input ('Digite um numero: '))
n2= int (input ('Digite outro numero: '))

if n1>n2:
    print(f"{n1} É maior que {n2}")

else:
    print(f"{n1} É maior que {n2}")

'''2 EXERCICIO'''
num = int (input ("Digite um numero: "))

if num > 0:
    print(f"o numero {num} é positivo")

else:
    print(f"o numero {num} é negativo")

'''3 EXERCICIO'''
genero= input ('Digite F para Feminino ou M para masculino): ').upper()


if genero == 'F':
    print('Feminino')

elif genero == 'M':
    print('Masculino')
else:
    print('Sexo invalido')

'''4 EXERCICIO'''
letra= input ('Digite uma letra: ')

if (letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u'):
    print('Vogal')

else:
    print('Consoante')

'''FORMA LISTA'''
vogais = ['a', 'e', 'i', 'o', 'u' ]

letra= input ('Digite uma letra: ')
if (letra == vogais[0] or letra == vogais[1] or letra == vogais[2] or letra == vogais[3] or letra == vogais[4]):
     print('Vogal')

else:
    print('Consoante')

'''EXERCICIO'''
n1 = int (input ("digite um numero: "))
n2 = int (input ("digite outro numero: "))
n3 = int (input ("digite outro numero: "))

if n1>n2 and n1>n3:
    print (f"o numero {n1} é o maior ")

elif n2>n1 and n2>n3:
    print (f"o numero{n2} é o maior  ")
    
else:
    print (f'O numero {n3} é o maior')