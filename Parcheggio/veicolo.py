#livello 0

listacolori = ["blu", "giallo", "nero", "bianco"]
listamarca = ["Audi", "Nissan", "Fiat", "Iveco", "Volkswagen"]
listaalim = ["diesel", "elettrico", "benzina"]
listalett = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z" ]
listanum = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

class Veicolo:
    def __init__(self, marca="volkswagen",modello="Golf",colore="nero",cilindrata:int = 1600,alimentazione:str = "diesel"):
        #se scrivo la marca in minuscolo me la riporta in maiuscolo
        if marca.capitalize() in listamarca:
            self.marca = marca
        else:
            raise ValueError("Non rientra tra le marche")
            
        #controllo che la cilindrata sia multiplo di 100
        if cilindrata%100 == 0:
            self.cilindrata = cilindrata
        else:
            raise ValueError("La cilindrata non è accettabile")
        