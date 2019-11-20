import time
import os

class person():
    def __init__(self, name, last_name):
        self.name = name
        self.last_name = last_name

class student(person):
    def __init__(self, name1, last_name, maths1, science1, english1):
        super().__init__(name1, last_name)
        self.english = english1
        self.maths = maths1
        self.science = science1

    def get_average(self):
        average = self.english + self.maths + self.science
        average = int(average / 3)
        return average

def main():
    name = input("Please enter student's first name: ")
    last_name = input("Please enter student's last name: ")
    validator = False
    
    while validator == False:
        english = input("Please enter english grade: ")
        validator = int_validator(english)
    english = int(english)
    validator = False
    
    while validator == False:
        maths = input("Please enter maths grade: ")
        validator = int_validator(maths)
    maths = int(maths)
    validator = False
    
    while validator == False:
        science = input("Please enter science grade: ")
        validator = int_validator(science)
    science = int(science)
    
    new_student = student(name, last_name, maths, science, english)

    average_grade = new_student.get_average()

    print(name, "has an average grade of: ", average_grade)

    time.sleep(5)
    clear()
    
    use_again()

def int_validator(num):
    try:
        num = int(num)
        return True
    except ValueError:
        print("Invalid input")
        return False

def use_again():
    while True:
        again = input("Do you want to enter another? (Y/N) : ").lower()
        if again == "y":
            main()
            break
        elif again == "n":
            print ("Bye!")
            exit()
        else:
            print("Invalid Input")
            continue

def clear():
    if os.name == 'nt':
        os.system('CLS')
    if os.name == 'posix':
        os.system('clear')

if __name__ == "__main__":
    main()
