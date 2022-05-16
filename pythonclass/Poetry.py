#시 출력 프로그램 (시 객체를 위한 클래스 Poetry.py) 1926005 2학년 김건 
import os,sys,time

class Poetry:
    def __init__(self,title,poet,contents):
        self.title = title
        self.poet = poet
        self.contents = contents
        self.consoleHeight = os.get_terminal_size().lines
        self.upSpeed = 0.5
    def print(self):
        print('\n'*self.consoleHeight)
        print('\t\t\t' + self.title)
        time.sleep(self.upSpeed)
        print()
        time.sleep(self.upSpeed)
        print('\t\t\t\t\t'+self.poet)
        time.sleep(self.upSpeed)
        for content in self.contents:
            print('\t' + content)
            time.sleep(self.upSpeed)
        for i in range(self.consoleHeight-len(self.contents)-7):
            print()
            time.sleep(self.upSpeed)
        input("감상 끝났으면 아무키나 누르세요.")
    def getTitle(self):
        return self.title
