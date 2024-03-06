#add import
from question_c import get_assessment_value, get_tax_assessed

while True:
    value = int(input("Please enter the default value of your home: "))
    assessed_value = get_assessment_value(value)
    property_tax = get_tax_assessed(assessed_value)
    print(f'The assessment value of your property is ${assessed_value:.2f}.')
    print(f'The property tax of your property is ${property_tax:.2f} per month.')

    while True:
        valid_response = ["yes", "no", "y", "n"]
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