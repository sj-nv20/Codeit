#리스트 (list)

numbers = [2, 3, 5, 7, 11, 13]          #리스트의 하나하나의 값들을 리스트의 요소라고 부름
names = ["윤수", "혜린", "태호", "영훈"]

print(numbers)  #[2, 3, 5, 7, 11, 13]
print(names)    #['윤수', '혜린', '태호', '영훈']

# 인덱스 : 요소의 위치 -> 0부터 시작함
# 인덱싱(indexing) : 인덱스를 통해 요소를 받아오는 것
print(names[0])     #윤수
print(names[1])     #혜린
print(numbers[1]+numbers[3])    #10

num_1 = numbers[1]
num_3 = numbers[3]
print(num_1 + num_3)    #10

#print(numbers[6])   #오류 - 인덱스 범위를 벗어남

#Python에는 인덱스가 -(마이너스)까지 있음
print(numbers[-1])      #13
print(numbers[-2])      #11
#print(numbers[-7])      #오류 - 범위를 벗어남

# 리스트 슬라이싱 (list slicing)
print(numbers[0:4])     #[2, 3, 5, 7] / 인덱스 0부터 3까지 자르기
print(numbers[2:])      #[5, 7, 11, 13] / 2부터 끝까지 자르기
print(numbers[:3])      #[2, 3, 5] / 인덱스 2부터 맨앞까지 자르기

#슬라이싱한 리스트를 변수에 넣고 이 변수에서 새로 슬라이싱 가능
new_list = numbers[:3]  # [2, 3, 5]
print(new_list[2])      # [5]

# 인덱스 요소 바꾸기
numbers[0] = 7
print(numbers)  #[7, 3, 5, 7, 11, 13]

numbers[0] = numbers[0] + numbers[1]
print(numbers)      #[10, 3, 5, 7, 11, 13]