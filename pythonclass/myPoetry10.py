from Poetry import *
from Menu2 import *
from PoetryBook3 import *
title = "시 출력 프로그램"
myPoetryBook =BookOfPoetry()
myMenu = Menu(title,myPoetryBook.getTitles())
myMenu.print()
menuNumber =myMenu.getMenuNumber()
while not myMenu.isExit(menuNumber):
    myPoetry = myPoetryBook.getPoetry(menuNumber)
    myPoetry.print()
    myMenu.print()
    menuNumber = myMenu.getMenuNumber()

input("시 프로그램을 종료합니다.")
