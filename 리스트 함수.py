#리스트(list) 함수

# len = 길이 / 리스트 값의 갯수를 출력
numbers = []
print(len(numbers))    #리스트의 요소 갯수를 출력 / 0

# .append - 리스트에 새로운 값을 가장 오른쪽에 추가 [추가연산]
numbers = []
numbers.append(5)
numbers.append(8)
print(numbers)          #[5, 8]
print(len(numbers))     #2

# del - list 요소 삭제
numbers_1 = [2, 3, 5, 7, 11, 13, 17, 19]
del numbers_1[3]        #인덱스 3을 삭제 - 7이 삭제됨
print(numbers_1)        #[2, 3, 5, 11, 13, 17, 19]

# insert - 원하는 위치에 값 삽입 [삽입연산]
numbers_1.insert(4, 37)     #인덱스 4에 37삽입
print(numbers_1)            #[2, 3, 5, 11, 37, 13, 17, 19]