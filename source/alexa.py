comment = " "

comment = input("Hello, I am alexa, how can I help you?\n")

weather = ["forecast","weather forecast", "how's the weather today?","rain"]
for s in weather:
    if(comment==s):
        print("Now's degree is 23.c\nThe probability of rain is 35%\nHope you have a nice day!") 
    else:
        continue
