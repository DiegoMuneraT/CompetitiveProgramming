class Bees:
    __elements = []

    def __init__(self):
        self.__elements = []

    def size(self):
        return len(self.elements)

    def get(self, index):
        return self.__elements[index]

    def add(self, object):
        self.elements.append(object)

    def addInIndex(self, index, object):
        self.__elements = self.__elements[:index] + [object] + self.__elements[index:]

    def removeInIndex(self, index):
        self.__elements = self.__elements.remove(self.__elements[index])

