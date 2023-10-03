import random   
randomnumber = int(random.randrange(1,11))

print("Lets play a game !! ")
print("We gonna play NUMBER GUESS !!")
print("Don't forget you have 3 CHANCES!!")

userchance = 3

for _ in range(userchance):
    userguess = int(input("Please enter a number between 1 and 10 \n"))
    if userguess > 10 :
        print("Wrong Input")

    if userguess == randomnumber :
        print ("Good Job!!")
        break


    else :

        if userguess > randomnumber :
            
            userchance -= 1
            print (f"Too high!! , you have {userchance} chances(s) more")
                
        if userguess < randomnumber : 
            
            userchance -= 1
            print (f"Too low !! , you have {userchance} chance(s) more")

        if userchance == 0 :
             print ("Out of chances sorry !!")
             break 


