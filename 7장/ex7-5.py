# def func(n): #리턴값 없을때 none
def func(): #리턴값 없을때 none
    # x=n+5
    # return x
    global x
    x=100 #지역변수 : 함수내에서만
    print(x)

# a=func(10)
# print(a)
# b=func(20)
# print(b)
# func()
# print(x) # 전역변수x가 없어서 오류
x=200
print(x)
func()
print(x)