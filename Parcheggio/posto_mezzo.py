#Parking posto

#Meneghetti Sebastiano
#4BS
#postomezzo

from datetime import datetime
from datetime import timedelta
tipologieMezzi = ["moto","auto"]

class PostoMezzo:
    def __init__(self):
        self.__parcheggioAuto = 1
        self.__parcheggioMoto = 1
        self.__postiOccupati = {}

    def __str__(self):
        return str(self.__dict__)
    def __repr__(self):
        return str(self.__dict__)
    
    @property
    def parcheggioMoto(self):
        return self.__parcheggioMoto

    @property
    def parcheggioAuto(self):
        return self.__parcheggioAuto

    def occupaPosto(self, tipologiaMezzo, targa, arrivo , oreSosta):
        if tipologiaMezzo.lower() not in tipologieMezzi:
            raise ValueError("Questo mezzo non è valido")
        if targa in self.__postiOccupati:
            raise ValueError("Veicolo già presente")
        orarioArrivo = arrivo
        orarioUscita = arrivo + timedelta(hours=oreSosta)
        if tipologiaMezzo.lower() == "moto":
            if self.__parcheggioMoto > 0:
                self.__parcheggioMoto -= 1
                self.__postiOccupati[targa] = (tipologiaMezzo, orarioArrivo, orarioUscita)
            else:
                raise ValueError("non ci sono più posti per moto")
        
        elif tipologiaMezzo.lower() == "auto":
            if self.__parcheggioAuto > 0:
                self.__parcheggioAuto -= 1
                self.__postiOccupati[targa] = (tipologiaMezzo, orarioArrivo, orarioUscita)
            else:
                raise ValueError("non ci sono più posti per auto")

    def liberaPosto(self, targa):
        if targa not in self.__postiOccupati:
            raise ValueError("il veicolo non è nel parcheggio")
        tipologiaMezzo = self.__postiOccupati.pop(targa)[0]
        if tipologiaMezzo.lower() == "moto":
            self.__parcheggioMoto += 1
        elif tipologiaMezzo.lower() == "auto":
            self.__parcheggioAuto += 1

#--------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    oggetto = PostoMezzo()
    print(oggetto)
    print()
    print("------AUTO------")
    print("OCCUPO POSTO AUTO")
    oggetto.occupaPosto("Auto", "TG473HH", datetime.now(),13)
    print(oggetto)
    print("LIBERO POSTO AUTO")
    oggetto.liberaPosto("TG473HH")
    print(oggetto)
    print()
    print("------MOTO------")
    print("OCCUPO POSTO MOTO")
    oggetto.occupaPosto("Moto", "FL385TR", datetime.now(),43)
    print(oggetto)
    print("LIBEO POSTO MOTO")
    oggetto.liberaPosto("FL385TR")
    print(oggetto)
    