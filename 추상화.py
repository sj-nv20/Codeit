#추상화

#변수 제대로 이해하기

#파이썬에서 등호의 의미 - '같다'의 의미X, 지정 연산자 - 오른쪽 값을 왼쪽에 지정
name = "김현승"
x = 7

x = x + 1   # (=) 지정연산자 - 오른쪽 값을 왼쪽에 넣어라는 뜻
print(x)    # 8
x = x - 3
print(x)    # 5

#함수의 실행 순서

def hello() :                       #함수정의 - 호출되면 실행
    print("Hello!")                 #2-1번째
    print("Welcome to Codeit!")     #2-2번째

print("함수 호출 전")        #1번째
hello()                    #2번째 - 함수를 호출하면서 함수 실행
print("함수 호출 후")        #3번째

def square(x) :             #함수정의 - 실행되는 건 아님
    return x * x

print("함수 호출 전")            #1번째
print(square(3) + square(4))   #2번째 - 25
print("함수 호출 후")            #3번째

#return문 제대로 이해하기
#return문 역할? (함수가)값 돌려주기 / 함수 즉시 종료하기

def square(x) :
    return x * x        #9를 돌려줌

print(square(3))        #9


def square_1(x) :
    print("함수 시작")
    return x * x        #9를 돌려주면서 함수를 종료
    print("함수 끝")     #return으로 함수가 끝나 출력되지 않음 - Dead Code(의미 없는 코드)

print(square_1(3))
print("Hello World!")

#return과 print의 차이
def print_square(x) :   #파라미터x의 제곱을 출력해주는 함수
    print(x * x)        #9출력 / 리턴값이 따로 없음

def get_square(x) :     #파라미터x의 제곱을 리턴해주는 함수
    return x * x

print_square(3)         #호출
get_square(3)           #9를 돌려받으나 출력되지는 않음
print(get_square(3))    #9를 돌려받고 9출력
print(print_square(3))  #리턴값이 따로 없으면 None이 리턴됨 / None출력

