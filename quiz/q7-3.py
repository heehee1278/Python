def count_char(string,x):
    count=0
    for i in string:
        if i==x:
            count+=1
    return count

test_str=input("영어문장입력:")
char=input("알파벳입력:")
num_char=count_char(test_str,char)

print("%s에 포함된 %s의 개수는 %d 개"%(test_str,char,num_char))
