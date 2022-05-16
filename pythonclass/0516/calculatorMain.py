from calculator import *
from Menu2 import *

title = "내가 만든 계산기"
contents = ['더하기','빼기','곱하기','나누기','더하기2']
myMenu=Menu(title,contents)
myMenu.print()
menuNumber=myMenu.getMenuNumber()
while not myMenu.isExit(menuNumber):
    op1 = Calculator('첫 번째 숫자를 입력하시오 :')
    op2 = Calculator('두 번째 숫자를 입력하시오 :')
    if menuNumber ==1:
        print(op1.Plus(op2))
    elif menuNumber ==2:
        print(op1.Minus(op2))
    else:
        print('\t\t waiting')
    input()
    myMenu=Menu(title,contents)
    menuNumber=myMenu.getMenuNumber()  

print()
print("다음에 또 봅시다")
