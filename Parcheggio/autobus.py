
from Veicolo import Veicolo

class Autobus(Veicolo):
    def __init__(self,targa: str,marca: str = "iveco",modello: str = "CityClass",colore:str = "bianco",cilindrata:int = 9000,alimentazione:str = "diesel",npassmax: int = 51,npasstr: int = 1,weightmax: int = 10000,weighttr: int = 8000):
        super().__init__(targa, marca, modello, colore, cilindrata, alimentazione)
        if npassmax <= 0:
            raise ValueError("impossibile")
        else:
            self.npassmax = npassmax
        if npasstr < 0 or npasstr > npassmax:
            raise ValueError("impossibile")
        else:
            self.npasstr = npasstr
        if weightmax <= 0:
            raise ValueError("impossibile")
        else:
            self.weightmax = weightmax
        if weighttr < 0 or weighttr > weightmax:
            raise ValueError("impossibile")
        else:    
            self.weighttr = weighttr
            
    def __str__(self):
        return __class__.__name__ + str(self.__dict__)
    
    def __repr__(self):
        return __class__.__name__ + str(self.__dict__)
            
a = Autobus("EF321GP")
print(a)
