#!/user/bin/python3

while True: #user options on this cal
    print("Options:")
    print("Enter 'add' to add two numbers")
    print("Enter 'suntract' to subract two numbers")
    print("Enter 'multiply' to multiply two numbers")
    print("Enter 'divide' to divide two numbers")
    print("Enter 'quit' to end the program")
    user_input = input (":")

    if user_input == "quit": #exiting the cal
        break
    elif user_input == "add": #The first method add
        num1 = float(input("Enter a number:")) #Taking the first numer from a user 
        num2 = float(input("Enter another number:")) #taking the second number 
        results = str(num1 + num2) #adding the numbers together 
        print("The answer is:"+ results) #printing the results to the user 

# repeat the above step for all the user options 

    elif user_input == "subtract":
        num1 = float(input("Enter a number:"))
        num2 = float(input("Enter another number:"))
        results = str(num1 + num2)
        print("The answer is:" + results)

    elif user_input == "multiply":
        num1 = float(input("Enter a number:"))
        num2 = float(input("Enter another number:"))
        results = str(num1 + num2)
        print("The answer is:" + results)
        
    elif user_input == "divide":
        num1 = float(input("Enter a number:"))
        num2 = float(input("Enter another number"))
        results = str(num1 / num2) 
        print("The answer is:" + results)
        