#구구단 프로그램

#구구단 프로그램을 while문이 아닌 for문을 사용해서 만들어 보세요.
#코드를 실행하면, 아래와 같이 출력되어야 합니다.

for i in range(1,10) :
    for j in range(1,10):
        print("{} * {} = {}".format(i,j,i*j))