#모듈 - 기능들을 정리해둔 파이썬 프로그램 / 다른 파이썬 파일에서 사용할 수 있는 파일
#calculator.py 파일을 모듈이라고 부름
#같은 위치에 있는 파일만 불러 올 수 있음
import calculator

print(calculator.add(2, 5))             #7
print(calculator.multiply(3, 4))        #12

import calculator as calc   #calculator 대신 calc를 사용하겠다는 의미
print(calc.divide(10, 5))               #2.0


from calculator import add, multiply    #calculator파일에서 add, multiply만 가져오겠다는 의미
print(add(2, 5))                        #앞에 모듈이름을 붙이지 않아도 사용 가능 / 7
print(multiply(3, 4))                   #12

from calculator import *        #모듈에서 모든 함수를 불러오는 것(권장x)
print(add(3, 2))                        #5
print(multiply(5, 2))                   #10
