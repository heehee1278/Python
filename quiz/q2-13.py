tel1 = input("하이픈(-)이 포함된 11자리의 휴대폰 번호는?")
tel2 = tel1[0:3]+tel1[4:8]+tel1[9:]
print("- 입력된 휴대폰 번호:%s"%tel1)
print("- 하이픈 삭제된 휴대폰 번호:%s"%tel2)