usuarios = ['root','ane','luisa']

senhas =        {0:'amarelo',
                 1:'rosa',
                 2:'azul',
                }


user= input('Digite seu usuário: ')
password= input('Digite sua senha: ')

for usuario in usuarios:
     if user == usuario:
         user= True
        

for senha in senhas:
     if senhas[senha] == password:
         password = True


if user == True and password == True:
     print('Acesso permitido!')
else:
     print('Acesso Negado!')

'''se o aluno tirar de 7 a 9, aprovado.
se o aluno tirar menos que 7, reprovado.
se o aluno tira 10, aprovado '''

total = 0
for notas in range (3):
     nota = float(input('digite sua nota: '))
     total = nota + total
     media = total/3
if media < 7:
    print ('reprovado')
elif media >=7 and media <10:
    print('aprovado')
else:
    print('aprovado!')


'''2. Faça um programa para imprimir os números pares de 1 a 20. Utilize a
função range() para criar a coleção de números.'''

for numero in range (1,21):
    if numero %2 == 0:
        print(numero)

'''3. Faça um programa para imprimir os números ímpares de 1 a 19. Utilize a
função range() para criar a coleção de números.'''   

for numero in range (1,20,2):
    print(numero)

'''4. Faça um programa para calcular a soma dos números de 1 a 100. Utilize a
função range() para criar a coleção de números.'''

n1 = 0

for numero in range (1,101):
    n1 = numero + n1
    print(n1)

'''5. Faça um programa para calcular a média de uma lista de números.'''


notas = [90,8,67,73]
media = 0
for nota in notas:
    media = media+nota
    print(media/4)

'''6. Faça um programa para verificar se um número é primo. Utilize a
condicional IF dentro do laço FOR.'''