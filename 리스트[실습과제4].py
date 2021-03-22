#리스트 함수를 활용하여 아래의 지시 사항을 따르세요.

# 1.numbers라는 빈 리스트를 만들고 리스트를 출력한다.
# 2.append를 이용해서 numbers에 1, 7, 3, 6, 5, 2, 13, 14를 순서대로 추가한다. 그 후 리스트를 출력한다.
# 3.numbers 리스트의 원소들 중 홀수는 모두 제거한다. 그 후 다시 리스트를 출력한다.
# 4.numbers 리스트의 인덱스 0 자리에 20이라는 수를 삽입한 후 출력한다.
# 5.numbers 리스트를 정렬한 후 출력한다.

# 1
numbers = []
print(numbers)

# 2
numbers.append(1)
numbers.append(7)
numbers.append(3)
numbers.append(6)
numbers.append(5)
numbers.append(2)
numbers.append(13)
numbers.append(14)
print(numbers)

# 3
del numbers[0]
del numbers[0]
del numbers[0]
del numbers[1]
del numbers[2]
print(numbers)

# 3 모범답안
i = 0
while i < len(numbers):
    if numbers[i] % 2 == 1:
        del numbers[i]
    else:
        i += 1
print(numbers)

# 4
numbers.insert(0, 20)
print(numbers)

#5
numbers.sort()
print(numbers)