# imports the necessary module
import random

highscore_e = 10
highscore_m = 10
highscore_h = 10

# defines the name of the user and welcomes them to the game
name = input('Please tell me your name: ' ).capitalize()
print('Welcome',name,'to my random number guessing game!\n')

# defines the main function of the code
def start_game(): 
    # sets how many guesses it takes for the user to get the answer
    guesses_e = 0
    guesses_m = 0
    guesses_h = 0

    # sets the highscore for each difficulty
    global highscore_e
    global highscore_m
    global highscore_h
    
    
    # defines the difficulty the user wishes to tackle
    difficulty = input('Please choose your desired difficulty between Easy, Medium, Hard: \n').lower()
    
    # defines the function if the difficulty chosen is easy
    if difficulty in ('easy', 'medium', 'hard'):
        while difficulty == 'easy':
            try:
                number = random.randrange(1,10)
                guess = int(input('Enter a number between 1 and 10: '))  
                if guesses_e == 0:
                    guesses_e += 1
                while guess != number:
                    if guess not in range(1,10):
                        print('Please choose a number between 1 and 10, thank you!\n')
                        start_game()
                    elif guess < number:
                        print('Your guess was too low.')
                        guess = int(input('Enter a number between 1 and 10: '))
                        guesses_e = guesses_e + 1
                    elif guess > number:
                        print('Your guess was too high.')
                        guess = int(input('Enter a number between 1 and 10: '))
                        guesses_e = guesses_e + 1
                print("You got it! It took you {} tries.".format(guesses_e))
                if guesses_e < highscore_e:
                    highscore_e = guesses_e
                break
            except ValueError:
                print('Please guess a number, thank you.') 
                
            
        # defines the function if the difficulty chosen is medium
        while difficulty == 'medium':
            try:
                number = random.randrange(1,50)
                guess = int(input('Enter a number between 1 and 50: '))  
                if guesses_m == 0:
                    guesses_m += 1
                while guess != number:
                    if guess not in range(1,50):
                        print('Please choose a number between 1 and 50, thank you!\n')
                        start_game()
                    elif guess < number:
                        print('Your guess was too low')
                        guess = int(input('Enter a number between 1 and 50: '))
                        guesses_m = guesses_m + 1
                    elif guess > number:
                        print('Your guess was too high.')
                        guess = int(input('Enter a number between 1 and 50: '))
                        guesses_m = guesses_m + 1
                print("You got it! It took you {} tries.".format(guesses_m))
                if guesses_m < highscore_m:
                    highscore_m = guesses_m
                break
            except ValueError:
                print('Please guess a number, thank you.') 
    
            
    
        # defines the function if the difficulty chosen is hard
        while difficulty == 'hard':
            try:
                number = random.randrange(1,100)
                guess = int(input('Enter a number between 1 and 100: '))  
                if guesses_h == 0:
                    guesses_h += 1
                while guess != number:
                    if guess not in range(1,100):
                        print('Please choose a number between 1 and 100, thank you!\n')
                        start_game()
                    elif guess < number:
                        print('Your guess was too low')
                        guess = int(input('Enter a number between 1 and 100: '))
                        guesses_h = guesses_h + 1
                    elif guess > number:
                        print('Your guess was too high.')
                        guess = int(input('Enter a number between 1 and 100: '))
                        guesses_h = guesses_h + 1
                print("You got it! It took you {} tries.".format(guesses_h))
                if guesses_h < highscore_h:
                    highscore_h = guesses_h
                break
            except ValueError:
                print('Please guess a number, thank you.') 
    
        new_game = input("Would you like to play again? yes or no: \n").lower()
        

        

        if new_game.lower() == 'yes':
            print('HIGHSCORE\n Easy:',(highscore_e),
                              'Normal:',(highscore_m),
                              'Hard:',(highscore_h),
                 'NOTE: The score is tallied by the least amount of tries it took to find the answer with the base score starting off at 10. The lower the number, the better you did. Aim for score of 1!\n')
            start_game()
        else:
            print('Thank you',name,'for playing my guessing game! Feel free to come back to play again!')
            quit()
    else:
        print('Please choose a difficulty from Easy, Medium, or Hard. Thank you.\n')
        start_game()
    # if the user inputs anything other than easy, normal, or hard it will prompt the user to try again and end the function
    print('Try again.')
    

if __name__ == '__start_game__':
    start_game()
