def get_grade(marks):
    if marks >= 70:
        return "A"
    elif marks >= 60:
        return "B"
    elif marks >= 50:
        return "C"
    elif marks >= 40:
        return "D"
    else:
        return "Fail"    

def average(subj1, subj2, subj3)-> float:
    return (subj1 + subj2 + subj3)/3

print("+" + "-"*48 + "+\n" + "|\t\t Grading System\t\t\t |\n" + "+" + "-"*48 + "+")

eng = int(input("Enter your English marks: "))
maths = int(input("Enter your Maths marks:   "))
sci = int(input("Enter your Sci marks:     "))

print("\n")
print("+" + "-"*48 + "+\n"+ "|\tSubject\t|\tMarks \t|\t Grade\t |\n" + "+" + "-"*48 + "+")
print("|\tEnglish\t\t{}\t\t{}\t |".format(eng, get_grade(eng)))
print("|\tMaths  \t\t{}\t\t{}\t |".format(maths, get_grade(maths)))
print("|\tScience\t\t{}\t\t{}\t |".format(sci, get_grade(sci)))
print("+" + "-"*48 + "+")
print("|\tAverage\t\t{:.2f}\t\t{}\t |".format(average(maths,eng,sci), get_grade(average(maths,eng,sci))))
print("+" + "-"*48 + "+\n")
