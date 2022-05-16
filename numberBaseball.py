# 숫자야구 프로그램 1926005 2학년 김건 5주차과제
from random import randint


def addNumbers():
    numbers = []
    while len(numbers) < 3:
        addNumber = randint(0, 9)
        if addNumber not in numbers:
            numbers.append(addNumber)
    print("0~9 범위의 서로 다른 숫자 3개를 랜덤순서로 뽑았습니다.")
    return numbers


def userInput():
    newInput = []
    while len(newInput) < 3:
        num = int(input("{}번째 수를 입력하세요: ".format(len(newInput) + 1)))
        if num < 0 or num > 9:
            print("0에서 9까지의 수를 입력해 주세요!")
        elif num in newInput:
            print("중복되는 숫자입니다. 다시 입력하세요.")
        else:
            newInput.append(num)

    return newInput


def get_score(predict, solution):
    strike_count = 0
    ball_count = 0
    for i in range(3):
        if predict[i] == solution[i]:
            strike_count += 1
        elif predict[i] in solution:
            ball_count += 1

    return strike_count, ball_count


result = addNumbers()
userTry = 0

while True:
    userInputNumber = userInput()
    s, b = get_score(userInputNumber, result)

    print("{}Strike {}Ball\n".format(s, b))
    userTry += 1
    if s == 3:
        break
print("축하합니다. {}번 만에 숫자야구에서 승리하셨습니다!".format(userTry))
