import time
print("")
print("--------")
print("TXT Game")
print("--------")
print("")
print("")

def char_creation():
    print("-----------------")
    print("Charater Creation")
    print("-----------------")
    char_name = input("Charater Name: ")
    print("")
    print("Charater gender")
    print("| 1 - Male | 2 - Female | 3 - other |")
    char_Gender = input("Charater Gender: ")
    if char_Gender == "1":
        char_Gender = "Male"
    elif char_Gender == "2":
        char_Gender = "Female"
    elif char_Gender == "3":
        char_Gender = "Enby"
    else:
        print("Invaild Charater")
        print("restarting Charater editor")
        time.sleep(1)
        print("")
        char_creation()

    return char_name
    return char_Gender

char_creation()

print(char_name)
print(char_Gender)