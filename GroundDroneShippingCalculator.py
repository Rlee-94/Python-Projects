

#Ask user for size of package in lbs and throw error if theres an invalid number input for weight.
while True:
    try:
        weight = float(input("Enter your the weight of your package in lbs: "))
    except ValueError:
        print("Please enter a valid number in lbs")
    else:
        break

#Ground shipping cost variables 
cost_ground = 0
cost_ground_premium = 125.00

#Calculate the cost of ground shipping based on weight of package in lbs
if weight < 2:
  cost_ground = weight * 1.5 + 20
  print(f"\nGround shipping cost for a {weight}lb package is: ${cost_ground:.2f}")

elif weight > 2 and weight <= 6:
  cost_ground = weight * 3.0 + 20
  print(f"\nGround shipping cost for a {weight}lb package is: ${cost_ground:.2f}")

elif weight > 6 and weight <= 10:
  cost_ground = weight * 4.0 + 20
  print(f"\nGround shipping cost for a {weight}lb package is: ${cost_ground:.2f}")

else: 
  cost_ground = weight * 4.75 + 20
  print(f"\nGround shipping cost for a {weight}lb package is: ${cost_ground:.2f}")


#Cost of drone shipping variable
cost_drone = 0

#Calculate the cost of drone shipping based on weight of package in lbs
if weight < 2:
  cost_drone = weight * 4.5 + 0
  print(f"Drone shipping cost for a {weight}lb package is: ${cost_drone:.2f}")

elif weight > 2 and weight <= 6:
  cost_drone = weight * 9.00 + 0
  print(f"Drone shipping cost for a {weight}lb package is: ${cost_drone:.2f}")

elif weight > 6 and weight <= 10:
  cost_drone = weight * 12.00 + 0
  print(f"Drone shipping cost for a {weight}lb package is: ${cost_drone:.2f}")

else: 
  cost_drone = weight * 14.25 + 0
  print(f"Drone shipping cost for a {weight}lb package is: ${cost_drone:.2f}")

print(f"\nDon't forget, you can have premium ground shipping for an extra ${cost_ground_premium:.2f}!")

#Prompt for premium ground shipping add-on
prompt_premium = input("Would you like to add premium ground shipping?(y/n): ")

cost_with_premium = cost_ground + cost_ground_premium #Define premium cost variable and return price to user below.

if prompt_premium == 'y' or prompt_premium == 'Y':
    print(f"\nGreat! Your new ground shipping cost is ${cost_with_premium:.2f}")

elif prompt_premium == 'n' or prompt_premium == 'N': 
    print("Ok. Thank you for your order!")


        

