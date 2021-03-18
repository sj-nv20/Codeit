#상수(constant) - 절대로 바뀌지 않는 값
#대문자로 사용 - 일반변수와 상수를 구분짓기위해 /실수를 하지 않기 위해 - 값을 절대로 바꾸지 않겠다는 의미

PI = 3.14   #원주율 '파이'

# 반지름을 받아서 원의 넓이 계싼
def calculate_area(r):
    return PI * r * r

radius = 4  #반지름
print("반지름이 {}면, 넓이는 {}".format(radius, calculate_area(radius)))

radius = 6
print("반지름이 {}면, 넓이는 {}".format(radius, calculate_area(radius)))

radius = 7
print("반지름이 {}면, 넓이는 {}".format(radius, calculate_area(radius)))

#스타일

'''
버거를 주문할 시에 혜택 차원에서 음료수 및 감자튀김을 받을 수 있다
버거를 주문하면 음료수와 감자튀김은 서비스다
'''
#두 문장은 의미는 같지만 스타일이 다름
#코딩에도 스타일이 있다 : 이해하기 쉬운 코드 = 좋은 스타일을 가진 좋은 코드

#안좋은 코드
print(6.28*4)
print(3.14*4*4)
print(6.28*8)
print(3.14*8*8)

#수정한 코드
PI = 3.14       #원주율(파이)
radius = 4      #반지름
print(2*PI*radius)
print(PI*radius*radius)
radius = 8      #반지름
print(2*PI*radius)
print(PI*radius*radius)
#===========================
#가독성이 좋은 코드 - 화이트스페이스(띄어쓰기,빈줄) 잘 활용
PI = 3.14       #원주율(파이)

radius = 4      #반지름
print(2 * PI * radius)
print(PI * radius * radius)

radius = 8      #반지름
print(2 * PI * radius)
print(PI * radius * radius)
#================================
#각 공식을 함수로 정의 - 이해하기 쉬워짐

PI = 3.14       #원주율(파이)

#반지름이 r인 원의 둘레 계산
def calculate_circumference(r):
    return 2 * PI * r

#반지름이 r인 원의 넓이 계산
def calculate_area(r):
    return PI * r * r

radius = 4      #반지름
print(calculate_circumference(radius))
print(calculate_area(radius))

radius = 8      #반지름
print(calculate_circumference(radius))
print(calculate_area(radius))

#파이썬에서 가장 많이 사용되는 스타일 가이드 - PEP8