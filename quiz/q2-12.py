price = int(input("책 값은"))
discount =int(input("할인율은"))
ship = int(input("배송료는"))

pay = price - (price * (discount/100)) + ship

# print("책값:",price,"원")
print("책값:%d원" %price)
# print("할인율:",discount,"원")
print("책값:%d원" %discount)
# print("배송료:",ship,"원")
print("책값:%d원" %ship)
print("결제 금액: %.0d원"%pay)

