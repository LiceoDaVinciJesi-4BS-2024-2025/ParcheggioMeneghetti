#Moto

from veicolo import Veicolo

class Moto(Veicolo):
    def __init__(self,
        targa: str,
        marca: str = "KTM",
        modello: str = "",
        colore: str = "Giallo",
        cilindrata:int = 100,
        alimentazione: str = "Diesel",
        passeggeriMassimi: int = 2,
        passeggeriABordo: int = 2):
        
        super().__init__(targa, marca, modello, colore, cilindrata, alimentazione)
        
        self.__passeggeriMassimi = passeggeriMassimi
        if passeggeriABordo <= self.__passeggeriMassimi:
            self.__passeggeriABordo = passeggeriABordo
        else:
            raise ValueError("I passeggeri a bordo non possono essere più di quelli massimi ammessi")
        
    def __str__(self):
        return __class__.__name__ + str(self.__dict__)
    def __repr__(self):
        return __class__.__name__ + str(self.__dict__)        
