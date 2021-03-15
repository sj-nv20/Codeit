print("Hello world!")
print("Hello Codeit")
print(2+5)
print(2*5)

# 코멘트(주석) - 프로그램이 실행될 때 무시됨 / 복잡한 코드 설명,하다가 만 부분 표시
print("Goodbye World")  # 이것도 코멘트

# 프로그래밍이란? 계산할 수식들을 컴퓨터에게 알려주는 것

# 프로그래밍의 기본 자료형 (Data Type)
# 정수(Integer) : -1, -2, -3, 0, 1, 2, 3
# 소수(Floating Point) : 3.14, -7.3, 2.0
# 문자열(String) : "Hello", "2" 따옴표안에 있는 것들
# 문자를 계산한다 => "Hello" + "World" = HelloWorld
# 정수 2 소수 2.0 문자열 "2"는 다 다른 타입 => 문자열 "2" + "5" = "25"
# 불린(Boolean) : 참과 거짓을 나타냄 (True / False) - 값들을 비교할 때

# 추상화(Abstraction) : 복잡한 내용은 숨기고, 주요 기능에만 신경쓰자!
# 프로그래밍에서의 추상화 3단계
# 변수(Variable) : 값을 저장하는 것
x = 254
y = 317
print(x + y)    #571

# 변수 사용 장점 : 1. 한눈에 알아보고 이해하기 쉽다(변수명 잘 정하기), 2. 코드 수정이 편하다
# 변수 사용 예 : 버거주문하기
burger_price = 4750     #변수값을 변수에 지정
fries_price = 1490
drink_price = 1250

print(burger_price)
print(burger_price * 2)
print(burger_price + fries_price)
print(burger_price * 3 + fries_price * 2 + drink_price * 5)

#-----------------------------------------------------------------------
# 함수 (Function) : 명령을 저장하는 것
# pirnt함수
burger_price = 4990
print(burger_price)     #print()함수 - 기본 제공되는 함수[내장함수-개발자들이 미리 구현]
def hello():            #직접 함수 정의 def - 함수정의 첫줄 완성(함수의 헤더)
    print("Hello")      #들여쓰기 후 함수 내용 작성 (자동으로 들여쓰기가 된다)
    print("Welcome to Codeit!")

hello()                 #함수 호출 - 함수 내용이 출력됨
hello()                 #호출 할 때 마다 똑같이 출력됨

#파라미터 : 함수에 넘겨 주는 값
#함수 호출 할 때 마다 다르게 출력하고 싶으면 파라미터 사용
#어떤 파라미터를 넘겨주냐에 따라 함수를 조금식 다르게 호출 가능
def hello(name):            #name이라는 파라미터 사용 - 함수 내에서 name이 사용 가능해짐
    print("hello")
    print(name)
    print("Welcom to Codeit")

hello("Michael")            #()안 문자열이 name이라는 파라미터 안으로 들어감
hello("Chris")

#한 함수에 여러개의 파라미터 전달 가능
#파라미터 이름은 원하는대로 지으면 된다
def print_sum(a, b):
    print(a + b)

print_sum(7, 3)     #a에7이 b에3이 전달

#return : 돌려준다
def get_square(x):      #3이라는 값을 x에 전달받음
    return x * x        #3*3을 연산 후 get_square(3)에 결과값을 돌려줌
print(get_square(3))    #3을 x에 전달 후 return으로 결과값(9)을 전달받은 후 출력

def get_square(x):
    return x * x
print(get_square(3) + get_square(4))    #9+16 = 25출력

# 객체 (Object)