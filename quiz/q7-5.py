def reverse(string):
    result=""
    index=len(string)

    while index >0:
        result+=string[index-1]
        index-=1

    return result

string=input("문자입력:")
print(reverse(string))
