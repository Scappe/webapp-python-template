class Impegni:
    def __init__(self, giorno):

        self.ora = []

        for index in range(0, 24):
            self.ora.append(False)


appuntamenti = [Impegni("martedi"), Impegni("mercoledì"), Impegni(
    "giovedì"), Impegni("venerdì"), Impegni("sabato")]
