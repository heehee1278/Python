member={"name":"황예린","age":"22","email":"yerin@hanmail.net"}
print(member)

score=dict([("국어",80),("영어",90),("수학",100)])
print(score) #리스트, 튜플을 사용해 dict 생성
print(score["국어"]) #Key 사용해 Value 얻기
print(score["영어"])
print(score["수학"])

score["음악"]=70 #없는 key dict에 추가됨
print(score)
score["수학"]=77 #있는 key dict에서 값 변경
print(score)