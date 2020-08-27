# Projeto - 6 Jogo de aventura
# Jogo que terá decisões diferentes baseado nas respostas que foram dadas.
import random
import PySimpleGUI as sg

# Cenário: Uma guerra temos alguns tipos de guerreiro, e dependendo se nascer no norte ou no sul, seguirá para algum local onde irá batalhar.
class JogoDaAventura:
    def __init__(self):
        self.pergunta1 = 'Você nasceu no norte ou no sul? (n/s)' #norte = LadoA e sul = LadoB
        self.pergunta2 = 'Você prefere a espada ou escudo? (espada/escudo)' # Se responder espada vai para LadoA, escudo LadoB
        self.pergunta3 = 'Qual sua especialidade? (linha/tático)' # linha de frente LadoA, Tático LadoB
        self.finalHistoria1 = 'Você irá na linha de frente!'
        self.finalHistoria2 = 'Você defenderá nossas tropas!'
        self.finalHistoria3 = 'Você irá se sacrificar nas batalhas!'
        self.finalHistoria4 = 'Você não é capaz de lutar essa batalha!'
        
    def Iniciar(self):
        #Layout
        layout = [
            [sg.Output(size=(30,0),key='respostas')],
            [sg.Input(size=(25,0),key='escolha')],
            [sg.Button('Responder')]
        ]
        

        #Janela
        self.janela = sg.Window('Jogo de Aventura!',Layout=layout)
        #Ler os dados
        self.LerValores()
        #Fazer algo com os dados
        print(self.pergunta1)
        if self.valores['escolha'] ==  'n':
            print(self.pergunta2) 
            self.LerValores()
            if self.valores['escolha'] == 'espada':
                print(self.finalHistoria1)
            if self.valores['escolha'] == 'escudo':
                print(self.finalHistoria2)
        if self.valores['escolha'] == 's':
            print(self.pergunta3)
            self.LerValores()    
            if self.valores['escolha'] == 'linha':
                print(self.finalHistoria3)
            if self.valores['escolha'] == 'tático':
                print(self.finalHistoria4)

    def LerValores(self):
        self.evento, self.valores = self.janela.Read()           

jogo=JogoDaAventura()
jogo.Iniciar()
