#Intro to BMI Calculator
print("Welcome to my BMI calculator!")
print("Give me your height and weight, I'll calculate your Body Mass Index")

# Gather BMI metrics from user
def bmi_metrics(): 
    name = input("\nWhat's your name?  ")
    height = float(input(f"\nHi {name.title()}, please enter your height in inches: "))
    weight = float(input("Please enter your weight in pounds: "))
    BMI = (weight  * 703) / (height ** 2)
    
    print(f"{name.title()}, your BMI is {BMI:.2f}")
    if BMI <= 18.5:
        print(f"A person with a BMI of {BMI:.2f} is underwieght ")
    elif BMI <= 24.9:
        print(f"A person with a BMI of {BMI:.2f} is normal weight ")
    elif BMI <= 29.9:
        print(f"A person with a BMI of {BMI:.2f} is overweight ")
    else:
        print(f"A person with a BMI of {BMI:.2f} is obese")
    return BMI

#Prompt user to calculate again       
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

bmi_metrics()
prompt_again()
