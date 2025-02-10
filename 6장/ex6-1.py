animals=("토끼","거북이","사자","여우")
print(animals)

numbers=tuple(range(10))
print(numbers)

# 튜플에서 값 변경 불가
# animals[2]=("호랑이") #오류발생
# print(animals)

# numbers=tuple(range(10))
# print(numbers)
n=tuple(range(10,21))
print(n)

print("n[0]=",n[0])
print("n[2:5]=",n[2:5])
print("n[2:]=",n[2:])   
print("n[:5]=",n[:5])   #n[:5]= (10, 11, 12, 13, 14)
print("n[-2]=",n[-2])   #n[-2]= 19
print("n[::-1]=",n[::-1]) #n[::-1]= (20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10)
