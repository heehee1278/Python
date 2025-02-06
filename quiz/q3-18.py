start=int(input("시작 수는?"))
end=int(input("끝 수는?"))
N=int(input("정수를 입력하세요"))

# if start < N < end :
if start < N and N< end :
    result="사이에 있다"
else:
    result="사이에 없다"

print("%d은(는)%d~%d%s"%(N,start,end,result))