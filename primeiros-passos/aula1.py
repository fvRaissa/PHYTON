print ('Hello world')

#Python é igual php, ele mesmo defn o tipo da linguagem
#DECLARANDO VARIAVEL
idade =15
nome = 'Jassinto Dores'
print ('A sua idade', nome, 'eh')
print (idade)

#INPUT E OPERAÇÃO
num = input ('Digite um valor')
num2 = input ('Digite outro valor')

result =int(num)+int(num2)
print (result)

#IF ELSE
idade = 11

if idade < 25:
  print('Vc é jovem ainda mas amanhã velho será')
else:
  print ('O amanhã chegou')


##EXERCICIOS 

#1)Faça um programa que leia um número digitado pelo usuário e apresente o seu sucessor
# e seu antecessor.

num = input('Digite um numero ')
print ('antecessor', int(num)-1)
print ('Suscessor', int(num)+1)


#2)Desenvolva um programa que leia três notas de um aluno e calcule a sua média 
# aritmética.

i = 1

n1 = input('Digite a primeira nota')
n2 = input('Digite a segunda nota ')
n3 = input('Digite a terceira nota ')

print ('A sua média das nota é:', (float(n1)+float(n2)+float(n3))/3)


#3)Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário,
# com 15% de aumento.

salario = input('Digite seu salario')

print('Seu novo salario será: ', int(salario)+int(salario)/100*15)


#4)Faça um programa que leia a largura e a altura de uma parede em Metro, calcule
# a sua área e 
# a quantidade de tinta necessária para pintá-la, sabendo que cada lata de tinta pinta
# uma área de 2m². 

altura = input('Digite a altura')
largura = input('Digite a largura')

print('A quantidades de latas a serem utilizadas é: ', float(altura)*float(largura)/2)


#5)Escreva um programa que faça o computador "Pensar" em um número inteiro entre 0 e 10 
# e solicite para o usuário tentar adivinhar qual foi o número escolhido pelo computador.

import random
num = random.randrange(0,10)
adivinha = int(input('Tente adivinhar um numero de 0 a 10 '))

if(adivinha == num):
  print('Para a bens você adivinhou')
else:
  print('Você não adivinhou, o numero era: ',num)


#6)Crie um programa que realize o jogo de par ou ímpar.  
# Onde o usuário tem a opção de escolher primeiro (Par ou Ímpar), em seguida o usuário
# digita um número o computador randomiza outro número e a soma dos dois revelara o 
#resultado e consequentemente o vencedor. 

import random
num = random.randrange(10)
pi = input('par ou impar? ')
numU = int(input('digite um numero ' ))

resul = (int(num)+int(numU)) % 2

if (resul == 0):
  result = 'par'
  print("Maquina: ",num)
  print("Você: ",numU)
  print(result)
else:
  result = 'impar'
  print("Maquina: ",num)
  print("Você: ",numU)
  print(result)

if (pi == result):
  print('Você ganhou')
else:
  print('Você perdeu')
