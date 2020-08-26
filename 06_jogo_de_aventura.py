# Projeto - 6 Jogo de aventura
# Jogo que terá decisões diferentes baseado nas respostas que foram dadas.

import random

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
        resposta1 = input(self.pergunta1)
        if resposta1 ==  'n':
            resposta1B = input(self.pergunta2) 
            if resposta1B == 'espada':
                print(self.finalHistoria1)
            if resposta1B == 'escudo':
                print(self.finalHistoria2)
        if resposta1 == 's':
            resposta1B = input(self.pergunta3)    
            if resposta1B == 'linha':
                print(self.finalHistoria3)
            if resposta1B == 'tático':
                print(self.finalHistoria4)

jogo=JogoDaAventura()
jogo.Iniciar()
