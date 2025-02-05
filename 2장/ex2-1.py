# input("당신의 이름은?")
name = input("당신의 이름은?")
# birth = input("당신의 태어난 해는?") #숫자를 입력해도 문자로 받음
birth = int(input("당신의 태어난 해는?")) #birth를 정수로 변환

age = 2025 - birth #error 'int' and 'str' => int로 변환 해결
# print("%d님" %name) error
# print("%s님" %name) s : 문자열을 받음
# print("%s님이 태어난 해는 %d" %(name,birth)) error not str
# print("%s님이 태어난 해는 %s" %(name,birth)) 
print("%s님의 나이는 %s세 입니다." %(name,age)) 