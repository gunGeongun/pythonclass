name = input("이름을 입력하시오 : ")
mykg = int(input("몸무게를 입력하시오 : "))
goldcurrent=75316.27
goldkg= mykg*266.66
goldmoney=goldkg*goldcurrent
print(f"{name}님 안녕하세요 !")
print(f"{name}님 몸무게는 {mykg}kg입니다.")
print(f"오늘의 금시세는 1g 당 {goldcurrent}원 입니다.")
print(f"{name}님의 몸무게를 금으로 환산하면 {goldkg}돈 입니다.")
print(f"{name}님의 몸무게를 금값으로 환산하면 {goldmoney:.0f}원 입니다.") #원 소수점을 없애고 첫째자리에서 반올림


#금값 75316.27원/ g 2022-03-21 기준
#순금 1돈 무게 = 3.75g
# 1kg = 266.66돈 
#266.66 * kg = 몇 돈
# 몇 돈 * 75316.27 = 금 값 환산치



#몸무게를 금값으로 이름:    몸무게: kg을 돈으로 치환      오늘의 금시세:      이름님! ~원 입니다.  3자리~4자리씩 나눠서 출력