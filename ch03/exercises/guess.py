import random   
randomnumber = int(random.randrange(1,11))

print("Lets play a game !! ")
print("We gonna play NUMBER GUESS !!")
userguess = int(input("Please enter a number between 1 and 10 \n"))

if userguess > 10 :
    print("Wrong Input")

else :
    if userguess == randomnumber :
        print ("Good Job!!")

    if userguess > randomnumber :
         print ("Too high")
        
    if userguess < randomnumber : 
        print ("Too Low")

