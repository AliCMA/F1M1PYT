
import random
people = ["Waldo","Jackson","Ray","Eric","Vaughn","Jesse","Herbert","Robert", "Rodrigo","Elija","Sasha","Nathaniel","Ellie","Allison","Jeremiah", "Paula", "Alisha","Tory","Troy", "Faye"]
random.shuffle(people)
# print(people)
print("Waldo is gevonden op nummer: \n"+str(people.index("Waldo"))+"")

index = 0
for x in people:
    print("op plaats", index, "zit", x)
    if x == "Waldo": 
        break
    index+=1
