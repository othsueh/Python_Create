from random import randint as ri 
string = " "

while(string != ""):
    string = input()
    if(string ==""):
        print("Game over")
        break
    else:
        print("The dice you roll is: %d"%(ri(1,7)))
