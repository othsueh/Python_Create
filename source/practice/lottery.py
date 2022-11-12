from random import sample as sp 

list1 = sp(range(1,50),7)
special = list1.pop()

list1.sort()
print("Lottery numbers of this time are: ",end="")
for s in list1:
    if(s==max(list1)):
        print("%d"%(s))
    else:
        print("%d"%(s),end=", ")
print("Special number is: %d"%(special))