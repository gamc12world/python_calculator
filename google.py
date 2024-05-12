def addTwoNumbers(l1, l2):
    self.l1=l1
    self.l2=l2
    x1=""
    x2=""
    for i in l1:
        x1=x1+str(i)
    for i in l2:
        x2=x2+str(i)
    
    x3=int(x2)
    x4=int(x1)
    sum1=str(x3+x4)
    print(sum1.split(","))
    su1=[]
    su2=[]
    for i in str(sum1):
        su1.append(i)
    su1.reverse()
    for i in su1:
        su2.append(int(i))
        print(int(i))
    return su2
    pass

addTwoNumbers([2,4,3],[5,6,4])