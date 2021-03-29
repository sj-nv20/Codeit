my_family = {
    '엄마':'김자옥',
    '아빠':'이석진',
    '아들':'이동민',
    '딸':'이지영'
}

#값의 목록 출력
print(my_family.values())   #dict_values(['김자옥', '이석진', '이동민', '이지영'])

#이지영이라는 값이 목록에 있는지 확인
print('이지영' in my_family.values())  #True
print('성태호' in my_family.values())  #False

#for문 이용해서 값 출력
for value in my_family.values():
    print(value)
'''
김자옥
이석진
이동민
이지영
'''

#키의 목록 출력
print(my_family.keys())     #dict_keys(['엄마', '아빠', '아들', '딸'])

#for문 이용해서 키 출력
for key in my_family.keys():
    print(key)
'''
엄마
아빠
아들
딸
'''

#for문 이용해서 키와 값 출력
for key in my_family.keys():
    value = my_family[key]
    print(key, value)
'''
엄마 김자옥
아빠 이석진
아들 이동민
딸 이지영
'''

#위 식을 좀 더 쉽게 쓰기
for key, value in my_family.items():
    print(key,value)