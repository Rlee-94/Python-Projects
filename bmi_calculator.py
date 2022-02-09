#Intro to BMI Calculator
print("Welcome to my BMI calculator!")
print("Give me your height and weight, I'll calculate your Body Mass Index")

# Gather BMI metrics from user and create two loops that only accept number inputs for height/weight
def bmi_metrics(): 
    get_name = (input("\nWhat's your name?  "))
    get_age = (input("What is your age? "))
 
    while True:
        try:
            get_height = float(input(f"\nHi {get_name.title()}, please enter your height in inches: "))
            break
        except ValueError:
            print("Oops, that doesn't look like a number, try again.")
    while True:
        try:
            get_weight = float(input("Please enter your weight in pounds: "))
            break
        except ValueError:
            print("Oops, that doesn't look like a number, try again.")

#Calculate BMI from given height and weight
    BMI = (get_weight  * 703) / (get_height ** 2) 

    return get_name, get_age, get_height, get_weight, BMI

def print_results():
    #Display user BMI and weight category back to them
    print(f"{get_name.title()}, your BMI is {BMI:.2f}")
    if BMI <= 18.5:
        print(f"A person with a BMI of {BMI:.2f} is considered underwieght ")
    elif BMI <= 24.9:
        print(f"A person with a BMI of {BMI:.2f} is considered normal weight ")
    elif BMI <= 29.9:
        print(f"A person with a BMI of {BMI:.2f} is considered overweight ")
    else:
        print(f"A person with a BMI of {BMI:.2f} is considered obese")
    
#Prompt user to run calculator again       
def prompt_again(): 
    while True:
        run_again = input("\nWould you like to do another calculation (y/n)? ")
        if run_again == 'y':
            bmi_metrics()
        elif run_again == 'Y':
            bmi_metrics()
        elif run_again == 'N':
            break
        elif run_again == 'n':
            break
        else:
            print("Please enter 'y' or 'n' ")

get_name, get_age, get_height, get_weight, BMI = bmi_metrics()
print_results()
prompt_again()




    

    
 
