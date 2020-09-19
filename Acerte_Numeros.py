from random import randint
from time import sleep

def LeiaInt(msg, maxNum, minNum):
    while True:
        num = input(msg)
        try:
            int(num)
        except:
            print('Digite apenas numeros')
        else:
            if not maxNum and not minNum:
                return int(num)
            elif int(num) > maxNum or int(num) < minNum:
                print(f'Digite um numero entre {minNum} e {maxNum}')
                continue
            return int(num)

def Menu(lst):
    for ind, el in enumerate(lst):
        print(f'{ind + 1} - {el}')
    num = LeiaInt('Digite sua opção: ', len(lst), 1)
    return lst[num - 1]

print('''
  ___                     _                           _   _         _              
 / _ \                   | |                         | | | |       | |             
/ /_\ \  ___   ___  _ __ | |_   ___        ___       | | | |  __ _ | |  ___   _ __ 
|  _  | / __| / _ \| '__|| __| / _ \      / _ \      | | | | / _` || | / _ \ | '__|
| | | || (__ |  __/| |   | |_ |  __/     | (_) |     \ \_/ /| (_| || || (_) || |   
\_| |_/ \___| \___||_|    \__| \___|      \___/       \___/  \__,_||_| \___/ |_|   
 ''')
sleep(1)
print('Escolha a Dificuldade: ')
sleep(1)
resp = Menu(['Facil', 'Medio', 'Dificil'])
if resp == 'Facil':
    qtd = (0, 10)
elif resp == 'Medio':
    qtd = (0, 100)
elif resp == 'Dificil':
    qtd = (0, 1000)

num_Sorteado = randint(qtd[0], qtd[1])
string = 'Sorteando Numeros...'
print()
for let in string:
    sleep(0.2)
    print(let, end='', flush=True)
print('\n')
while True:
    resp = LeiaInt(f'\nTente acertar o numero sorteado. Uma dica, ele esta entre {qtd[0]} e {qtd[1]}: \n', False, False)
    if resp == num_Sorteado:
        print('Wow, você acertou, parabens')
        break
    elif resp > num_Sorteado:
        print('Tente chutar um numero mais baixo')
    elif resp < num_Sorteado:
        print('Tente chutar um numero mais alto')

