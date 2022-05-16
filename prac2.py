import random
import os

os.system('cls')
print("      가위바위보 프로그램")
print("1.가위 2.바위 3.보 4.종료")

user = 0
user= input("1.가위,2.바위,3.보 중 하나 입력")
com = random.choice(['1','2','3'])
while user not in ['1','2','3']:
    print("메뉴에 있는 번호를 입력하시오")
    user= input("1.가위,2.바위,3.보 중 하나 입력")
    com = random.choice(['1','2','3'])


while user != '4':
    if user == '4':
        print("프로그램 종료")
    elif (user=='1' and com=='3'):
        print("사용자 가위 컴퓨터 보 사용자 승")
    elif (user=='2' and com=='1'):
        print("사용자 바위 컴퓨터 가위 사용자 승")
    elif (user=='3' and com=='2'):
        print("사용자 보 컴퓨터 바위 사용자 승")
    elif (user=='1' and com=='1'):
        print("사용자 가위 컴퓨터 가위 무승부")
    elif (user=='2' and com=='2'):
        print("사용자 바위 컴퓨터 바위 무승부")
    elif (user=='3' and com=='3'):
        print("사용자 보 컴퓨터 보 무승부")
    elif (user=='1' and com=='2'):
        print("사용자 가위 컴퓨터 바위 사용자 패")
    elif (user=='2' and com=='3'):
        print("사용자 바위 컴퓨터 보 사용자 패")
    elif (user=='3' and com=='1'):
        print("사용자 보 컴퓨터 가위 사용자 패")
    user=input("가위,바위,보 중 하나 입력")
    com = random.choice(['1','2','3'])
    while user not in ['1','2','3']:
        print("메뉴에 있는 번호를 입력하시오")
        user= input("1.가위,2.바위,3.보 중 하나 입력")
        com = random.choice(['1','2','3'])

    

