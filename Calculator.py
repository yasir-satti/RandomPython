import math
num1 = 1
num2 = 1
operator = ""
answer = 0
while True:
    validation = False
    while validation == False:
        try:
            num1 = input("Please enter your first number: ")
            if num1 == "ans":
                num1 = answer
                validation = True
            else:
                num1 = float(num1)
                validation = True
        except ValueError:
            print("Invalid input")
            continue

    validation = False
    while validation == False:
        try:
            operator = input("Please choose operator(*) Multiply, (/) Divide, (+) Add, (-) Subtract, (^) Power of, (sqrt) Square root:  ")
            if (operator == "*" or operator == "/" or operator == "+" or operator == "-" or operator == "^" or operator == "sqrt"):
                validation = True
            else:
                print("Invalid input")
                continue
        except ValueError:
            print("Invalid input")
            continue

    validation = False
    if operator == "sqrt":
        if num1 == 0.0:
            print("cannot find square root of 0")
            exit()
        else:
            if num1 < 0:
                num1 = abs(num1)
                answer = math.sqrt(num1)
                print("The square root of -", num1, " = ", answer, "√i")
                validation = True
            else:
                answer = math.sqrt(num1)
                print("The square root of ", num1, " = ", answer)
                validation = True
    while validation == False:
        try:
            num2 = float(input("Please enter your second number: "))
        except ValueError:
            print("Invalid input")
            continue

        if operator == "*":
            answer = num1 * num2
            print(num1, " * ", num2, " = ", answer)
            validation = True
        elif operator == "/":
            if num1 != 0 and num2 != 0:
                answer = num1 / num2
                print(num1, " / ", num2, " = ", answer)
                validation = True
            else:
                print("cannot divide by zero")
                validation = True
        elif operator == "+":
            answer = num1 + num2
            print(num1, " + ", num2, " = ", answer)
            validation = True
        elif operator == "-":
            answer = num1 - num2
            print(num1, " - ", num2, " = ", answer)
            validation = True
        elif operator == "^":
            answer = num1 ** num2
            print(num1, " ^ ", num2, " = ", answer)
            validation = True
        else:
            print("You fucked up boo")

