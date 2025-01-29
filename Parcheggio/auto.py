from Veicolo import Veicolo

class Auto(Veicolo):
    def __init__(self,targa: str,marca: str = "Volkswagen",modello: str = "Golf",colore:str = "blu",cilindrata:int = 1600,alimentazione:str = "diesel",npassmax: int = 6,npasstr: int = 2,weightmax: int = 500,weightr: int = 300):
        super().__init__(targa, marca, modello, colore, cilindrata, alimentazione)
        if npassmax <= 0:
            raise ValueError("impossibile")
        else:
            self.npassmax = npassmax
        if npasstr < 0 or npasstr > npass:
            raise ValueError("Qualcuno deve essersi buttato fuori...")
        else:
            self.npasstr = npasstr
        if npweightmaxass <= 0:
            raise ValueError("impossibile")
        else:
            self.weightmax = weightmax
        if weightr < 0 or weightr > weightmax:
            raise ValueError("impossibile")
        else:    
            self.weightr = weightr
            
    def __str__(self):
        return __class__.__name__ + str(self.__dict__)
    
    def __repr__(self):
        return __class__.__name__ + str(self.__dict__)