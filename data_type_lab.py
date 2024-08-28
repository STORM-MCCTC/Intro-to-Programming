#data-types-lab.py
my_int = 42
my_float = 3.14

print("The value of my_int is: ", my_int)
print("The value of my_float is: ", my_float)

addition = my_int + my_float
subtraction = my_int - my_float
mutliplication = my_int * my_float
div = my_int / my_float
power = my_int ** 2
modu = my_int % 5
floor_div = my_int // my_float

print("add: ", addition)
print("sub: ", subtraction)
print("multi: ", mutliplication)
print("division: ", div)
print("power: ", power)
print("modulus: ", modu)
print("Floor Division: ", floor_div)

first_name = "Luke"
last_name = "Skywalker"
full_name = (first_name + " " + last_name)
print("Your Jedi name is: ", full_name)

name_length = len(full_name)
print("the Length of your Jedi name is", name_length, "characters")

message = "May the Force be with you, " + full_name + "!"
print(message)

starships = ["Millenniun falcon", "X-wing", "TIE fighter"]
print("Initial starship fleet: ", starships)

starships.append("star destroyer")
print("updated ship fleet: ", starships)

print("the second starship in the fleet is: ", starships[1])
print("the first starship ready for battle is: ", starships[0])
print("the last starship in formation is: ", starships[-1])