

name = str(input("Enter student name: "))
student_class = str(input("Enter class: "))
num_subjects = int(input("Enter number of subjects: "))

total = 0
for i in range(num_subjects):
    subject = str(input(f"Enter subject {i+1} name: "))
    while True:
        marks = float(input(f"Enter marks for {subject} out of 100: "))
        if marks > 100:
            print("Marks cannot be more than 100. Please try again.")
        elif marks < 0:
            print("Marks cannot be less than 0. Please try again.")
        else:
            break
    total += marks

average = total / num_subjects

if average >= 90:
    grade = "A"
elif average >= 80:
    grade = "B"
elif average >= 70:
    grade = "C" 
elif average >= 60:
    grade = "D"  
else:
    grade = "F"

print("Grade Card")
print("Name:", name)
print("Class:", student_class)
print("Average Marks:", average)
print("Grade:", grade)