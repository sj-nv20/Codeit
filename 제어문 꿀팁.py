#제어문 꿀팁

#break문
#만약 while문의 조건 부분과 상관 없이 반복문에서 나오고 싶으면, break문을 사용하면 됩니다.

i = 100

while True:
    # i가 23의 배수면 반복문을 끝냄
    if i % 23 == 0:
        break
    i = i + 1

print(i)

#continue문
#현재 진행되고 있는 수행 부분을 중단하고 바로 조건 부분을 확인하고 싶으면 continue문을 쓰면 됩니다.

i = 0

while i < 15:
    i = i + 1

    # i가 홀수면 print(i) 안 하고 바로 조건 부분으로 돌아감
    if i % 2 == 1:
        continue
    print(i)