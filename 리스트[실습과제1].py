#리스트[실습과제1]

greetings = ["안녕", "니하오", "곤니찌와", "올라", "싸와디캅", "헬로", "봉주르"]

#greetings 리스트의 원소를 모두 출력하는 프로그램을 작성해 보세요.
#while문과 리스트의 개념을 활용하시면 됩니다.
#출력하면 아래와 같은 결과물이 나와야 합니다.

# 내 답안
i = 0
while i <= 6:
    print(greetings[i])
    i += 1

# 모범답안
i = 0
while i < len(greetings):
    print(greetings[i])
    i += 1