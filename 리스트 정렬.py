#리스트 정렬

numbers = [19, 13, 2, 5, 3, 11, 7, 17]

# sorted - 기존 리스트는 건드리지 않고, 정렬된 새로운 리스트를 리턴
new_list = sorted(numbers)
print(new_list)         #[2, 3, 5, 7, 11, 13, 17, 19]

new_list = sorted(numbers, reverse=True)    #거꾸로 정렬
print(new_list)         #[19, 17, 13, 11, 7, 5, 3, 2]
print(numbers)          #[19, 13, 2, 5, 3, 11, 7, 17]

# sort - 아무것도 리턴하지 않고, 기존 리스트를 정렬
print(numbers.sort())   #None
numbers.sort()
print(numbers)          #[2, 3, 5, 7, 11, 13, 17, 19]

numbers.sort(reverse=True)      #[19, 17, 13, 11, 7, 5, 3, 2]
print(numbers)

