#시 출력 프로그램 (__main__ 시 출력 메인프로그램 myPoetry.py)) 1926005 2학년 김건 
from Poetry import *
from PoetryBook import *
from Menu import *

menuTitle = '시 출력 프로그램'

poetBook = PoetryBook(myPoetryBook)
titles = poetBook.getTitles()

myMenu = Menu(menuTitle,titles)
myMenu.print()
menuNumber = myMenu.getMenuNumber()
getPoetry = poetBook.getPoetry(menuNumber)

while not myMenu.isExit(menuNumber):
    getPoetry.print()
    myMenu.print()
    menuNumber = myMenu.getMenuNumber()




