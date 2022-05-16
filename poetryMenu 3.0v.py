# 5개의 시중 원하는 시를 선택하는 시 메뉴 출력 프로그램 1926005 2학년 김건
import sys
import os
import time


def printMenu(menuTitle, menuContents):
    os.system('cls')
    print('\n'*4)
    print('\t'+menuTitle)
    print()
    i = 1
    for content in menuContents:
        print(f'{i}.{content}')
        print()
        i += 1
    print(f'{i}.종료')
    print('\n'*2)


def getMenuNumber(menuContents):
    menuNumber = input('원하는 번호를 입력하시오: ')
    validMenuNumbers = [str(i+1) for i in range(len(menuContents)+1)]
    while menuNumber not in validMenuNumbers:
        menuNumber = input('번호가 틀렸습니다. 원하는 번호를 다시 입력하시오 :')
    return menuNumber


def printTitle(poetry):
    upSpeed = time
    print('\n'*40)
    print('\t\t\t'+poetry[0])
    upSpeed.sleep(1)
    print()
    upSpeed.sleep(1)


def printPoet(poetry):
    upSpeed = time
    print('\t\t\t\t'+poetry[1])
    upSpeed.sleep(1)
    print()
    upSpeed.sleep(1)


def printContents(poetry):
    upSpeed = time
    terminalSize = os.get_terminal_size()
    consoleHeight = terminalSize.lines
    for content in poetry[2:]:
        print(f'\t{content}')
        upSpeed.sleep(1)
    for i in range(consoleHeight-len(poetry)):
        print()
        upSpeed.sleep(1)


def printPoetry(poetry):
    printTitle(poetry)
    printPoet(poetry)
    printContents(poetry)
    input('감상이 끝났으면 아무키나 누르세요.')


def isExitMenuNumber(menuNumber, menuContents):
    if menuNumber == str(len(menuContents)+1):
        print("프로그램을 종료합니다.")
        sys.exit(0)


sanYuHwa = '''산유화
         김소월
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
goHyang = '''고향
         백 석
나는 북관(北關)에 혼자 앓아 누워서
어느 아침 의원(醫員)을 뵈이었다.
의원은 여래(如來) 같은 상을 하고 관공(關公)의 수염을 드리워서
먼 옛적 어느 나라 신선 같은데,
새끼손톱 길게 돋은 손을 내어
묵묵하니 한참 맥을 짚더니
문득 물어 고향이 어데냐 한다.
평안도 정주라는 곳이라 한즉
그러면 아무개씨(氏) 고향이란다.
그러면 아무개씨(氏)를 아느냐 한즉
의원은 빙긋이 웃음을 띠고
막역지간(莫逆之間)이라며 수염을 쓸는다.
나는 아버지로 섬기는 이라 한즉
의원은 또다시 넌즈시 웃고
말없이 팔을 잡아 맥을 보는데
손길은 따스하고 부드러워
고향도 아버지도 아버지의 친구도 다 있었다.
'''
nunMul = '''눈물
        김현승
더러는
옥토(沃土)에 떨어지는 작은 생명이고저…….
흠도 티도,
금가지 않은
나의 전체는 오직 이뿐!
더욱 값진 것으로
드리라 하올 제,
나의 가장 나아종 지닌 것도 오직 이뿐.
아름다운 나무의 꽃이 시듦을 보시고
열매를 맺게 하신 당신은
나의 웃음을 만드신 후에
새로이 눈물을 지어 주시다.
'''
maUm = '''마음
        김광섭
나의 마음은 고요한 물결
바람이 불어도 흔들리고
구름이 지나가도 그림자 지는 곳.
돌을 던지는 사람
고기를 낚는 사람
노래를 부르는 사람
이리하여, 이 물가 외로운 밤이면
별은 고요히 물 위에 뜨고
숲은 말없이 물결을 재우나니
행여 백조가 오는 날
이 물가 어지러울까
나는 밤마다 꿈을 덮노라.
'''
mokSum = '''목숨
        김남조
아직 목숨을 목숨이라고 할 수 있는가
꼭 눈을 뽑힌 것처럼 불쌍한
사람과 가축과 신작로와 정든 장독까지
누구 가랑잎 아닌 사람이 없고
누구 살고 싶지 않은 사람이 없고
불붙은 서울에서
금방 오무려 연꽃처럼 죽어갈 지구를 붙잡고
살면서 배운 가장 욕심없는
기도를 올렸습니다.
반만년 유구한 세월에
가슴 틀어박고 매아미처럼 목태우다 태우다
끝내 헛되이 숨져간 이건
그 모두 하늘이 낸 선천(先天)의 벌족(罰族)이더라도
돌멩이처럼 어느 산야에고 굴러
그래도 죽지만 않는
그러한 목숨을 갖고 싶었습니다.
'''

myPoetryBook = [sanYuHwa.split('\n'), goHyang.split(
    '\n'), nunMul.split('\n'), maUm.split('\n'), mokSum.split('\n')]
title = "시 감상 프로그램"
contents = ['산유화', '고향', '눈물', '마음', '목숨']
printMenu(title, contents)
menuNumber = getMenuNumber(contents)
isExitMenuNumber(menuNumber, contents)
while menuNumber != '6':
    printPoetry(myPoetryBook[int(menuNumber)-1])
    printMenu(title, contents)
    menuNumber = getMenuNumber(contents)
