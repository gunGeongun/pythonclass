import sys
import os
import time
#222

def printMenu(menuTitle, menuContents):
    os.system('cls')
    print('\n'*4)
    print('\t\t\t'+menuTitle)
    print('n'*2)
    i = 1
    for content in menuContents:
        print(f'\t\t{i},{content}')
        print()
        i+=1
    print(f'\t\{i}.종  료')
    print('\n'*2)

def getMenuNumber(menuContents):
    menuNumber=input('원하는 번호는 : ')
    validMenuNumbers=[str(i+1) for i in range(len(menuContents)+1)]
    while menuNumber not in validMenuNumbers:
        menuNumber=input('번호 틀림 원하는 번호는 :')
    return menuNumber

def printPoetry(poetry):
    terminalSize=os.get_terminal_size()
    consoleHeight=terminalSize.lines
    print('\n'*40)
    print('\t\t\t'+poetry[0])
    time.sleep(0.3)
    print()
    time.sleep(0.3)
    print('\t\t\t\t\t'+poetry[1])
    time.sleep(0.3)
    print()
    time.sleep(0.3)
    for content in poetry[2:]:
        print(f'\t\t\t\t\t{content}')
        time.sleep(0.3)
    for i in range(consoleHeight-len(poetry)):
        print()
        time.sleep(0.3)
    input('다 봤으면 아무키나...')

jinDalRae='''진달래 꽃
김소월
나보기가 역겨워....
나보기가 역겨워....
나보기가 역겨워....
나보기가 역겨워....
나보기가 역겨워....
나보기가 역겨워....
나보기가 역겨워....
'''
choHon='''진달래 꽃2
김소월
나보기가 역겨워....
나보기가 역겨워....
나보기가 역겨워....
나보기가 역겨워....
나보기가 역겨워....
나보기가 역겨워....
나보기가 역겨워....
'''
umMaYa='''진달래 꽃3
김소월
나보기가 역겨워....
나보기가 역겨워....
나보기가 역겨워....
나보기가 역겨워....
나보기가 역겨워....
나보기가 역겨워....
나보기가 역겨워....
'''
gaeYeoUl='''진달래 꽃4
김소월
나보기가 역겨워....
나보기가 역겨워....
나보기가 역겨워....
나보기가 역겨워....
나보기가 역겨워....
나보기가 역겨워....
나보기가 역겨워....
'''

myPoetryBook=[jinDalRae.split('\n'),choHon.split('\n'),umMaYa.split('\n'),gaeYeoUl.split('\n')]
title = "시를 감상합시다"
contents=['진달래 꽃','진달래 꽃2','진달래 꽃3','진달래 꽃4']
printMenu(title,contents)
menuNumber = getMenuNumber(contents)
while menuNumber != '5':
    printPoetry(myPoetryBook[int(menuNumber)-1])
    input()
    printMenu(title,contents)
    menuNumber = getMenuNumber(contents)


    


# 좋은 프로그램을 작성하는 방법 5가지 카멜
