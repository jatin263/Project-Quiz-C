def exp(x,y):
    if y==1:
        return x
    else:
        return x*exp(x,y-1)
    
print(exp(2,4))