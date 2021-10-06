

class calcComb:

    def __init__(self,stringa):
        
        self.__stringa = stringa
        self.stringalist = list(stringa)

    def getStringa(self):
        return self.__stringa

    def getStringalist(self):
        return self.stringalist

    def setStringa(self, str):
        self.__stringa = str
        self.stringalist = list(str)

    def permutazioni(self, k):
        return len(self.__stringa)**k
pippo = calcComb("pippo mangia")
print(pippo.permutazioni(3))
print(pippo.stringa)
print(pippo.getStringa())

pippo.setStringa("casa")
print(pippo.stringa)
print(pippo.stringalist)