#add import
from question_b import get_sum_of_evens
while True:
    response = int(input("Insert a number to get the sum of all even numbers in it: "))
    evensum = get_sum_of_evens(response)
    print(f'The sum of all the evens in {response} is {evensum}.')
    while True:
        valid_response = ["yes", "no", "y", "n"]
        response = input("Would you like to play again? ")
        if response not in valid_response:
            print("Please insert a valid yes or no response.")
        elif response == "yes" or response == "y":
            print("Okay. Restarting program.\n")
            p = True
            break
        elif response == "no" or response == "n":
            print("Okay. Exiting program.")
            p = False
            break
    if p:
        continue
    else:
        exit()

