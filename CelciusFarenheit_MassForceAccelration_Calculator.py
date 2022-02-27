# Uncomment this when you reach the "Use the Force" section
train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1

#Convert farenheit to celcius
def f_to_c(f_temp):
  c_temp = (f_temp - 32) * 5/9
  return c_temp
f100_in_celsius = f_to_c(100) 

#Convert celcius to farenheit
def c_to_f(c_temp):
    f_temp = c_temp * (9/5) + 32
    return f_temp
c0_in_farenheit = c_to_f(0)

#Calculate train force 
def get_force(mass, acceleration):
    return mass * acceleration
train_force = get_force(train_mass, train_acceleration)
print(f"The GE train supplies {train_force} Newtons of force")

#Calculate energy and set c as a constant for speed of light
def get_energy(mass, c = 3*10**8):
    return mass * c
bomb_energy = get_energy(bomb_mass)
print(f"A 1kg bomb supplies {bomb_energy} Joules")

#Calculate train force over a distance
def get_work(mass, acceleration, distance):
    force = (mass * acceleration) * distance
    return force
train_work = get_work(train_mass, train_acceleration, train_distance)
print(f"The GE train does {train_work} oules of work over {train_distance} meters.")
