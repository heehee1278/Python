# def sub(a,b):
#     return a-b
# result=sub(a=7, b=3)
# print(result)

# def add_many(*args):
#     result=0
#     for i in args:
#         result+=i
#     return result
# result=add_many(1,2,3,4,5,6,7,8,9,10)
# print(result)

def add_mul(choice,*args):
    if choice =="add":
        result=0
        for i in args:
            result+=i
    elif choice == "mul":
        result=1
        for i in args:
            result*=i
    return result
result=add_mul('add', 1,2,3,4,5)
print(result)