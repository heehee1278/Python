# number = [7,9,15,18,30,-3,7,12,-16,-12]
# sum=0
# for number in number:
#     sum+=number

# print("합계 :",sum)
number = [7,9,15,18,30,-3,7,12,-16,-12]
sum=0
i=0
print("짝수 번째 요소:",end=" ")
while i < len(number):
    if(i+1)%2==0:
        sum+=number[i]
        print(number[i],end=" ")
    i+=1
print()
print("합계 :",sum)
