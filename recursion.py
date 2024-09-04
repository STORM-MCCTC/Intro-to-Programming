#below is an example of recursion.

def my_recursion():
    choice = input("would you like to play a game: ")
    choice = choice.lower()
    if(choice == "y"):
        my_recursion()
    elif(choice == "n"):
        print("Have a nice day")
        exit()
    else:
        my_recursion()
my_recursion()