class Carro:
    def __init__(self, km=0):
        self.km = km
        pass
    
    class Comandos:
        def __init__(self, outer):
            self.outer = outer #caso a inner class (Comandos) queira ter acesso à outer class (Carro)

        def dirigir():
            print('dirigindo...')
        
        def get_km(self):
            print(self.outer.km)
        

c1 = Carro()

c1.Comandos.dirigir()
c1.Comandos(c1).get_km()