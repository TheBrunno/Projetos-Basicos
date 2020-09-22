import PySimpleGUI as sg
from random import randint
from time import sleep

class Interfaces:
    def __init__(self, Theme='Reddit'):
        self.theme = Theme
        sg.theme(self.theme)

    def Simulador_De_Dados(self):
        layout = [
            [sg.Text('Quantos dados quer simular?:'), sg.Input(size=(10, 1), key='Input')],
            [sg.Button('OK!', size=(5, 1)), sg.Text('Tempo de espera:', size=(15, 1)), sg.InputText(0, size=(5, 1), key='InputTime'),sg.Text('Max: 1s')],
            [sg.Output(size=(38, 10))]
        ]
        janela = sg.Window('Simulador De Dados', layout)
        while True:
            event, values = janela.read()
            if event == sg.WIN_CLOSED:
                break
            if event == 'OK!':
                self.input = values['Input']
                try:
                    int(self.input)
                    float(values['InputTime'])
                except:
                    if self.input == '' or values['InputTime'] == '':
                        print('Digite a quantidade no campo acima')
                        continue
                    print('Digite apenas numeros')
                else:
                    if float(values['InputTime']) > 1:
                        print('O Tempo de espera maximo é 1s')
                        continue
                    numbers = []
                    for c in range(int(self.input)):
                        number_Sorted = randint(1, 6)
                        sleep(float(values['InputTime']))
                        print(f'{c + 1}º Dado - {number_Sorted}')
                        numbers.append(number_Sorted)
                    print('-=' * 10)
                    print('QUANTIDADES')
                    for c in range(6):
                        qtd = numbers.count(c+1)
                        print(f'{c+1}:{qtd}')
                    print('-=' * 10)
    
    def Acerte_O_Numero(self):
        layout = [
            [sg.Text('Escolha a dificuldade: ')],
            [sg.Radio('Fácil', 'dificuldade', key='facil'), sg.Radio('Médio', 'dificuldade', key='medio'), sg.Radio('Difícil', 'dificuldade', key='dificil')],
            [sg.Button('Confirmar!')],
        ]
        janela = sg.Window('Escolha a dificuldade: ', layout)
        while True:
            event, values = janela.read()
            if event == sg.WIN_CLOSED:
                break
            elif event == 'Confirmar!':
                if values['facil']:
                    qtd = (0, 10)
                elif values['medio']:
                    qtd = (0, 100)
                elif values['dificil']:
                    qtd = (0, 1000)
                else:
                    break
                janela.close()
                layout2 = [
                    [sg.Text('Digite o Numero: '), sg.Input(key='input2', size=(10, 1))],
                    [sg.Button('Confirmar!')],
                    [sg.Output(size=(27, 5))]
                ]
                janela2 = sg.Window(f'{qtd[0]} à {qtd[1]}:', layout2)
                numero_sorteado = randint(qtd[0], qtd[1])
                while True:
                    event2, values2 = janela2.read()
                    if event2 == sg.WIN_CLOSED:
                        break
                    try:
                        int(values2['input2'])
                    except:
                        print('Digite apenas NUMEROS')
                    else:
                        if int(values2['input2']) == numero_sorteado:
                            print('Wow, Você acertou :D')
                            sleep(2)
                            break
                        elif int(values2['input2']) > numero_sorteado:
                            print('Chute um numero MENOR')
                        elif int(values2['input2']) < numero_sorteado:
                            print('Chute um numero MAIOR')

if __name__ == "__main__":
    janelaIN = Interfaces('Reddit')
    janelaIN.Acerte_O_Numero()
    janelaIN.Simulador_De_Dados()