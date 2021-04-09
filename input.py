#input - 사용자 입력을 받는다

name = input("이름을 입력하세요 : ")
print(name)

# input은 항상 문자열을 입력받기 때문에 정수와의 연산이 불가능하다
x = input("숫자를 입력하세요: ")    #오류발생
print(x + 5)

# 위의 식을 실행시키기 위해서는 input을 int형으로 지정해주자
x = int(input("숫자를 입력하세요: "))
print(x + 5)