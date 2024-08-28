#functions are essentially a block of code that does nothing until it is called somewhere
# DRY! Don't repeat yourself.
# DRY! Don't repeat yourself.
# DRY! Don't repeat yourself.
#How many times have you given the same advice, or directions, or whatever over and over again?
#With funtions. you would be able to write the code once and then cal it whatever someone needed it.

#"def" is what notifies the code that a function is about to start
#my_function is the name of the function below.
#"()" the parenthesisis for the a parameters. the block below has none. ":" the colon lets the code know that the block of code that follows is part of the function.
def my_function ():
    #anything that is indented is part of the function. if it is not indented the program reads it as though it is outside the function. think of russian nesting dolls, each line needs indented to be a child of the code above.
    print("My function has run")

# in order for the function to run you have "call it". you do that by writing the name of the function with the (). can't be indented, because that would make it part of the function itself.
my_function()

def npc_greeting():
    print("Hello Traveler. Would you like to browse my wares?")

npc_greeting()

# parameters - 

def player_response(The_response):
    print(The_response)

answer_no = "nah, im good bruh."
answer_yes = "oh yes, no skibidi ohio stuff tho."
player_response(answer_no)
player_response(answer_yes)

npc_greeting()
player_response(answer_no)

def approach_vendor():
    npc_greeting()
    player_response = input("enter 1 for yes 2 for no: ")
    player_response = int(player_response)

    if (player_response == 1):
        print("I'd like to buy a Skibidi Toilet")
    elif (player_response == 2):
        print("Player vanishes like ninja Fortnite Blevins mixer streamer")
    else:
        print("sorry i don't speak stupid")

approach_vendor()