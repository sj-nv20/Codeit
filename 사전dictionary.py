#사전 (dictionary)
#key-value pair (키-값 쌍)
my_dictionary = {
    5: 25,      #키-값
    2: 4,       #키-값
    3: 9        #키-값
}
print(type(my_dictionary))      #<class 'dict'>

#키를 입력하면 값을 알려줌
print(my_dictionary[3])     #9

#원하는 키에 값 넣기
my_dictionary[9] = 81
print(my_dictionary)        #{5: 25, 2: 4, 3: 9, 9: 81}

#리스트와의 차이점
# 리스트 - 인덱스가 순서대로 0,1,2,3으로 진행 / 인덱스가가정수형이다
# 사전 - 순서 개념 없음 / 사전의 키는 정수형일 필요가 없다.
my_family = {
    '엄마':'김자옥',
    '아빠':'이석진',
    '아들':'이동민',
    '딸':'이지영'
}

print(my_family)             #{'엄마': '김자옥', '아빠': '이석진', '아들': '이동민', '딸': '이지영'}
print(my_family['아빠'])      #이석진