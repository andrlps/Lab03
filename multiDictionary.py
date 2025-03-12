import time
from dictionary import Dictionary

class MultiDictionary:

    def __init__(self):
       self.dictionary = dict()

    def addDict(self, language, filename):
        self.dictionary[language] = Dictionary()
        self.dictionary[language].loadDictionary(filename)

    def printDic(self, language):
        pass

    def searchWord(self, words, language):
        dic = self.dictionary[language].dict
        print()
        print("______________________________\n"+"Using contains")
        tic = time.time()
        for word in words:
            if dic.__contains__(word.parola):
                word.corretta = True
            else:
                print(word.parola)
        toc = time.time()
        print("Time elapsed: " + str(toc-tic))
        print("______________________________\n"+"Using contains")
        tic = time.time()
        for word in words:
            for d in dic:
                if word.parola == d:
                    word.corretta = True
            if not word.corretta:
                print(word.parola)
        toc = time.time()
        print("Time elapsed: " + str(toc-tic))
        print("______________________________\n"+"Using contains")
        tic = time.time()
        for word in words:
            sinistra = 0
            destra = len(dic) - 1
            while sinistra <= destra:
                i = (sinistra + destra) // 2  # Calcolo dell'indice medio
                if dic[i] == word.parola:
                    word.corretta = True
                    break # Parola trovata
                elif dic[i] < word.parola:
                    sinistra = i + 1  # Cerca nella metà destra
                else:
                    destra = i - 1  # Cerca nella metà sinistra
            if not word.corretta:
                print(word.parola)
        toc = time.time()
        print("Time elapsed: " + str(toc-tic))