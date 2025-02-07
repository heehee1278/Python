stc=input("문장을 입력해 주세요:")
stc=stc.replace(' ','-') #replace => ("찾을 값", "바꿀 값",[바꿀횟수])

rev = " "
i = len(stc)-1
while i >=0:
    rev+=stc[i]
    i-=1

print(rev)

