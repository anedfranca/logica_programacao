metros = float (input ("digite o numero em metros que deseja converter em cm: "))
cm = metros*100
print  (metros," em centimetro é: " ,cm)

#converter graus celsius em F
c = float (input ("digite um valor em graus Celsius: "))
f = (c*9/5)+ 32
print (c, "em fahrenheit é: " ,f)

genero = input ("digite seu genero [m- masculino] [f- feminino]: ")
h = float (input("digite sua altura: ")) 

if (genero == "m" or genero == "M"):
    peso = (72.7*h)-58
    g = "masculino"

elif (genero == "f" or genero == "F"):
    peso = (62.1*h)-44.7
    g = "feminino"

print(f"uma pessoa do genero {g} com altura de {h} metros precisa ter como peso ideal: {peso:.2f}")


''' == IGUAL. verifica se um valo é gual o outro (5 == 5) \\false
 != DIFERENTE DE. verifica se o valor é diferente do outro (5 != 5) \\ false
 > MAIOR (5 > 4) \\ false
 < MENOR (5 < 6) \\ true
 >= MAIOR IGUAL (5 >= 5) \\ true
 <= MENOR IGUAL (6 <= 5) \\ false
 + SOMA
 - SUBTRACAO 
 % MODULO
 ** EXPONENCIÇAO
 * MULTIPLICAÇÂO
 \n QUEBRA DE LINHA '''


#calcular area do quadrado
l = float (input ("digite o valor do lado do quadrado: "))
area = l**2
print (f"a area do quadrado é {area}")
dobro = area*2
print (f"o dobro da area do quadrao é {dobro}")


hora = int (input ("Digite quanto voce ganha por hora: "))
mes = int (input ("Digite o numero de horas trabalhadas no mês: "))
total = hora*mes
print (f"seu salario referido no mes {total}")


#mostre o maior entre dois numeros
n1 = int (input ("digite um numero: "))
n2 = int (input ("digite outro numero: "))

if (n1>n2):
    print (f"maior {n1}")

else:
    print (f"o maior é {n2}")

num = int (input ("Digite um valor: "))

if (num<0):
    print (f"{num} é negativo")

elif (num>0):
    print (f"{num} é positivo")


#peça as duas notas e calcule a media
nota1 = float (input ("Digite sua priemra nota: "))
nota2 = float (input ("Digite sua 2 nota: "))

media = (nota1 + nota2)/2

if (media==10):
    print ("Aprovado com distinção")

elif (media>=7):
    print ("Aprovado")

elif (media<7):
    print ("Reprovado")

n1 = int (input ("Digite um numero:"))
n2 = int (input ("Digite outro numero:"))
n3 = int (input ("Digite o ultimo numero: "))