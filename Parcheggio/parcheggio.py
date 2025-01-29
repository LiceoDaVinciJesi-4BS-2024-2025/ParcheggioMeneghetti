#Parcheggio

from posto_mezzo import *
from auto import *
from moto import *
import datetime

class Parcheggio:
    def __init__(self):
        self.__postiMassimiAuto = 1000
        self.__postiMassimiMoto = 200
        self.__postiAuto = []
        self.__postiMoto = []
        self.__prezziAllOra = {
        "auto": 1.5,
        "moto": 1.2
        }
        for x in range(self.__postiMassimiMoto):
            self.__postiMoto.append(PostoMezzo())
        for y in range(self.__postiMassimiAuto):
            self.__postiAuto.append(PostoMezzo())
        
    @property
    def postiMassimiAuto(self):
        return self.__postiMassimiAuto
    @property
    def postiMassimiMoto(self):
        return self.__postiMassimiMoto
    @property
    def postiMoto(self):
        return self.__postiMoto
    @property
    def postiAuto(self):
        return self.__postiAuto

    
    
    def prenotaPosto(self, veicolo, oreDiSoggiorno):
        if type(veicolo) not in veicoliAmmessi:
            raise ValueError("Tipo veicolo non disponibile")
        if type(veicolo) == Auto:
            for x in self.__postiAuto:
                if x.libero:
                    x.parcheggia(veicolo, oreDiSoggiorno)
                    return
        else:
            for y in self.__postiMoto:
                if y.libero:
                    y.prenotaPosto(vehicle, oreDiSoggiorno)
                    return
        return


    def pagaGiornaliera(self):
        totaleSoldi = 0
        for x in self.__postiMoto:
            if not x.libero:
                tempoDiSoggiorno = x.giornoOraDiUscita - datetime.datetime.now()
                soldi = self.__prezziAllOra * (tempoDiSoggiorno.total_seconds() / 3600)
                totaleSoldi += soldi

        for y in self.__postiAuto:
            if not y.libero:
                tempoDiSoggiorno = y.giornoOraDiUscita - datetime.datetime.now()
                soldi = self.__prezziAllOra * (tempoDiSoggiorno.total_seconds() / 3600)
                totaleSoldi += soldi

        return totaleSoldi

    def liberaPosti(self):
        for x in self.__postiMoto:
            if not x.libero and x.giornoOraDiUscita < datetime.datetime.now():
                x.liberaPosto()

        for y in self.__postiAuto:
            if not y.libero and y.giornoOraDiUscita < datetime.datetime.now():
              y.liberaPosto()
        return

    def __str__(self):
        return __class__.__name__ + str({"postiMassimiAuto": self.__postiMassimiAuto, "postiMassimiMoto": self.__postiMassimiMoto, "prezziAllOra": self.__prezziAllOra})
    def __repr__(self):
        return __class__.__name__ + str({"postiMassimiAuto": self.__postiMassimiAuto, "postiMassimiMoto": self.__postiMassimiMoto, "prezziAllOra": self.__prezziAllOra})
    
    
#--<<|>>----<<|>>----<<|>>----<<|>>----<<|>>----<<|>>----<<|>>----<<|>>----<<|>>----<<|>>----<<|>>----<<|>>----<<|>>----<<|>>----<<|>>----<<|>>----<<|>>----<<|>>--

if __name__ == "__main__":
    parcheggino = Parcheggio()
    print(parcheggino)
    parcheggino.liberaPosti()
    v1 = Car("AG666ES")
    v2 = Motorbike("GG324GJ")
    v3 = Motorbike("BO111SI")
    parcheggino.prenotaPosto(v1, 3)
    parcheggino.prenotaPosto(v2, 2)
    parcheggino.prenotaPosto(v3, 4)
    print(parcheggino)

    file = open("park.data", "w")
    file.write("Parcheggio Auto: \n")
    for x in range(parcheggino.postiMassimiAuto):
        file.write(str(parcheggino.postiAuto[x]) + "\n")
    file.write("Parcheggio Moto: \n")
    for y in range(parcheggino.postiMassimiMoto):
        file.write(str(parcheggino.postiMoto[y]) + "\n")
    file.close()
