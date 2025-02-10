# def plus():
#     result=first+second
#     return result
# def minus():
#     result=first-second
#     return result
# def double():
#     result=first*second
#     return result
# def div():
#     result=first/second
#     return result


# first=int(input("첫번째 숫자를 입력하세요:"))
# second=int(input("두번째 숫자를 입력하세요:"))
# sym=input("원하는 연산을 선택하세요 1/2/3/4")
# if sym==1:
#     sym=="+"
# elif sym==2:
#     sym=="-"
# elif sym==3:
#     sym=="*"
# elif sym==4:
#     sym=="%"

    
# print("%d %s %d = %d"%(first,sym,second,result))


# sym=input("원하는 연산을 선택하세요(1/2/3/4)")
# first=plus()
# print("%d %s %d = %d"%(first,sym,second))

def plus(x,y):
    return x+y
def plus(x,y):
    return x-y
def plus(x,y):
    return x*y
def plus(x,y):
    return x/y

print("-선택옵션")
print("1.더하기")
print("2.빼기")
print("3.곱하기")
print("4.나누기")

print()
num1=int(input("첫번째 숫자를 입력하세요:"))
num2=int(input("두번째 숫자를 입력하세요:"))
choice=input("원하는 연산을 선택하세요 1/2/3/4")
print()

if choice=="1":
    print(num1,"+",num2,"=".add(num1,num2))
elif choice=="2":
    print(num1,"-",num2,"=",substract(num1,num2))
elif choice=="3":
    print(num1,"*",num2,"=",multi(num1,num2))
elif choice=="4":
    print(num1,"/",num2,"=",div(num1,num2))
