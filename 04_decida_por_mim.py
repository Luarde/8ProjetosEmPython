# Projeto - 5 Decida por Mim
# Faça uma pergunta para o programa, e ele terá que te dar uma resposta.
import random


class DecidaPorMim:
    def __init__(self):
        self.respostas = [
            'Com certeza você deve fazer isso!',
            'Não sei. você sabe',
            'Não faz isso!'   
            'Acho que ta na hora certa!'
        ]

    def Iniciar(self):
        input('Faça sua pergunta: ')
        print(random.choice(self.respostas))

decida = DecidaPorMim()
decida.Iniciar()