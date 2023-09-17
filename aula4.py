'''LISTA'''
carros = ['celta', 'uno', 'Marea Turbo', 'Gol bola batido']

for contador in range(0,4):
    print(carros[contador])


'''LOGIN E SENHA'''
op = ''


while op != 'sair':
    print('''
        opção 1: login
        opção 2: mudar senha
        
        digite sair para sair
    
    
    ''')

    op= int(input('Digite uma opção: '))

    if op == 1:
        login= input('Digite seu login: ')
    elif op == 2:
        senha= input('Digite sua senha atual: ')
        novasenha= input('Digite sua nova senha: ')
        novasenha= input('Confirme sua nova senha: ')



'''CALCULADORA'''
while True:
    print('''
          CALCULADORA 1.0
          
          Selecione a operação desejada
          
          1: Adição
          2:Subtração
          3:Multiplicação
          4:Divisão


          0: Sair
'''  )
    
    op= int(input('Operação: '))

    match op: 
        case 1: 
            num1 = int(input('Digite um numero: '))
            num2 = int(input('Digite outro numero: '))
            soma= num1 + num2

            print(f'A soma de {num1} e {num2} é {soma}')
        case 2:
            num1 = int(input('Digite um numero: '))
            num2 = int(input('Digite outro numero: '))
            subtração= num1 - num2

            print(f'A subtração de {num1} e {num2} é {subtração}')

        case 3: 
            num1 = int(input('Digite um numero: '))
            num2 = int(input('Digite outro numero: '))
            multiplicação = num1 * num2

            print(f'A subtração de {num1} e {num2} é {multiplicação}')

        case 4:
            num1 = int(input('Digite um numero: '))
            num2 = int(input('Digite outro numero: '))
            divisão = num1//num2

            print(f'A subtração de {num1} e {num2} é {divisão}')

        case 0:
            break




'''peça uma nota de 0 a 10. mostre uma mensagem caso o valor seja inválido e continue pedindo
ate que o usuaro mostre um valor valido'''

while True:
    nota= int(input('Digite uma nota: '))
    if nota >=0 and nota <=10:
        print('Valor válido!')
        break
    else:
        print('Valor inválido!')


''' Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha
igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as
informações.'''

while True:
    user= input('Digite seu usuário: ')
    senha= input('Digite sua senha: ')

    if user == senha:
        print('As credenciais não podem ser idênticas!!!')
    else:
        print('Acesso permitido!')
        break


'''Faça um programa que leia e valide as seguintes informações:
Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd';


len()

'''


while True:

    nome= input('Digite seu nome: ')
    if len(nome) <=3:
        print('O nome precisa ter mais que 3 caracteres')
        continue

    idade= int(input('Digite sua idade: '))
    if idade < 0 or idade > 150:
        print('A idade precisa ser maior que 0 e menor que 150')
        continue
    salario= float(input('Digite seu salário: '))
    if salario <=0:
        print('O salário precisa ser maior que 0')
        continue
    '''sexo= input('Digite seu sexo F/M: ').upper()

    if sexo != 'F' or sexo != 'M':
        print('Opção inválida! \nDigite F para feminino ou M para masculino')
    '''
    estadoCivil= input('''Selecione um estado cívil
                        s- solteiro(a)
                        c- casado(a)
                        v- viúvo(a)
                        d- divorciado(a)
        ''')
    
    match estadoCivil:

        case 's':
            print('Solteiro(a)')
            break
        case 'c':
            print('Casado(a)')
            break
        
        case 'v':
            print('Víuvo(a)')
            break
        
        case 'd':
            print('Divorciado(a)')
            break
    
    if estadoCivil != 's' or estadoCivil != 'c' or estadoCivil != 'v' or estadoCivil != 'd':
        print('Estado cívil inválido!')