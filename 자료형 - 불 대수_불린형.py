#자료형

#불 대수 : 일상적인 논리를 수학적으로 표현한 것
# 일반 수학의 값, 숫자 // 불 대수의 값, 진리값 - True / False 두가지 뿐
# 일반 수학 연산 +, - 등 // 불 대수의 연산 AND, OR, NOT
# 명제 : 참과 거짓이 확실한 문장

# AND연산 : X와 Y가 모두 참일 때만 x AND y가 참
'''
  x       y     xANDy
True    True    True
True    False   False
False   True    False
False   False   False

대한민국의 수도는 서울이다 AND 2는 1보다 크다    => True
대한민국의 수도는 서울이다 AND 2는 1보다 작다    => False
'''
# OR연산 : x와 y중 하나라도 참이면 x OR y는 참
'''
  x       y     xORy
True    True    True
True    False   True
False   True    True
False   False   False

대한민국의 수도는 제주도이다 OR 대한민국의 수도는 서울이다   => True
대한민국의 수도는 제주도이다 OR 대한민국의 수도는 부산이다   => False
'''
# NOT연산 : 참이면 거짓, 거짓이면 참으로 나타냄
'''
  x      NOTx
 True    False
 False   True

NOT 대한민국의 수도는 서울이다  => False
NOT 대한민국의 수도는 부산이다  => True
'''

# 불린 (Boolean)
print("True")   #문자열이지 불린형이 아님
print(True)
print(False)

# 불린 연산
print(True and True)        # True
print(True and False)       # False
print(False or True)        # True
print(False or False)       # False
print(not True)             # False
print(not False)            # True

#명제
print(2>1)      #True
print(2<1)      #False
print(3>=2)     #True
print(2==2)     #True
print(2!=2)     #False

print("Hello"=="Hello")     #True
print("Hello"!="Hello")     #False

print(2>1 and "Hello"=="Hello")     #True

print(not not True)     # not False
print(not not False)    # not True

print(7 == 7 or (4 < 3 and 12 > 10))    #True or False -> True / 괄호안 먼저 계산

x = 3
print(x > 4 or not (x < 2 or x == 3))   #False or False -> False
