import copy

from database.meteo_dao import MeteoDao


class Model:
    def __init__(self):
        self.bestCammino = []
        self.costo = None
        self.situazioni = []

    def getUmidita(self, mese):
        return MeteoDao.getUmidita(mese)

    def getSequenza(self, mese):
        self.situazioni = MeteoDao.get_all_situazioni(mese)
        self.ricorsione([])
        return self.costo, self.bestCammino

    def ricorsione(self, parziale):
        if len(parziale) == 15:
            if self.costo is None or self.calcolaCosto(parziale) < self.costo:
                self.bestCammino = copy.deepcopy(parziale)
                self.costo = self.calcolaCosto(parziale)
                print(self.costo)
        else:
            for s in self.situazioni:
                if self.condizione(s, parziale):
                    parziale.append(s)
                    self.ricorsione(parziale)
                    parziale.pop()

    def calcolaCosto(self, parziale):
        peso = 0
        for s in parziale:
            peso += s.umidita
        return peso

    def condizione(self, s, parziale):
        if len(parziale) == 0:
            return True
        if parziale[-1].data.day != s.data.day-1:
            return False
        if len(parziale) < 3:
            if parziale[-1].localita == s.localita:
                return True
            else:
                return False
        numGiorni = 0
        for i in range(len(parziale)):
            if parziale[i].localita == s.localita:
                numGiorni += 1
        if numGiorni >= 6:
            return False
        var = True
        for i in range(len(parziale)-3, len(parziale)-1):
            if parziale[i].localita != parziale[i+1].localita:
                var = False
        if var:
            return True
        else:
            if s.localita == parziale[-1].localita:
                return True
            else:
                return False






