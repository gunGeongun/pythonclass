from inspect import getmembers
import sys,os,time
def jin():
    print('\t\t\t진달래 꽃')
    time.sleep(1)
    print()
    time.sleep(1)
    print('\t\t\t\t\t김  소  월')
    time.sleep(1)
    print()
    time.sleep(1)
    print('\t진달래 꽃 진달래 꽃진달래 꽃진달래 꽃진달래 꽃')
    time.sleep(1)
    print('\t진달래 꽃 진달래 꽃진달래 꽃진달래 꽃진달래 꽃')
    time.sleep(1)
    print('\t진달래 꽃 진달래 꽃진달래 꽃진달래 꽃진달래 꽃')
    time.sleep(1)
    print('\t진달래 꽃 진달래 꽃진달래 꽃진달래 꽃진달래 꽃')
    time.sleep(1)
    print('\t진달래 꽃 진달래 꽃진달래 꽃진달래 꽃진달래 꽃')
    time.sleep(1)
    print('\t진달래 꽃 진달래 꽃진달래 꽃진달래 꽃진달래 꽃')
    time.sleep(1)
    for i in range(10):
        print()

def printMenu():
    os.system('cls')
    print()
    print()
    print('김소월 시선')
    print()
    print("1.~~~")
    print()
    print("2.~~~")
    print()
    print("3.~~~")
    print("원하는 시를 선택하세요:",end='')

def getMenuNumber():
    menuNumber=input()
    while menuNumber not in ['1','2','3','4']:
        print('잘못 입력 했어')
        menuNumber=input()
    return menuNumber

printMenu()
menuNumber=getMenuNumber()
while menuNumber != '4':
    if menuNumber=='1':
        jin()
    elif menuNumber=='2':
        print("두번째")
    elif menuNumber=='3':
        print("3333")
    input("감상 끝났으면 아무키나")
    printMenu()
    menuNumber=getMenuNumber()
print("빠이")
input()




#리스트 이용