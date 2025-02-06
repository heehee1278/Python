# n1=int(input("첫 번째 숫자를 입력하세요."))
# n2=int(input("두 번째 숫자를 입력하세요."))
# print("원하는 연산은?")
# x=input("+,-,*,/중 하나를 선택하세요")

# if x=="+":
#     print("%d+%d=%d"(n1,n2,n1+n2))
# elif x=="-":
#     print("%d-%d=%d"(n1,n2,n1-n2))
# elif x=="*":
#     print("%d*%d=%d"(n1,n2,n1*n2))
# elif x=="/":
#     print("%d/%d=%.2f"(n1,n2,n1/n2))
# else:
#     print("오류")


# function=input("기능 선택")
# function1="1. 더하기"
# function1="2. 빼기"
# function1="3. 곱하기"
# function1="4. 나누기"


# calculatorFunction=input("계산기 기능을 선택하세요(1/2/3/4) : ")
# n1=int(input("첫 번째 숫자를 입력하세요 : "))
# n2=int(input("두 번째 숫자를 입력하세요 : "))

# if function1=="1":
#     result=n1+n2

# elif function1=="2":
#     result=n1-n2

# elif function1=="3":
#     result=n1*n2

# elif function1=="4":
#     result=n1/n2

print("기능선택")
print("1. 더하기")
print("2. 빼기")
print("3. 곱하기")
print("4. 나누기")

x=input("계산기 기능을 선택하세요(1/2/3/4)")
n1=int(input("첫 번째 숫자를 입력하세요 : "))
n2=int(input("두 번째 숫자를 입력하세요 : "))

if x=="1":
    print("%d+%d=%d"%(n1,n2,n1+n2))
elif x=="2":
    print("%d-%d=%d"%(n1,n2,n1-n2))
elif x=="3":
    print("%d*%d=%d"%(n1,n2,n1*n2))
elif x=="4":
    print("%d/%d=%.2f"%(n1,n2,n1/n2))
else:
    print("오류")