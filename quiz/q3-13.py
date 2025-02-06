# num1 = input("숫자를 입력하세요")
# result = int(num1[2])
# if result%2==0:
#     print("%d은(는) 짝수이다."%result)
# if result%2==1:
#     print("%d은(는) 홀수이다."%result)


num1 = input("숫자를 입력하세요")
x = int(num1[2])
if x%2==0:
    result="은(는)짝수이다."
else:
    result="은(는)홀수이다."

print("%d%s"%(x,result))