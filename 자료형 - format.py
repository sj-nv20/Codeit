#자료형

# 오늘은 2019년 10월 29일입니다.
year = 2019
month = 10
day = 29
print("오늘은 " + str(year) +"년 "+str(month)+"월 "+str(day)+"일입니다.")    #번거로움

#format메소드
#방법 1
print("오늘은 {}년 {}월 {}일입니다".format(year, month, day))

#방법 2
date_string = "오늘은 {}년 {}월 {}일입니다"
print(date_string.format(year,month,day))
print(date_string.format(year,month,day+1))     #다음날을 출력하고 싶을 경우

#format 다루기
print("저는 {},{},{}를 좋아합니다".format("유재석", "도경수", "이진욱"))     #순서대로 출력
print("저는 {1},{0},{2}를 좋아합니다".format("유재석", "도경수", "이진욱"))  #순서 정해서 출력

num_1 = 1
num_2 = 3
print("{0} 나누기 {1}은 {2}입니다".format(num_1, num_2, num_1/num_2))  #1 나누기 3은 0.3333333333333333입니다
print("{0} 나누기 {1}은 {2:.2f}입니다".format(num_1, num_2, num_1/num_2))  #소수점 둘째자리로 반올림 / 1 나누기 3은 0.33입니다
print("{0} 나누기 {1}은 {2:.0f}입니다".format(num_1, num_2, num_1/num_2))  #정수로 바꾸어주기 / 1 나누기 3은 0입니다

#문자열 포맷팅 하는 방법
#1. 가장 오래된 방식 (%기호) - %s, %d와 같은 '포맷 스트링'이라는 것을 사용
name = "최지웅"
age = 32

print("제 이름은 %s이고 %d살입니다." % (name, age))

#2. 현재 가장 많이 쓰는 방식(format 메소드)
name = "최지웅"
age = 32

print("제 이름은 {}이고 {}살입니다.".format(name, age))

#3. 새로운 방식 (f-string)
name = "최지웅"
age = 32

print(f"제 이름은 {name}이고 {age}살입니다.")