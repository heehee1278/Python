# for x in range(start, stop, step)
print("-"*30)
print(" 섭씨   화씨")
print("-"*30)

for c in range(-20,31,5):
    f=c*9.0/5.0+32.0
    print("%5d %6.1f"%(c,f)) #%5d = 변수앞에 수 -> 출력 자릿수
    # print("%5d %d"%(c,f)) # %6.1f => %d 강제로 정수로 출력
print("-"*30)