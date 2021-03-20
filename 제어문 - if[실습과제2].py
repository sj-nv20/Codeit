#while문과 if문을 활용하여, 100 이하의 자연수 중 8의 배수이지만 12의 배수는 아닌 것을 모두 출력하세요.
#예를 들어서 16은 8의 배수이지만 12의 배수가 아니니까 조건에 부합합니다.
#하지만 48은 8의 배수이면서 12의 배수이기도 해서 조건에 부합하지 않습니다.
#실행하면 콘솔에 아래와 같이 출력되어야 합니다.
'''
8
16
32
40
56
64
80
88
'''

i = 1
while i <= 100:
    if i % 8 == 0 and i % 12 != 0:
        print(i)
    i += 1