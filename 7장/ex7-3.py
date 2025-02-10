def average(*args):
    # print(args) # 튜플형식 출력
    num_args=len(args)
    sum=0
    for i in range(num_args):
        sum+=args[i]
    # print(sum)
    avg=sum/num_args
    # print(avg)
    print("%d과목평균: %.1f"%(num_args,avg))
    
        
average(85,65,56)
average(85,65,56,66,75)