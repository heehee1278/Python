def square(num):
    list_new=[]

    for i in range(1,num+1):
        list_new.append(i**2)
    
    return list_new

n=int(input("n값 입력"))
list1=square(n)
print(list1)