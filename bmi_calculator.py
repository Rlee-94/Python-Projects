#Intro to BMI Calculator
print("Welcome to my BMI calculator!")
print("Give me your height and weight, I'll calculate your Body Mass Index")

# Gather BMI metrics from user and store name,age,height, and weight
def bmi_metrics(): 
    get_name = (input("\nWhat's your name?  "))

    #Loop that only accepts number inputs for age, weight and height  
    while True:
        try:
            get_age = int(input(f"\nHi {get_name.title()}, please enter your age: "))
            while get_age <= 0: #Don't accept 0 input for age
                get_age = int(input(f"\nHi {get_name.title()}, please enter your age: "))
        except ValueError:
            print("Oops, that doesn't look like a number, try again.")
        else:
            break
          
    while True:
        try:
            get_height = float(input(f"\nPlease enter your height in inches: "))
            while get_height <= 0: #Dont accept 0 input for height
                get_height = float(input(f"\nPlease enter your height in inches: "))
        except ValueError:
            print("Oops, that doesn't look like a number, try again.")
        else:
            break
         
    while True:
        try:
            get_weight = float(input("\nPlease enter your weight in pounds: "))
            while get_weight <= 0: #Don't accept 0 input for weight
                get_weight = float(input(f"\nPlease enter your weight in pounds: "))
        except ValueError:
            print("Oops, that doesn't look like a number, try again.")
        else:
            break

    return get_name, get_height, get_weight, get_age

#Calculate BMI from given height and weight 
def calculate_bmi():
    bmi_result = (weight * 703) / (height ** 2)

    return bmi_result

#Print BMI and weight category back to user
def print_results():
    print(f"{name.title()}, your BMI is {bmi:.2f}")
    if bmi <= 18.5:
        print(f"A person with a BMI of {bmi:.2f} is considered underwieght ")
    elif bmi <= 24.9:
        print(f"A person with a BMI of {bmi:.2f} is considered normal weight ")
    elif bmi <= 29.9:
        print(f"A person with a BMI of {bmi:.2f} is considered overweight ")
    else:
        print(f"A person with a BMI of {bmi:.2f} is considered obese")

    return name,bmi
  

name, height, weight, age = bmi_metrics()
bmi = calculate_bmi()
print_results()

