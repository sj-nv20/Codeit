#주민등록번호 가리기

'''
주민등록번호 YYMMDD-abcdefg는 총 열세 자리인데요.

앞의 여섯 자리 YYMMDD는 생년월일을 의미합니다.

YY → 연
MM → 월
DD → 일
뒤의 일곱 자리 abcdefg는 살짝 복잡합니다.

a → 성별
bc → 출생등록지에 해당하는 지방자치단체의 고유번호
defg → 임의의 번호
보시다시피 많은 부분은 특정 규칙대로 정해져 있는데요.
여러분에 대한 몇 가지 정보만 알면, 마지막 네 개 숫자 defg를 제외한 앞의 아홉 자리는 쉽게 알 수 있다는 거죠.

그래서 저희는 주민등록번호의 마지막 네 자리 defg만 가려 주는 보안 프로그램을 만들려고 합니다.

mask_security_number라는 함수를 정의하려고 하는데요.
이 함수는 파라미터로 문자열 security_number를 받고,
security_number의 마지막 네 글자를 '*'로 대체한 새 문자열을 리턴합니다.

참고로 파라미터 security_number에는 작대기 기호(-)가 포함될 수도 있고, 포함되지 않을 수도 있는데요.
작대기 포함 여부와 상관 없이, 마지막 네 글자가 '*'로 대체되어야 합니다!
'''

def mask_security_number(security_number):
    if len(security_number) == 13:
        number = security_number[0:9]
    else:
        number = security_number[0:10]
    star = "****"
    return number + star


# 테스트
print(mask_security_number("880720-1234567"))
print(mask_security_number("8807201234567"))
print(mask_security_number("930124-7654321"))
print(mask_security_number("9301247654321"))
print(mask_security_number("761214-2357111"))
print(mask_security_number("7612142357111"))

#모범답안
def mask_security_number(security_number):
    return security_number[:-4] + '****'


# 테스트
print(mask_security_number("880720-1234567"))
print(mask_security_number("8807201234567"))
print(mask_security_number("930124-7654321"))
print(mask_security_number("9301247654321"))
print(mask_security_number("761214-2357111"))
print(mask_security_number("7612142357111"))