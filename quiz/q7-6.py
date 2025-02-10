def hypen(string):
    result=""
    i=0

    while i < len(string):
        if string[i] == " ":
            result+="-"
        else:
            result+=string[i]
        i+=1
    return result
string=input("문자입력:")
print(hypen(string))