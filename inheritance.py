class Automovel():
    def __init__(self, marca:str, ano:int, km:float=0):
        self.marca = marca
        self.ano = ano
        self.km = km

    def __str__(self):
        return f'{self.marca} de {self.ano}, {self.km} km.'
    
    def add_km(self, n:int):
        self.km += n


class Carro(Automovel):
    def __init__(self, marca, ano, placa, km = 0):
        super().__init__(marca, ano, km)
        self.placa = placa
    pass

class Barco(Automovel):
    def __init__(self, marca, ano, km = 0):
        super().__init__(marca, ano, km)
    pass

class Caminhao(Automovel):
    def __init__(self, marca, ano, km = 0):
        super().__init__(marca, ano, km)
    pass

c1 = Carro('Renault', 2018, 'TTN9D56')

print(c1)