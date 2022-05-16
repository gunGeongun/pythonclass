import sys,os
def calculator():
    os.system('cls')
    print('\t\t내가 만든 계산기')
    print('1.더하기 2.빼기 3.곱하기 4.나누기 5.종료')
    menuNumber=input('원하는 메뉴를 선택하시오 : ')
    while menuNumber not in '12345':
        print("에러")
        menuNumber=input('원하는 메뉴를 선택하시오 : ')
    while menuNumber!='5':
        strOperand1=input('첫번째 숫자:')
        while not strOperand1.isdigit():
            print("숫자가 아니다.")
        strOperand1=int(input('첫번째 숫자:'))
        strOperand2=input('두번째 숫자:')
        while not strOperand2.isdigit():
            print("숫자가 아니다.")
        strOperand2=int(input('두번째 숫자:'))
        
        if menuNumber =='1':
            print(f'{strOperand1}+{strOperand2} ={strOperand1+strOperand2}')
        elif menuNumber =='2':
            print(f'{strOperand1}-{strOperand2} ={strOperand1-strOperand2}')
        elif menuNumber =='3':
            print(f'{strOperand1}*{strOperand2} ={strOperand1*strOperand2}')
        elif menuNumber =='4':
            print(f'{strOperand1}/{strOperand2} ={strOperand1/strOperand2}')
        
if len(sys.argv)==1:
    calculator()
elif len(sys.argv)==2:
    if sys.argv[1]=='/?' or sys.argv[1]=='/h':
        "rr"
    else:
        print("에러")
elif len(sys.argv)==3:
    if sys.argv[1].isdigit():
        intOperand1 = int(sys.argv[1])
    else:
        print("error")
    if sys.argv[2].isdigit():
        intOperand2 = int(sys.argv[2])
    else:
        print("error2")
elif len(sys.argv)>3:
    print("에러")


