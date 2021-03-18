#scope(범위) : 변수가 사용 가능한 범위
#로벌켠수 : 변수를 정의한 함수 내에서만 사용 가능
#글로벌변수 : 모든 곳에서 사용 가능
#함수에서 변수를 사용하면, 로컬변수를 먼저 찾고 나서 글로벌 변수를 찾음

# 함수 내에서 x정의
def my_function():
    x = 3
    print(x)    #3 / 로컬 변수 - 함수 내에서 정의한 변수 / 함수 내에서만 사용 가능 / scope가 함수 내

my_function()
#print(x)        #오류 발생 : x라는 이름이 정의 된 적 없다 / 변수x가 유효하지 않음

# 함수 밖에서 x정의
x = 2           #글로벌 변수 - 함수 밖에서 정의한 변수 / 모든곳에서 사용 가능 / scope가 코드 전체
def my_function():
    print(x)    #2

my_function()
print(x)        #2

#함수 내에서도 함수 밖에서도 x정의
x = 2       #글로벌변수
def my_function():
    x = 3           #로컬변수
    print(x)        #3  가장 최근에 지정한 값이 출력

my_function()
print(x)            #2  글로벌변수 값 출력

#파라미터도 로컬 변수
def square(x):
    return x * x

print(square(3))