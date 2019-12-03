


class Impegni:
    def __init__(self, giorno):

        self.ora = []

        for idxElement in range(0,24):
            self.ora[idxElement] = False


appuntamenti = [Impegni("martedi"), "mercoledi", "giovedi", "venerdi", "sabato"]