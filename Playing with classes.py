import time
import os
from abc import ABC, abstractmethod


class person():                                                             #Super class 
    def __init__(self, name, last_name):
        self.name = name
        self.last_name = last_name
        
    @abstractmethod
    def get_average(self):
        pass

class student(person):                                                      #object constructor for students
    def __init__(self, name, last_name, maths, science, english):
        super().__init__(name, last_name)   #declares name variables from person()
        self.english = english
        self.maths = maths
        self.science = science

    def get_average(self):                 #overriding function
        average = self.english + self.maths + self.science
        average = int(average / 3)
        return average
    
class teacher(person):                                                      #object constructor for teachers
    def __init__(self, name, last_name, av_english, av_maths, av_science):
        super().__init__(name, last_name)  #declares name variables from person()
        self.av_english = av_english
        self.av_maths = av_maths
        self.av_science = av_science

    def get_average(self):                #overriding function
        average = self.av_english + self.av_maths + self.av_science
        average = int(average / 3)
        return average
    
def main():
    selection = input("please select (T)eacher or (S)tudent: ").lower()  #Select path with elif

    if selection == "s":
        name = input("Please enter student's first name: ")
        last_name = input("Please enter student's last name: ")
        validator = False
            
        while validator == False:                                      #while loop only broken by int_validator()
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
            
        new_student = student(name, last_name, maths, science, english)   #Create new instance

        average_grade = new_student.get_average()                         #calculates average with overidden function

        print(new_student.name, new_student.last_name, "has an average grade of: ", average_grade)
            
    elif selection == "t":       #Exact same as student but taking different values
        name = input("Please enter teacher's first name: ")
        last_name = input("Please enter teacher's last name: ")
        validator = False

        while validator == False:
            av_english = input("Please enter average class english grade: ")
            validator = int_validator(av_english)
        av_english = int(av_english)
        validator = False

        while validator == False:
            av_maths = input("Please enter average class maths grade: ")
            validator = int_validator(av_maths)
        av_maths = int(av_maths)
        validator = False

        while validator == False:
            av_science = input("Please enter average class science grade: ")
            validator = int_validator(av_science)
        av_science = int(av_science)

        new_teacher = teacher(name, last_name, av_english, av_maths, av_science)

        average_grade = new_teacher.get_average()

        print(new_teacher.name, new_teacher.last_name, "has an average class grade of: ", average_grade)

    else:
        print("Invalid input")
        main()

    time.sleep(5)
    clear()
        
    use_again()

def int_validator(num):    #Auto validates int user inputs
    try:
        num = int(num)
        if num < 0 or num > 100:
            print("Invalid input")
            return False
        else:
            return True
    except ValueError:
        print("Invalid input")
        return False

def use_again():       #Simple elif to rerun code as many times as desired
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

def clear():      #Clears screen on linux or windows
    if os.name == 'nt':
        os.system('CLS')
    if os.name == 'posix':
        os.system('clear')


if __name__ == "__main__":
    main()
