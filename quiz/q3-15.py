n=input("문자열을 입력하세요 :")
length = len(n) #바로 정수로 됨
if length%2==0:
    result="짝수이다"
else:
    result="홀수이다"

print("문자열의 개수는 %s"%result)

