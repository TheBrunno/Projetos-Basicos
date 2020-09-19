from random import randint
from time import sleep


def leiaInt(msg):
    while True:
        val = input(msg)
        try:
            int(val)
        except:
            print('Digite apenas numeros')
            continue
        else:
            return int(val)


print('''
 _____  _                    _             _                     _           ______             _             
/  ___|(_)                  | |           | |                   | |          |  _  \           | |            
\ `--.  _  _ __ ___   _   _ | |  __ _   __| |  ___   _ __     __| |  ___     | | | |  __ _   __| |  ___   
 `--. \| || '_ ` _ \ | | | || | / _` | / _` | / _ \ | '__|   / _` | / _ \    | | | | / _` | / _` | / _ \ 
/\__/ /| || | | | | || |_| || || (_| || (_| || (_) || |     | (_| ||  __/    | |/ / | (_| || (_| || (_) | 
\____/ |_||_| |_| |_| \__,_||_| \__,_| \__,_| \___/ |_|      \__,_| \___|    |___/   \__,_| \__,_| \___/ 
''')
sleep(2)
qtd = leiaInt('Quer simular quantos dados: ')
for c in range(0, qtd):
    sleep(0.2)
    print(f'{c + 1}º Dado - {randint(1, 6)}')
