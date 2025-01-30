#Parking posto

from moto import *
from auto import *
import datetime

veicoliAmmessi = [Auto, Moto]

class PostoMezzo:
    def __init__(self):
        self.__veicolo = None
        self.__targaVeicolo = ""
        self.__libero = True
        self.__giornoOraDiUscita = None
    
    def __str__(self):
        return __class__.__name__ + str(self.__dict__)
    def __repr__(self):
        return __class__.__name__ + str(self.__dict__)

    @property
    def veicolo(self):
        return self.__veicolo

    @property
    def targaVeicolo(self):
        return self.__targaVeicolo

    @property
    def libero(self):
        return self.__libero

    @property
    def giornoOraDiUscita(self):
        return self.__giornoOraDiUscita
    
    def parcheggia(self, veicolo, oreDiSoggiorno: int):
        if type(veicolo) not in veicoliAmmessi:
            raise ValueError("Invalid veicolo type")

        self.__targaVeicolo = veicolo.targa
        self.__giornoOraDiUscita = datetime.datetime.now() + datetime.timedelta(hours = oreDiSoggiorno)
        self.__libero = False
        return

    def liberaPosto(self):
        self.__targaVeicolo = ""
        self.__veicolo = None
        self.__libero = True
        self.__giornoOraDiUscita = None
        return


print("--<<|>>----<<|>>----<<|>>----<<|>>----<<|>>----<<|>>----<<|>>----<<|>>----<<|>>----<<|>>----<<|>>----<<|>>----<<|>>----<<|>>----<<|>>----<<|>>----<<|>>----<<|>>----<<|>>--")
posto = PostoMezzo()
print(posto)
print(posto.giornoOraDiUscita)
auto = Auto("AB123CD")
posto.parcheggia(Auto, 3)
print(posto.giornoOraDiUscita)
  
