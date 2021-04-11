#파일읽기
## r = read의 약자
with open('data/chicken.txt', 'r') as f:      #읽어드린 파일을 변수f에 저장
    print(type(f))      #<class '_io.TextIOWrapper'>

# 파일 내용 출력하기
with open('chicken.txt', 'r') as f:
    for line in f:          #한 줄씩 순서대로 변수line에 저장
        print(line)

#인코딩 문제 발생 시
with open('data/chicken.txt', 'r', encoding='UTF-8') as f:
    for line in f:
        print(line)

