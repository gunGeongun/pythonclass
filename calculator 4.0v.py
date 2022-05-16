#함수를 이용한 계산기 프로그램 1926005 2학년 김건 5주차과제
import sys,os

def Plus(op1,op2):
    return op1+op2
def Minus(op1,op2):
    return op1-op2
def Multiply(op1,op2):
    return op1*op2
def Divide(op1,op2):
    if op2 == 0:
        return '0나누기 x'
    else:
        return op1/op2
def Share(op1,op2):
    if op2 == 0:
        return '0나누기 x'
    else:
        return op1//op2
def Remainder(op1,op2):
    if op2 == 0:
        return '0나누기 x'
    else:
        return op1%op2
def Power(op1,op2): 
    return op1**op2


def printMenu():


    os.system('cls')
    print('\n'*2)
    print('\t\t\t내가 만든 계산기')
    print()
    print('\t\t1.더하기')
    print()
    print('\t\t2.빼기')
    print() 
    print('\t\t3.곱하기')
    print()
    print('\t\t4.나누기')
    print()
    print('\t\t5.몫')
    print()
    print('\t\t6.나머지')
    print()
    print('\t\t7.승')
    print()
    print('\t\t8.종료')
    print()

def getMenuNumber():
    menuNumber=input('\t\t원하는 메뉴를 선택하시오')

    return menuNumber
def getOperand(message):
    operand = input(message)
    while not operand.isdigit():
        if operand.count('.')==1:
            lstOperand=operand.split('.')
        if not lstOperand[0].isdigit():
            print('소숫점 앞이 숫자가아닙니다.')
        elif not lstOperand[1].isdigit():
            print('소숫점 뒤가 숫자가아닙니다.')
        else:
            return float(operand)
        operand = input(message)
    return int(operand)

def numberSign():
    if int(menuNumber)==1:
        return '+'
    elif int(menuNumber)==2:
        return '-'
    elif int(menuNumber)==3:
        return '*'
    elif int(menuNumber)==4:
        return '/'
    elif int(menuNumber)==5:
        return '//'
    elif int(menuNumber)==6:
        return '%'
    elif int(menuNumber)==7:
        return '**'

menuKey={1:Plus,2:Minus,3:Multiply,4:Divide,5:Share,6:Remainder,7:Power}
printMenu()
menuNumber=getMenuNumber()

while not menuNumber=='8':
    operand1 = getOperand('첫 번째 숫자를 입력하시오 :')
    operand2 = getOperand('두 번째 숫자를 입력하시오 :')
    if menuKey[int(menuNumber)]==menuKey.get(int(menuNumber)):
        print(f'{operand1}{numberSign()}{operand2}= {menuKey[int(menuNumber)](operand1,operand2)}')
    input('아무키나 누르세요.')
    printMenu()
    menuNumber=getMenuNumber()

   
