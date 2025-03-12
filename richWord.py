class RichWord:
    def __init__(self, parola):
        self._parola = parola # this is a string
        self._corretta = False #this is a bool

    @property
    def parola(self):
        return self._parola

    @property
    def corretta(self):
        # print("getter of parola called" )
        return self._corretta

    @corretta.setter
    def corretta(self, boolvalue):
        # print("setter of parola called" )
        self._corretta = boolvalue

    def __str__(self):
        return self._parola