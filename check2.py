def checkif2(x):
    if(x==0):
        return False
    else:
        while(x % 2==0):
            x=x/2

    return (x==1)
print(checkif2(8))