class Calculator:
    def __init__(self):
        self.value = 0
    def add(self,val):
        self.value += val
class maxLimitCalculator(Calculator):
    def add(self,val):
        self.value += val
        if self.value > 100:
            self.value = 100

cal = maxLimitCalculator()
cal.add(100)
cal.add(7)

print(cal.value)

