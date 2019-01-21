

def num(X,N,n):
    #print(pow(n,N))
    if(pow(n,N)<X):
        return num(X,N,n+1)+num(X-pow(n,N),N,n+1)
    elif(pow(n,N)==X):
        return 1;
    else:
        return 0;


x=int(input("enter the value of X = "))
y = int(input("enter the value of N = "))
#print(type(x),type(y))
print(num(x,y,1))
