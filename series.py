num=int(input("enter a number"))
for i in range(1,11):
    sum=i*num
    mod=sum%10
    div=sum/10
    res=int(mod+div)
    if(int(res)>10):
        mod1=int(res%10)
        div1=int(res/10)
        res1=mod1+div1
        print(res1)
    else:
        print(res)

