"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.


num = input('Digite um número: ')

try:
    num_int = int(num)
    if num_int % 2 == 0:
        print(f'O número {num_int} é par.')
    else:
        print(f'O número {num_int} é ímpar.')
except:
    print('Você não digitou um número inteiro.')


Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.


hora = input('Quantas horas? ')

try:
    hora_float = int(hora)
    if hora_float >= 0 and hora_float <= 11:
        print('Bom dia!')
    elif hora_float >= 12 and hora_float <= 17:
        print('Boa tarde!')
    elif hora_float >= 18 and hora_float <= 23:
        print('Boa noite!')
    else:
        print("não conheço essa hora.")
except:
    print("Digite apenas números")


Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome = input('digite seu nome: ')
tam_nome = len(nome)

try:
    if tam_nome <= 4:
        print('Seu nome é pequeno.')
    elif tam_nome >= 5 and tam_nome <= 6:
        print('Seu nome é normal.')
    elif tam_nome >= 7:
        print('Seu nome é grande.')
except:
    print('Algo de errado não está certo.')