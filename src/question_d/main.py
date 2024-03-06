#add import
from question_d import is_prime

valid_response = ["yes", "no", "y", "n"]

while True:
    num = int(input("Please enter a number: "))
    prime = is_prime(num)

    if prime:
        print("PRIME")
    else:
        print("NOT PRIME")

    while True:
        response = input("Would you like to enter a separate value? ")

        if response not in valid_response:
            print("Please enter a valid yes or no response.")
            continue
        elif response == "yes" or response == "y":
            print("")
            p = True
            break
        elif response == "no" or response == "n":
            p = False
            break
    if p:
        continue
    else:
        exit()