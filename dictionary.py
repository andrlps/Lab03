class Dictionary:
    def __init__(self):
        self._dict = list()

    def loadDictionary(self,path):
        try:
            txt = open(path, "r")
        except FileNotFoundError:
            print("File not found")
            pass
        for line in txt:
            l = line.rstrip()
            self.dict.append(l)
        txt.close()

    def printAll(self):
        mystr = ""
        for l in self.dict:
            mystr += l + "\n"
        print(mystr)

    @property
    def dict(self):
        return self._dict
