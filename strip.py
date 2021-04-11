# strip = 물자열 앞뒤의 화이트스페이스(" " "\t" "\n")를 없애준다

##문자열 맨앞과 맨뒤의 화이트스페이스가 사라짐
print("      abc  def   ".strip())                      #abc  def
print("     \t      \n      abc   def \n\n\n".strip())  #abc   def


with open('data/chicken.txt', 'r', encoding='UTF-8') as f:
    for line in f:
        print(line.strip())