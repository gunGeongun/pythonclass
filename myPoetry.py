from Poetry import *
from PoetryBook import *

menuTitle = '나의 애송시'
menuContents = [Poetry.getTitle() for Poetry in myPoetryBook]


myPoetryBook[0].print()



# menu.py ,  PoetryBook 이라는 객체를 하나 더만드는데 init(self)