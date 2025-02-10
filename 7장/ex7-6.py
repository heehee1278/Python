def cir_area():
    result=r*r*3.14
    return result
def cir_length():
    result=2*r*3.14
    return result

# r=10
r=int(input("반지름을 입력하세요"))
area=cir_area()
# area=cir_area(r) #TypeError: cir_area() takes 0 positional arguments but 1 was given
length=cir_length()
print("원의 면적:%.1f, 원주:%.1f"%(area,length))