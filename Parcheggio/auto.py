#Car

from veicolo import Veicolo

class Auto(Veicolo):
    #Prendo i parametri necessari per crare un oggetto di classe Auto
    def __init__(
        self,
        targa: str,
        marca: str = "Toyota",
        modello: str = "Yaris",
        colore: str = "Giallo",
        cilindrata:int = 100,
        alimentazione: str = "Diesel",
        passeggeriMassimi: int = 4,
        passeggeriABordo: int = 3,
        pesoMassimo: int = 20,
        pesoTrasportato: int = 10):

        #Uso la __ini__() del veicolo per i controlli su alcuni parametri
        super().__init__(targa, marca, modello, colore, cilindrata, alimentazione)

        #Aggiungo i controlli sui parametri non inclusi nel veicolo
        self.__passeggeriMassimi = passeggeriMassimi
         
        if passeggeriABordo > self.__passegeriMassimi:
            raise ValueError("I passeggeri a bordo non possono essere più di quelli massimi ammessi")
        else:
            self.__passeggeriABordo = passeggeriABordo

    #Funzioni standard
    def __str__(self):
        return __class__.__name__ + str(self.__dict__)
    def __repr__(self):
        return __class__.__name__ + str(self.__dict__)

#Test
a = Auto("AB123CD")
print(a)
