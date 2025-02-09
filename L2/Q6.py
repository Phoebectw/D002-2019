#L2 Q6: Banana Guessing game

#Step 1: Import necessary modules
import random
#Step 2: Welcome Message
print('''Welcome to the Banana Guessing Game
Dave hid some bananas. Your task is to find out the number of bananas he hid.''')
#Step 3: Choose a random number between 1-100
n = random.randint(1,100)

# define a flag for found/not found and counter on how many trials
found = False
count = 0
#Step 4: Give three chances to the players
while count < 3:
    print ("you now have %d chances" %(3-count))
    guess=int(input("please input your first guess"))
    count=count+1
    if guess==n:
        found=True
        break
    else:
        if guess<n:
            print("your guess is too low")
        if guess>n:
            print("your guess is too high")
#Step 5: Display a message
if found == True:
        print('You got the correct guess in %d trials' % count)
        print('Dave\'s banana are now all yours!')
else:
        print("You failed to find the number of bananas Dave hid! Try again next")
