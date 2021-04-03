#Aliasing

x = 5
y = x
y = 3
print(x)        # 5
print(y)        # 3

# y는 x의 가명(Alias) - y와x는 이름은 다르지만 같은 값임을 의미
x = [2, 3, 5, 7, 11]
y = x           # 변수 y는 변수 x가 가리키는 곳을 함께 가리키게 된다
y[2] = 4
print(x)        # [2, 3, 4, 7, 11]
print(y)        # [2, 3, 4, 7, 11]

x = [2, 3, 5, 7, 11]
y = list(x)     # 리스트x를 y에 복사 / y는 x의 alias가 아님
y[2] = 4
print(x)        # [2, 3, 5, 7, 11]
print(y)        # [2, 3, 4, 7, 11]