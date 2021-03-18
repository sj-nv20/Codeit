#옵셔널 파라미터
#파라미터에게 '기본값'을 설정할 수 있으며 기본값을 설정해 두면, 함수 호출할 때 꼭 파라미터에ㅔ 값을 안 넘겨줘도 된다.
#필수로 넘겨 줄 필요가 없는 파라미터 - 옵셔널 파라미터

def myself(name, age, nationality = "한국") :
    print("내 이름은 {}".format(name))
    print("나이는 {}살".format(age))
    print("국적은 {}".format(nationality))

myself("코드잇", 1, "미국")  #옵셔널 파라미터를 제공하는 경우
#내 이름은 코드잇
#나이는 1살
#국적은 미국
print()
myself("코드잇",1) #옵셔널 파라미터를 제공하지 않는 경우
#내 이름은 코드잇
#나이는 1살
#국적은 한국

#옵셔널 파라미터는 모두 마지막에 있어야 한다 즉, 일반 파라미터가 옵셔널 파라미터 뒤에 쓰여지면 안된다.
def myself(name, nationality="한국", age):    # 오류 발생
    print("내 이름은 {}".format(name))
    print("나이는 {}살".format(age))
    print("국적은 {}".format(nationality))


myself("코드잇", 1)  # 기본값이 설정된 파라미터를 바꾸지 않을 때
print()
myself("코드잇", "미국", 1)  # 기본값이 설정된 파라미터를 바꾸었을 때