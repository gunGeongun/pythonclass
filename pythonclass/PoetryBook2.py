from Poetry import *

class BookOfPoetry:
    def __init__(self) -> None:
        self.PoetryBook =list()
        self.loadPoetry()
    def loadPoetry(self):
        title = '산유화'
        poet='김소월'
        contents = '''
        산에는 꽃 피네
        꽃이 피네
        갈 봄 여름 없이
        꽃이 피네.
        산에 산에
        피는 꽃은
        저만치 혼자서 피어 있네.
        산에서 우는 작은 새여
        꽃이 좋아
        산에서
        사노라네.
        산에는 꽃이 지네
        꽃이 지네
        갈 봄 여름 없이
        꽃이 지네.
        '''
        myPoetry = Poetry(title,poet,contents.split('\n'))
        self.PoetryBook.append(myPoetry)
    def getPoetry(self,menuNumber):
        return self.PoetryBook[menuNumber-1]
    def getTitles(self):
        return [poetry.getTitle() for poetry in self.PoetryBook]


