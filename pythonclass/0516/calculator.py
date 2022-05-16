class Calculator :
    def __init__(self,message) -> None:
        operand=input(f'\t\t{message}')
        while not self.validNumber(operand):
            operand=input(f'\t\t 오류 입력!!{message}숫자 입력:')
    def validNumber(self,operand):
        while not operand.isdigit():
            if operand.count('.')==1:
                list1=operand.split('.')
                if not list1[0].isdigit():
                    print('\t\t소숫점 앞 숫자 x')
                    return False
                elif not list1[1].isdigit():
                    print('\t\t소숫점 앞 숫자 x')
                    return False
                else:
                    self._number=float(operand)
                    return True
            else:
                print("\t\t 소숫점많거나 숫자아님")
                return False




        else:
            self._number=int(operand)
            return True
    @property
    def Number(self):
        return self._number
    def Plus(self,other):
        return f'{self.Number}+{other.Number} = {self.Number + other.Number}'
    def Minus(self,other):
        return f'{self.Number}-{other.Number} = {self.Number - other.Number}'
    def __add__(self,other):
        return f'{self.Number}-{other.Number} = {self.Number - other.Number}'
   
