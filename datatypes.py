# "#" Comments the code - so that humans can read it, but the program ignores it. 
# Uses Comments to communicate what your code does.

# Strings - Strings are words/characters.
first_name = "STORM" # Strings have to be inside of " double quotes" or 'single quotes'
# the quotes have to match. You can't have "Hi' a double quote matched with a single quote.
print(first_name)

# Side note: the assignment operator & variables. "=" is the assignment operator. It is a command that says the variable name is equal to the value. So first_name = "STORM", is a command telling first_name is "STORM"

# int --> intergers. theses are whole numbers: -5, -4 ,-3, -1, 0, 1, 2, 3, 4... 506,322
user_age = 16
print(user_age)

#floats --> these are nubers with decimal points. 97.6, 101.2
patient_temp = 97.6
print(patient_temp)

# boolean --> true and/or false
x = 5
y = 10
z = 10
w = 100
print(x == y)
print(z == y)
if (x == y):
    print(f"if this print is true. x: {x} equals y: {y}")
if (y == z):
    print(f"if this print is true. y: {y} equals z: {z}")
#additional boolean operators
# == equal to
# >= greater than or equal to
# < less than
# > greater than
# != not equal to

print(w == y)
print(w <= y)
print(w >= y)
print(w < y)
print(w > y)
print(w != y)