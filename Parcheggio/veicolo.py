#Veicolo

listaColori = ["Blu", "Giallo", "Nero", "Bianco"]
listaMarche = ["Audi", "Nissan", "Panda", "Toyota", "BMW", "KTM"]
alimentazione = ["Diesel", "Elettrico", "Benzina"]
alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numList = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

# PROF: la classe Veicolo non funziona. E con essa NIENTE del progetto.
# PROF: Ci sono molti riferimenti a 'variabili' non definite ----> codice COPIATO MALE da un altro
class Veicolo:
    #Init
    def __init__(
        self,
        targa: str,
        marca: str = "Toyota",
        modello: str = "Yaris",
        colore: str = "Giallo",
        cilindrata:int = 100,
        alimentazione: str = "Diesel"):
        
        self.__modello = modello
        
        if marca not in listaMarche:
            raise ValueError("IMPOSSIBLE")
        else:
            self.__marca = marca
        if colore not in listaColori:
              raise ValueError("IMPOSSIBLE")
        else:  
            self.__colore = colore
        if cilindrata < 0 or cilindrata % 100 != 0:
            raise ValueError("value not supported")
        else:
            self.__cilindrata = cilindrata
        if alimentazione not in BenzinaList:
            raise ValueError("IMPOSSIBLE")
        else:
            self.__alimentazione = alimentazione
        if targa[0] in letterList and targa[1] in letterList and targa[2] in numList and targa[3] in numList and targa[4] in numList and targa[5] in letterList and targa[6] in letterList:
            self.__targa = targa
        else:
            raise ValueError("targa not available")
    
    @property
    def targa(self):
        return self.__targa
    
    @property
    def marca(self):
        return self.__marca
    
    @property
    def modello(self):
        return self.__modello
    
    @property
    def colore(self):
        return self.__colore
    
    @property
    def cilindrata(self):
        return self.__cilindrata
    
    @property
    def alimentazione(self):
        return self.__alimentazione
    
    @colore.setter
    def colore(self, value):
        if value in listaColori:
            self.__colore = value
            return
        raise ValueError("colore not in colore list")
           
    def __lt__(self, other):
        if self.__marca.upper() == other.__marca.upper():
            if self.__modello.upper() == other.__modello.upper():
                return self.__cilindrata < other.__cilindrata
            else:
                return self.__modello.upper() < other.__modello.upper()
        else:
            return self.__marca.upper()[0] < other.__marca.upper()

    def __str__(self):
        return __class__.__name__ + str(self.__dict__)
    def __repr__(self):
        return __class__.__name__ + str(self.__dict__)

# PROF: Tutto questo... semplicemente NON è il tuo codice
v = Veicolo("AB123CD")
print(v)
v1 = Veicolo("AB124CD", "Audi")
vList = [v, v1]
vList.sort()
print(vList)
