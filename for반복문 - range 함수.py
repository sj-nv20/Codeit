#range 함수 - 파라미터를 1~3개 쓰는 버전이 있음
#range 함수 장점 - 간편 / 깔끔 / 메모리 효율성(1쓰고 버리고 2쓰고 버기로 등)

for i in [1,2,3,4,5,6,7,8,9,10] :
    print(i)

# 파라미터 1개 버전
'''
for i in range(stop) :              #0부터stop-1까지의 범위
    print(i)
'''
for i in range(10):                 #0부터 9까지 범위
    print(i)                        # 0 1 2 3 4 5 6 7 8 9
# 파라미터 2개 버전
'''
for i in range(start, stop):        #strat부터 stop-1까지의 범위
    print(i)
'''
for i in range(3,11) :              #3부터 10까지 범위
    print(i)                        # 3 4 5 6 7 8 9 10

#파라미터 3개 버전
'''
for i in range(start, stop, step) : #start부터 stop-1까지의 범위, 간격 step
    print(i)
'''
for i in range(3, 17, 3):           #3부터 16까지의 범위, 간격 +3
    print(i)                        # 3 6 9 12 15