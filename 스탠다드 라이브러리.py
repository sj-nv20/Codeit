#standard library (표준 라이브러리) - 우리가 쓸만한 기능들이 들어있음

#math모듈
import math
print(math.log10(100))      #2.0
print(math.cos(0))          #1.0
print(math.pi)              #3.141592653589793

#os모듈
import os
print(os.getlogin())        #20929
print(os.getcwd())          #C:\Users\20929\PycharmProjects\Codeit01 파일이 있는 폴더의 경로

#random모듈
import random
print(random.random())      #random값이 나옴

##randint함수
##randint는 두 수 사이의 어떤 랜덤한 정수를 리턴하는 함수입니다.
##randint(a, b)를 하면, a ≤ N ≤ b를 만족하는 어떤 랜덤한 정수 N을 리턴하는 것
import random

print(random.randint(1, 20))
print(random.randint(1, 20))
print(random.randint(1, 20))
print(random.randint(1, 20))
print(random.randint(1, 20))

##uniform 함수
##uniform은 두 수 사이의 랜덤한 소수를 리턴하는 함수입니다.
##randint와 다른 것은 리턴하는 값이 정수가 아니라 소수라는 점
##uniform(a, b)를 하면, a ≤ N ≤ b를 만족하는 어떤 랜덤한 소수 N을 리턴하는 것
import random

print(random.uniform(0, 1))
print(random.uniform(0, 1))
print(random.uniform(0, 1))
print(random.uniform(0, 1))
print(random.uniform(0, 1))

#datetime모듈 - '날짜'와 '시간'을 다루기 위한 다양한 '클래스'를 갖추고 있다
#datetime 값 생성
import datetime
pi_day = datetime.datetime(2020, 3, 14)
print(pi_day)
print(type(pi_day))
'''
2020-03-14 00:00:00
<class 'datetime.datetime'>
'''

#시간 직접 정하기
pi_day = datetime.datetime(2020, 3, 14, 13, 6, 15)
print(pi_day)
print(type(pi_day))
'''
2020-03-14 13:06:15
<class 'datetime.datetime'
'''

#코드 실행한 지금 이 순간의 날짜와 시간 받아오기
today = datetime.datetime.now()
print(today)
print(type(today))
'''
2021-04-08 23:32:42.338582
<class 'datetime.datetime'>
'''

#timedelta - 날짜 간의 차이를 나타내는 타입
today = datetime.datetime.now()
pi_day = datetime.datetime(2020, 3, 14, 13, 6, 15)
print(today - pi_day)
print(type(today - pi_day))
'''
390 days, 10:27:26.455296
<class 'datetime.timedelta'>
'''

#timedelta를 생성해서 datetime값에 더해주기
today = datetime.datetime.now()
my_timedelta = datetime.timedelta(days=5, hours=3, minutes=10, seconds=50)

print(today)
print(today + my_timedelta)
'''
2021-04-08 23:34:22.053700
2021-04-14 02:45:12.053700
'''

#datetime해부하기
#dateteime값에서 연도나 월 같은 값들을 추출
today = datetime.datetime.now()

print(today)
print(today.year)  # 연도
print(today.month)  # 월
print(today.day)  # 일
print(today.hour)  # 시
print(today.minute)  # 분
print(today.second)  # 초
print(today.microsecond)  # 마이크로초
'''
2021
4
8
23
35
16
123908
'''

#datetime 포맷팅
#strftime사용해서 출력하기
today = datetime.datetime.now()

print(today)
print(today.strftime("%A, %B %dth %Y"))     #%A, %B, %d, %Y => 포맷 코드
'''
2021-04-08 23:35:47.234465
Thursday, April 08th 2021
'''
