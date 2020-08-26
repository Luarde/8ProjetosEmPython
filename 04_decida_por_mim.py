# Projeto - 5 Decida por Mim
# Faça uma pergunta para o programa, e ele terá que te dar uma resposta.
import random 
import PySimpleGUI as sg


class DecidaPorMim:
    def __init__(self):
        self.respostas = [
            'Com certeza você deve fazer isso!',
            'Não sei. você sabe',
            'Não faz isso!'   
            'Acho que ta na hora certa!'
        ]

    def Iniciar(self):
        #Layout
        layout = [
            [sg.Text('Faça sua pergunta: ')],
            [sg.Input()],
            [sg.Output(size=(50,10))],
            [sg.Button('Decida Por Mim')]
        ]
        # Criar uma janela
        self.janela = sg.Window('Decida Por Mim!',layout=layout)
        while True:
            # Ler os valores
            self.eventos, self.valores = self.janela.Read()
            # Fazer alguma coisa Com os valores
            if self.eventos == 'Decida Por Mim':
                print(random.choice(self.respostas))



decida = DecidaPorMim()
decida.Iniciar()