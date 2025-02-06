# num1 = int(input("첫 번째 숫자를 입력하세요 : "))
# num2 = int(input("두 번째 숫자를 입력하세요 : "))
# num3 = (num1+num2)/3
# if num3/3 ==0:
#     result = "3의 배수이다"

# else:
#     result = "3의 배수가 아니다"

# print("%d은(는)%s"%(num3,result))


num1 = int(input("첫 번째 숫자를 입력하세요 : "))
num2 = int(input("두 번째 숫자를 입력하세요 : "))
num3 = num1+num2
print("%d+%d=%d"%(num1,num2,num3))

if num3%3==0:
    print("%d은(는)3의 배수이다."%num3)
else:
    print("%d은(는)3의 배수가아니다."%num3)