import PySimpleGUI as sg
from string import ascii_lowercase, ascii_uppercase, digits, punctuation
from random import randint
from time import sleep

class PasswordGenerator:
    def __init__(self, theme):
        sg.theme(theme)
        self.__layout = [
            [sg.Text('Quantas senhas quer gerar:'), sg.Input(size=(5, 1), key='Input', default_text=3)],
            [sg.Text('De quantos caracteres:'), sg.Input(size=(5, 1), key='Input2', default_text=10)],
            [sg.Checkbox('Maiúsculas', default=True, key='Maiusc'), sg.Checkbox('Minúsculas', default=True, key='Minusc')],
            [sg.Checkbox('Números   ', default=True, key='Numeri'), sg.Checkbox('Caracteres Espec.', default=True, key='CarEsp')],
            [sg.Button('Ok', size=(5, 1)),sg.CButton('Cancel')],
            [sg.Output(size=(31, 10))],
        ]
    
    def Init(self):
        window = sg.Window('Password Generator',self.__layout)
        while True:
            self.__Car = ''
            event, values = window.read()
            if values['Maiusc']:
                self.__Car += ascii_uppercase
            if values['Minusc']:
                self.__Car += ascii_lowercase
            if values['Numeri']:
                self.__Car += digits
            if values['CarEsp']:
                self.__Car += punctuation
            if not self.__Car == '':
                if event == sg.WIN_CLOSED:
                    break
                if event == 'Ok':
                    try:
                        int(values['Input'])
                        int(values['Input2'])
                    except:
                        if values['Input'] == '' or values['Input2'] == '':
                            print('Digite os valores nos campos acima')
                            continue
                        print('Digite apenas NÚMEROS')
                    else:
                        values['Input'] = int(values['Input'])
                        values['Input2'] = int(values['Input2'])
                        for _ in range(0, values['Input']):
                            for _ in range(0, values['Input2']):
                                print(self.__Car[randint(0, len(self.__Car) - 1)], end='')
                            print('\n' + ('-=' * 17))
                            if values['Input'] >= 100:
                                sleep(0.1)
                            else:
                                sleep(0.25)
                        continue
                    

test = PasswordGenerator('Reddit')
test.Init()