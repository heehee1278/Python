def kilotomile():
    result=kilo*0.621371
    return result

kilo=int(input("킬로미터를 입력하세요 : "))
mile=kilotomile()
print("%d 킬로미터는 %.2f 마일이다."%(kilo,mile))