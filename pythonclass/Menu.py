#시 출력 프로그램 (메뉴 객체를 위한 클래스 Menu.py) 1926005 2학년 김건 
import os,sys,time
class Menu:
    def __init__(self,title,contents):
        self.title = title
        self.contents = contents
    def getMenuNumber(self):
        menuNumber = input('원하는 번호를 입력하시오: ')
        validMenuNumbers = [str(i+1) for i in range(len(self.contents)+1)]
        while menuNumber not in validMenuNumbers:
            menuNumber = input('번호가 틀렸습니다. 원하는 번호를 다시 입력하시오 :')
        return menuNumber
    def isExit(self,menuNumber):
        if menuNumber == str(len(self.contents)+1):
            return True
        else :
            return False

    def print(self):
        os.system('cls')
        print('\n'*4)
        print('\t'+self.title)
        print()
        i = 1
        for content in self.contents:
            print(f'{i}.{content}')
            print()
            i += 1
        print(f'{i}.종료')
        print('\n'*2)