#자료형

# 3. 형 변환(Type Conversion) : 값을 한 자료형에서 다른 자료형으로 바꾸는 것
print(int(3.8))     #3
print(float(3))     #3.0
print(int("2") + int("5"))      #7
print(float("1.1")+ float("2.5"))   #3.6
print(str(2) + str(5))      #25

age = 7
print("제 나이는 " + age + "살입니다.")     # 오류발생 - age가 정수라서 문자열과 연결불가능
print("제 나이는 " + str(age) + "살입니다.")    #제 나이는 7살 입니다. / age를 문자열로 변환

print(int("Hello World"))   #오류-문자열을 숫자로 바꿀 수 없기때문에