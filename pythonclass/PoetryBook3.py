from Poetry import *

class BookOfPoetry:
    def __init__(self) -> None:
        self.PoetryBook =list()
        self.loadPoetry()
    def loadPoetry(self):
        poetFile = open('C:\gunpy\pythonclass\고향.txt','r',encoding="UTF8")
        readPoetFile=poetFile.readlines()
        myPoetry = Poetry(readPoetFile[0],readPoetFile[1],readPoetFile[2:])
        self.PoetryBook.append(myPoetry)
        poetFile = open('C:\gunpy\pythonclass\눈물.txt','r',encoding="UTF8")
        readPoetFile=poetFile.readlines()
        myPoetry = Poetry(readPoetFile[0],readPoetFile[1],readPoetFile[2:])
        self.PoetryBook.append(myPoetry)
        poetFile = open('C:\gunpy\pythonclass\산유화.txt','r',encoding="UTF8")
        readPoetFile=poetFile.readlines()
        myPoetry = Poetry(readPoetFile[0],readPoetFile[1],readPoetFile[2:])
        self.PoetryBook.append(myPoetry)
        poetFile = open('C:\gunpy\pythonclass\마음.txt','r',encoding="UTF8")
        readPoetFile=poetFile.readlines()
        myPoetry = Poetry(readPoetFile[0],readPoetFile[1],readPoetFile[2:])
        self.PoetryBook.append(myPoetry)
        poetFile = open('C:\gunpy\pythonclass\목숨.txt','r',encoding="UTF8")
        readPoetFile=poetFile.readlines()
        myPoetry = Poetry(readPoetFile[0],readPoetFile[1],readPoetFile[2:])
        self.PoetryBook.append(myPoetry)
    def getPoetry(self,menuNumber):
        return self.PoetryBook[menuNumber-1]
    def getTitles(self):
        return [poetry.getTitle() for poetry in self.PoetryBook]


