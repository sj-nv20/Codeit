#자료형

#type = 어떤 자료형인지 확인 가능한 함수
print(type(3))      #<class 'int'>
print(type(3.0))    #<class 'float'>
print(type("3"))    #<class 'str'>
print(type("True")) #<class 'str'>
print(type(True))   #<class 'bool'>

def hello():
    print("Hello World!")

print(type(hello))  #<class 'function'> / 함수 또한 하나의 자료형
print(type(print))  #<class 'builtin_function_or_method'> / 내장되어 있는 함수