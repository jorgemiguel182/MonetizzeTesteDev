from random import sample
from tabulate import tabulate

class MonetizzeTeste:
    def __init__(self, quantidade_dezenas, total_jogos):
        self.quantidade_dezenas = quantidade_dezenas
        self.total_jogos = total_jogos
        self.resultado = []
        self.jogos = []
   
    @property
    def quantidade_dezenas(self):
        return self._quantidade_dezenas
    
    @quantidade_dezenas.setter
    def quantidade_dezenas(self, value):
        if int(value) not in range(6, 10):
            raise ValueError('O valor precisa estar entre 6 e 10')
        self._quantidade_dezenas = value
    
    def _dezenas_aleatorias(self):
        return sorted(sample(range(1,60), self._quantidade_dezenas))
        
    def retorna_jogos(self):
        lista_jogos = []
        for t in range(0, self.total_jogos):
            lista_jogos.append(self._dezenas_aleatorias())
        self.jogos = lista_jogos
        
    def sorteio_resultado_aleatorio(self):
        self.resultado = sorted(sample(range(1,60), 6))
        
    def confere_jogos(self):
        lista_conferencia = []
        for jogo in self.jogos:
            lista_interna = [jogo]
            lista_interna_resultado = ["Esse jogo acertou " + str(len(set(jogo).intersection(self.resultado))) + " dezenas.", list(set(jogo).intersection(self.resultado))]
            lista_interna.append(lista_interna_resultado)
            lista_conferencia.append(lista_interna)
        print(tabulate(lista_conferencia, tablefmt='html'))
            