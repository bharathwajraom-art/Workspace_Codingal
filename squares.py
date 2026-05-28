def getsquarenums():
    while True:
        try:
            num1=int(input("enter beginning number: "))
            num2=int(input("enter ending number: "))
            if num1>num2:
                print("error: beginning number should be less than or equal to ending number")
                continue
            break
        except ValueError:
            print ("error: invalde input please enter integers")
    evensqr=[]
    oddsqr=[]
    for i in range(num1,num2+1):
        sqr=i*i
        if sqr%2==0:
            evensqr.append(sqr)
        else:
            oddsqr.append(sqr)
    print(f"result for range {num1} to {num2}:")
    print(f"even sqr list: {evensqr}")
    print(f"odd sqr list: {oddsqr}")
getsquarenums()
