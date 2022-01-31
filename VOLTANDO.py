"""pes=float(input("Digite quando Pes:"))
polegadas= pes*12
jardas= pes*3
milhas=pes*1760
print(f"Polegas:{polegadas}"
      f"jardas:{jardas}"
      f"milhas:{milhas}",
      )"""
import math
"""area=int(input("Qual o tamanha em metros quadrados:"))
litros=area/3
capacidade= 18
preco= 80
lata= (litros/capacidade)
capacidade_galo=3.6
preco_galo= 25
galão=litros/capacidade_galo
total_galo= galão*preco_galo
total=lata*preco"""
import math

"""def contabilidade(salario_bruto,salario_liquido,descontos):
    ganha=float(input("Quanto vc ganha por hora:"))
    tempo=float(input("horas trabalhadas no mês:"))
    salario=ganha*tempo
    inss= salario*(8/100)
    ir= salario*(11/100)
    sindicato=salario*(5/100)
    descontos=(inss+ir+sindicato)
    salario_liquido=salario-descontos
    print(f"O seu salario Bruto é R${salario:.0f}")
    print(f"O seu salario teve desconto de R${inss} do inss")
    print(f"O seu salario teve desconto de R${ir} do ir")
    print(f"Pagou R${sindicato} ao sindicato ")
    print(f"O seu salario liquido foi de R${salario_liquido}")"""

"""num_1=int(input("Digite um numero:"))
num_2=int(input("Digite outro numero:"))
maior=0
if num_2>num_1:
    maior=num_2
elif num_1>num_2:
    maior=num_1
print(f"O numero maior é{maior}")"""

"""letra=str(input("Digite um letra:"))
vogal="a" and "e" and "i"
if letra == vogal:
    print("A letra digitada é uma v")
else:
    print("A letra é uma c")"""

"""sexo=str(input("Digite seu sexo:")).upper().strip()
while sexo not in "MmFf":
    sexo=input("Dado invalido!!!! Digite seu sexo:").upper().strip()
print(f"Sexo {sexo} registrado com sucesso")"""


"""media=0
cont=0
soma=0
while True:
    num_1=int(input("Digite a nota do aluno:"))
    cont += 1
    p=str(input("Quer continuar? [S/N]")).upper().strip()[0]
    media += num_1 + num_1 / cont
    soma+=num_1
    while p not in "SN":
        p=str(input("Dado invalido!!!Quer continuar? [S/N]")).upper().strip()[0]
    if p == "N":
        break
media = soma / cont
if media <=5:
    print(f"A nota media do aluno foi {media} (REPROVADO)")
elif media >= 5 and  media <=8:
    print(f"A nota media do aluno foi {media} (APROVADO)")
elif media >= 9:
    print(f"A nota media do aluno foi {media} (APROVADO COM HONRA) ")"""

"""opcao=0
kg=0
pagamento=0
F=0
p=0
t=0
while opcao != 4  :
    print('''    [1]File duplo
    [2]Alcatra
    [3]Picanha''')
    opcao=int(input("Qual a sua opção:"))
    print()
    kg=float(input("Quantos kg de carne?"))
    if opcao == 1:
        opcao="File duplo"
        if  kg <=5:
            F=4.90*kg
        elif kg >=6:
            F=5.80*kg
    if opcao == 2:
        opcao="Alcatra"
        if kg <= 5:
            F = 5.90 * kg
        elif kg >= 6:
            F = 6.80 * kg
    if opcao == 3:
        opcao="Picanha "
        if  kg <=5:
            F=6.90*kg
        elif kg >=6:
            F=7.80*kg
    print('''  [1] Cartão
    [2] Dinheiro 
    [3] Pix
    [4] Sair''')
    pagamento=int(input("Qual a forma de pagamento:"))
    if pagamento == 1:
        pagamento="cartão"
    if pagamento == 2:
        pagamento = "Dinheiro"
        p= (F*5/100)
    if pagamento == 3:
        pagamento="Pix"
    t=F-p
    if opcao != 4:
        break

print(f"{'-'*15} NOTA FISCAL {'-'*15}")
print(f"Carne..........................{opcao}")
print(f"Quantidade.....................{kg}kg")
print(f"Preço..........................R${F}")
print(f"Desconto.......................R${p:.2f}")
print(f"Forma de pagamento.............{pagamento}")
print(f"Total a pagar..................R${t:.2f}")"""

"""class Pessoa:
    def __init__(self, nome:str, idade:int, altura:float):
        self.nome=nome
        self.idade=idade
        self.altura=altura
    def dizer_ola(self):
        print(f'Ola, meu nome é {self.nome} muito prazer. tenho {self.idade} anos '
              f'e {self.altura} de altura')
    def cozinha(self, alimento: str):
        print(f'Hoje vamos cozinhar {alimento}')
    def andar(self, metros: float):
        print(f'Vou andar ate dar {metros} metros ')


pessoa=Pessoa(nome="Daniel",idade= 17, altura= 1.89)
pessoa.dizer_ola()
pessoa.andar(350)
pessoa.cozinha('Arroz')"""

"""def sequencia(n):
    for i in range(n):
        i+=1
        print(str(i)*i)

num=int(input("Digite um numero:"))
sequencia(num)"""

"""def inteiro (num:str):
    print( f'Voce digitou {len(num)} digitos')
digito=str(input("Digite um numero inteiro:"))
inteiro(digito)"""

'''def reverso(num:str):
    print(f'O numero ao contrario é {num[::-1]}')
n=input('Digite um numero:')
reverso(n)'''

from time import sleep
from random import randint
sleep(0.5)
print(f'{"-="*8}CAPS{"-="*8}')
jogos=[]
p=0
p1=0
def caps(num:int):

    sleep(0.5)
    print(f'''Resultado...
{num}''')
    sleep(1)
    while True:
        if num == 7 or num == 11:
            print("PARABENS!!!!!VOCÊ GANHOU PONTOS DUPLOS")
            p=2
            jogos.append(p)

        elif num == 2 or num==3 or num==12:
            print("INFELIZMENTE VOCE PERDEU ")

        elif num == 4 or num == 5 or num == 6 or num == 8 or num == 9 or num == 10:
            print('VOCÊ GANHOU UM PONTO')
            p1=1
            jogos.append(p1)
        print(f"{'-=-'*16}")
        break

while True:
    jogada = input("Quer jogar caps?(S/N) ").upper()
    if jogada == "S":
        jogos.append(caps(randint(2,12)))
    while jogada not in "SN":
        jogada=input("DADO INVALIDO!!!!Quer jogar caps?(S/N)")
    if jogada == "N":
        print("OBRIGADO POR JOGAR!!!")
        break


























