
def table3(num, i, temp):
    num=int(num)
    i=int(i)
    temp=int(temp)
    if(i!= num):
        temp += 3
        i=str(i)
        temp=str(temp)
        print("3 x " + i + ": " + temp)
        i = int(i)
        i += 1
        table3(num,i,temp)


totalnum=int(input("Enter the total no. of time where 3 has to be multiplied"))
totalnum+=1
totalnum=str(totalnum)
table3(totalnum,1,0)
