Plus = lambda op1, op2: op1 + op2

def divide(op1, op2):
    try:
        op1 / op2
    except ZeroDivisionError:
        return '0나눔 오류입니다.'
    else:
        return op1 / op2

contentsList = [str(i+1) for i in range(len(contents)+1)]
