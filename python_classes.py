print('Me habituando com métodos, classes, herança e boas práticas')

class Carro:
    def __init__(self, brand:str, model:str, plaque:str, km:int=0):
        self.brand = brand
        self.model = model
        self.plaque = plaque
        self.km = km
    
    def __str__(self):
        return f'{self.brand} {self.model} {self.km} km de placa {self.plaque}'
    
    def info(self):
        return f'Brand: {self.brand} \nModel: {self.model} \nPlaque: {self.plaque} \nKm: {self.km}'
    
    
    def honk(self, n:int):
        honks = ''
        for i in range(n):
            honks = honks + 'HONK '
        return honks
    
    def add_km(self, km):
        self.km += km

sandero = Carro('Fiat', 'Cronos', 'TTR4E90')
print(sandero.info())
sandero.add_km(10)
print(sandero.info())

print(sandero)