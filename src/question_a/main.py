#add import
from question_a import get_random_number
while True:
    num = get_random_number()
    valid_response = ("yes", "no", "y", "n")

    # did you win?
    while True:
        response = int(input("Guess the random number (1-5): "))
        if response == num:
            print("YOU ACTUALLY DID IT HOORAY! The number WAS " + str(num))
            p = True
            break
        else:
            while True:
                response = input("Nope. Try again? ")
                if response not in valid_response:
                    print("I'm sorry, I didn't quite catch that. Try inputting a valid yes or no response.")
                elif response == "yes" or response == "y":
                    p = True
                    break
                elif response == "no" or response == "n":
                    print("The correct number was", str(num) + ". Shutting down the program.")
                    p = False
                    break
            if p:
                continue
            else:
                break

    # play again?
    while p == True:
        response = input("Would you like to play again? ")
        if response not in valid_response:
            print("I'm sorry, I didn't quite catch that. Try inputting a valid yes or no response.")
        elif response == "yes" or response == "y":
            print("You got it. Restarting the program.")
            p = True
            break
        elif response == "no" or response == "n":
            print("You got it. Shutting down the program.")
            p = False
            break
    if p:
        continue
    else:
        exit()