# Operadores in e not in
# Strings são iteráveis
#  0 1 2 3 4 5 6 7 8
#  G u i l h e r m e
# -9-8-7-6-5-4-3-2-1
# nome = 'Guilherme'
# print(nome[2])
# print(nome[-4])
# print('lher' in nome)
# print('zero' in nome)
# print(10 * '-')
# print('lher' not in nome)
# print('zero' not in nome)

nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')