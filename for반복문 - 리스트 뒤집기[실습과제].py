#리스트 뒤집기

#리스트 원소들의 순서를 거꾸로 뒤집으려고 합니다.
#numbers라는 리스트가 주어졌을 때, for문을 사용하여 리스트를 거꾸로 뒤집어 보세요!

numbers = [2, 3, 5, 7, 11, 13, 17, 19]

# 리스트 뒤집기
for left in range(len(numbers) // 2):   #리스트의 반만 돌아도 리스트를 뒤집을 수 있음 - 리스트 길이의 반을 넘게 돌면 위치 다시 원상복구
    # 인덱스 left와 대칭인 인덱스 right 계산
    right = len(numbers) - left - 1

    # 위치 바꾸기
    numbers[right], numbers[left] = numbers[left], numbers[right]

print("뒤집어진 리스트: " + str(numbers))
