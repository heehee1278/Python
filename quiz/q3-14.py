n=int(input("숫자를 입력하세요 :"))
if n >= 0 and n <=9 :
    print("한자리 숫자")
elif n >= 10 and n <=99 :
    print("두자리 숫자")

elif n >= 100 and n <=999 :
    print("세자리 숫자")

else:
    print("오류")

    

