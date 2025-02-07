sum=0 #기본값 0
for i in range(1,11): # 1~10
    # print("안녕하세요!")
    sum+=i
    print("i의 값 : %d=> 합계 : %d"%(i,sum))

# for x in range(start, stop, step)
# sum=0
# for i in range(100,201,5):
#     sum+=i
# print(sum)
# # print("5의 배수의 합계:%d"%sum)

x=1
sum=0
while x < 101:
    sum = sum + x
    x=x+1
print(sum)