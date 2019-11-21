import os
import time

def clear():
    if os.name == 'nt':
        os.system('CLS')
    if os.name == 'posix':
        os.system('clear')

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

def homework(HW_Grade):
    HW_percent = HW_Grade / 25
    HW_percent = HW_percent * 100
    return HW_percent

def assessment(Assess_Grade):
    A_percent = Assess_Grade / 50
    A_percent = A_percent * 100
    return A_percent

def ICT_Final_Exam(Final_exam_Grade):
    F_percent = Final_exam_Grade / 100
    F_percent = F_percent * 100
    return F_percent

def percent_calc(HW_percent, A_percent, F_percent):
    HW_weighted = HW_percent * 0.25
    A_weighted = A_percent * 0.35
    F_weighted = F_percent * 0.40

    final = HW_weighted + A_weighted + F_weighted
    return final

def display_results(name, Final_percent, HW_Grade, Assess_Grade, Final_exam_Grade):
    grade = ""
    p_f = ""
    if Final_percent >= 90:
        grade = "A*"
        p_f = "Passed"
    elif Final_percent >= 80:
        grade = "A"
        p_f = "Passed"
    elif Final_percent >= 70:
        grade = "B"
        p_f = "Passed"
    elif Final_percent >= 60:
        grade = "C"
        p_f = "Passed"
    elif Final_percent >= 50:
        grade = "D"
        p_f = "Passed"
    elif Final_percent >= 40:
        grade = "E"
        p_f = "Passed"
    elif Final_percent < 40:
        grade = "F"
        p_f = "Failed"

    print("The Student", name, "has", p_f, " with a grade of ", grade)
    time.sleep(1)
    print("Score Breakdown: ")
    time.sleep(1)
    print("Homework: ", HW_Grade, "/25 (Counts as 25%)")
    time.sleep(1)
    print("Assessment: ", Assess_Grade, "/50 (Counts as 35%)")
    time.sleep(1)
    print("Final Exam: ", Final_exam_Grade, "/100 (Counts as 40%)  ")
    time.sleep(1)
    print("With a final weighted percentage of: ", Final_percent, "%")
    time.sleep(5)
    use_again()
    

def main():
    clear()
    name = input("Please enter student's name: ")
    while True:
        try:
            HW_Grade = int(input("Please enter IT Homework Grade (/25): "))
            if HW_Grade > 25:
                clear()
                print("Maximum mark is 25")
                continue
            elif HW_Grade < 0:
                clear()
                print("Cannot have negative marks")
                continue
            clear()
            break
        except ValueError:
            clear()
            print("Invalid input")
            continue
    while True:
        try:
            Assess_Grade = int(input("Please enter assessment grade (/50): "))
            if Assess_Grade > 50:
                print("Maximum mark is 50")
                clear()
                continue
            elif Assess_Grade < 0:
                print("Cannot have negative marks")
                clear()
                continue
            clear()
            break
        except ValueError:
            print("Invalid input")
            clear()
            continue
    while True:
        try:
            Final_exam_Grade = int(input("Please enter ICT final exam grade (/100): "))
            if Assess_Grade > 100:
                print("Maximum mark is 100")
                clear()
                continue
            elif Assess_Grade < 0:
                print("Cannot have negative marks")
                clear()
                continue
            clear()
            break
        except ValueError:
            print("Invalid input")
            clear()
            continue

    HW_percent = homework(HW_Grade)
    A_percent = assessment(Assess_Grade)
    F_percent = ICT_Final_Exam(Final_exam_Grade)

    Final_percent = percent_calc(HW_percent, A_percent, F_percent)
    display_results(name, Final_percent, HW_Grade, Assess_Grade, Final_exam_Grade)
    

if __name__ == "__main__":
    main()
