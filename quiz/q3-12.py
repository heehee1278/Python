# num1 = int(input("양의 정수를 입력하세요 :"))
# if num1%3==0:
#     print("%d은(는) 3의 배수이다"%num1)
# if num1%4==0:
#     print("%d은(는) 4의 배수이다"%num1)
# if num1%4==0 and num1%3==0:
#     print("%d은(는) 3의 배수이면서 4의 배수이다"%num1)
# if num1%4!=0 and num1%3!=0:
#     print("%d은(는) 3의 배수도 4의 배수도 아니다."%num1)


num1 = int(input("양의 정수를 입력하세요 :"))
result="3의 배수도 4의 배수도 아니다."

if num1%3==0:
    result="3의 배수이다."
if num1%4==0:
    result="4의 배수이다."
if num1%4==0 and num1%3==0:
    result="3의 배수이면서 4의 배수이다."

print("%d은(는) %s"%(num1,result))

