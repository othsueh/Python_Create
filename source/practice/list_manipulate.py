list1 = []
inum = 0

while(inum != -1):
    inum = int(input("Please input the number: "))
    list1.append(inum)
list1.pop()
print("The length of input numbers is %d\n"%(len(list1)))
print("The sum of input number is %d\n"%(sum(list1)))
print("The max number in the input numbers is %d"%(max(list1)))
print("The mini number in the input numbers is %d"%(min(list1)))
print("The sort of the input numbers are: {}".format(sorted(list1,reverse=True)))
