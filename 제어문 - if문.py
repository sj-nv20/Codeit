#if문
'''
#if문 구조
if 조건 부분 :      #불린 값으로 계산되는 식
    수행 부분       #조건 충족 시 수행되는 명령

#예시
while 다운로드 안 받은 이미지가 있다:
    다음 이미지를 본다
    if 이미지가 png파일이다:
        이미지를 다운로드 받는다
    else:
        print("png가 아닙니다.")
'''
#온도에 따라 자켓고르기
temperature = 16
if temperature <= 10:
    print("자켓을 입는다.")
else:
    print("자켓을 입지 않는다")

#elif - else + if를 합친것
score = 82
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
else:
    print("C")