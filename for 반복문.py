#for 반복문
#while반복문과 다르게 조건부문이 없음
#상황에 따라 판단 후 for문과 while문 중 골라서 사용하기

#for문
my_list = [2,3,5,7,11]

for number in my_list:      #number은 우리가 지정해준 변수라 바꿔도 상관없음
    print(number)           #수행부문  / 2,3,5,7,11출력

#===========================================================================
#while문
my_list = [2,3,5,7,11]

i = 0
while i <len(my_list):
    print(my_list[i])
    i += 1


