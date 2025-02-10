def func(food): #매개변수를 리스트로 받아서 처리 가능
    for x in food:
        print(x)
    food.append("strw")
    food.append("wtml")

# func(["사과","오렌지","바나나"])
fruits=["사과","오렌지","바나나"]
# func(fruits) # add strw 

print(fruits) 
func(fruits) # add strw 
print(fruits) # added strw print # ㄴㄴ함수에서 append 반영되어 출력