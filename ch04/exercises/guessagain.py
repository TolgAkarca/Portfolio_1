import random
randomnumber = int(random.randrange(1,1001))

print("Lets play a game !! ")
print("We gonna play NUMBER GUESS !!")
print("Number gonna between 1 and 1000 (inclusive)")

usertries = 0 

while True :
    userguess = int(input("Please enter a number !!!"))
    if userguess == randomnumber :
        print (f"Good Job !!! You find number in {usertries} tries ")
        break
    
    elif userguess != randomnumber :
        usertries += 1
        print("Keep Trying !!!") 
        if userguess > randomnumber:
            print ("Too high!!")        
        if userguess < randomnumber : 
            print ("Too low !!")

    