#리스트와 문자열
'''
list - 자료형 나열
문자열 - 문자열 나열
'''

# 문자열과 list 비슷한점
# list
alphabet_list = ['A','B','C','D','E','F','G','H','I','J']

## 알파벳 리스트의 인덱싱
print(alphabet_list[0])     #A
print(alphabet_list[1])     #B
print(alphabet_list[4])     #E
print(alphabet_list[-1])    #J

## 알파벳 리스트의 슬라이싱
print(alphabet_list[0:5])   #['A', 'B', 'C', 'D', 'E']
print(alphabet_list[4:])    #['E', 'F', 'G', 'H', 'I', 'J']
print(alphabet_list[:4])    #['A', 'B', 'C', 'D']

## 리스트의 덧셈 연산
list_1 = [1, 2, 3, 4]
list_2 = [5, 6, 7, 8]
list_3 = list_1 + list_2
print(list_3)               #[1, 2, 3, 4, 5, 6, 7, 8]

## 리스트의 길이 재기
my_list = [2, 3, 5, 7, 11]
print(len(my_list))         #5

## 알파벳 리스트의 반복문
alphabets_list = ['C', 'O', 'D', 'E', 'I', 'T']
for alphabet in alphabets_list:
    print(alphabet)

# 문자열
alphabet_string = 'ABCDEFGHIJ'

## 알파벳 문자열의 인덱싱
print(alphabet_string[0])   #A
print(alphabet_string[1])   #B
print(alphabet_string[4])   #E
print(alphabet_string[-1])  #J

## 알파벳 문자열의 슬라이싱
print(alphabet_string[0:5])   #ABCED
print(alphabet_string[4:])    #EFGHIJ
print(alphabet_string[:4])    #ABCD

## 문자열의 덧셈 연산
str_1 = 'Hello'
str_2 = 'World'
str_3 = str_1 + str_2
print(str_3)    #HelloWorld

## 문자열의 길이 재기
my_string = 'Hello World!'
print(len(my_string))       #12

## 알파벳 문자열의 반복문
alphabets_string = 'CODEIT'
for alphabet in alphabets_string:
    print(alphabet)

# 문자열과 list의 차이점 - Mutable (수정 가능) vs. Immutable (수정 불가능)

# list
## 리스트 데이터 바꾸기
numbers = [1, 2, 3, 4]
numbers[0] = 5
print(numbers)      # [5, 2, 3, 4]

# 문자열
## 문자열 데이터 바꾸기
name = 'codeit'
name[0] = 'C'
print(name)     #오류발생 - 문자열은 수정 불가능

name_1 ='codeit' + 'it'       # 문자열을 수정한 것이 아니라 새로운 문자열을 만드는 것이라 오류가 발생하지 않음
print(name_1)
