from multiDictionary import MultiDictionary
from richWord import RichWord

class SpellChecker:

    def __init__(self):
        self.md = MultiDictionary()
        self.md.addDict("italian","resources/Italian.txt")
        self.md.addDict("english","resources/English.txt")
        self.md.addDict("spanish","resources/Spanish.txt")

    def handleSentence(self, txtin, language):
        txtin = replaceChars(txtin)
        txtin = txtin.lower().split(" ")
        words = []
        for word in txtin:
            word = RichWord(word)
            words.append(word)
        self.md.searchWord(words, language)

    def printMenu(self):
        print("______________________________\n" +
              "      SpellChecker 101\n"+
              "______________________________\n " +
              "Seleziona la lingua desiderata\n"
              "1. Italiano\n" +
              "2. Inglese\n" +
              "3. Spagnolo\n" +
              "4. Exit\n" +
              "______________________________\n")


def replaceChars(text):
    chars = "\\*_{}[]><#+-.!$£&%^;,=.ç°§+|'"
    for c in chars:
        text = text.replace(c, "")
    return text