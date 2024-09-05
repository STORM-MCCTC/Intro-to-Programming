def start():
    #takes user input
    operation = input("Input Opertion (+, -, *, /, ^): ")
    num1 = input("First Number: ")
    num2 = input("Second Number: ")
    
    if operation == ("+"):
        addition(num1, num2)
    elif operation == ("-"):
        subtraction(num1, num2)
    elif operation == ("*"):
        multiplication(num1, num2)
    elif operation == ("/"):
        division(num1, num2)
    elif operation == ("^"):
        exponent(num1, num2)
    else:
        print("Error: Invaild Operator")
        print("")
        start()
        
def addition(var1, var2):
    anw = (float(var1) + float(var2))
    print((var1) + "+" + (var2) + "=" + str(anw))
def subtraction(var1, var2):
    anw = (float(var1) - float(var2))
    print((var1) + "-" + (var2) + "=" + str(anw))
def multiplication(var1, var2):
    anw = (float(var1) * float(var2))
    print((var1) + "*" + (var2) + "=" + str(anw))
def division(var1, var2):
    if var1 == "0":
        print("divide by zero error")
    elif var2 == "0":
        print("divide by zero error")
    else:
        anw = (float(var1) / float(var2))
        print((var1) + "/" + (var2) + "=" + str(anw))
def exponent(var1, var2):
    anw = (float(var1) ** float(var2))
    print((var1) + "^" + (var2) + "=" + str(anw))

loop = "true"
while (loop == "true"):
    start()
    print("")