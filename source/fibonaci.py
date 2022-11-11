def fibonaci(n):
    if(n==1 or n==2):
         return 1
    elif(n==0):
        return 0
    else:
        return fibonaci(n-1) + fibonaci(n-2) 

a = int(input("The recurve: "))
a = fibonaci(a)
print("The fibonaci: %d"%(a))