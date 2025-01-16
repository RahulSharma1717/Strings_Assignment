# Imagine You run an Institute where all your students are stored in a variable something like this :
# students = 'david mark bill sam'
# You have a few tasks to do like :
# Add a student given by user
# Delete a student given by user
# Check if a student given by user is present or not
# Replace a Student given by user

students = 'david mark bill sam'

def add_student():
    name = input("Enter the name of the student: ")
    add_student = students + ' ' + name
    print(add_student)

def delete_student():
    name = input("Enter the name of the student: ")
    delete_student = students.replace(name, '')
    print(delete_student)

def student_present():
    name = input("Enter the name of the student: ")
    student_present = students.find(name)
    if student_present == -1:
        print(f"The student {name} is not present")
    else:
        print(f"The student {name} is present")

def replace_student():
    old_student = input("Enter the name of the old student to replace: ")
    new_student = input("Enter the name of the new student: ")
    replaced = students.replace(old_student, new_student)
    print(replaced)

operations = input("""Enter the operation to be performed: 
                        For adding a student type 'ADD'
                        For deleting a student type 'DEL'
                        To check if a student is present type 'PRESENT'
                        To replace a student type 'REPLACE'
                        """).upper()

if operations == 'ADD':
    add_student()
elif operations == 'DEL':
    delete_student()
elif operations == 'PRESENT':
    student_present()
elif operations == 'REPLACE':
    replace_student()
else:
    print("Enter only the operations provided")


"""Output:
Enter the operation to be performed: 
                        For adding a student type 'ADD'
                        For deleting a student type 'DEL'
                        To check if a student is present type 'PRESENT'
                        To replace a student type 'REPLACE'
                        del
Enter the name of the student: sam
david mark bill 
"""

"""Output:
Enter the operation to be performed: 
                        For adding a student type 'ADD'
                        For deleting a student type 'DEL'
                        To check if a student is present type 'PRESENT'
                        To replace a student type 'REPLACE'
                        present
Enter the name of the student: david
The student david is present
"""

"""Output:
Enter the operation to be performed: 
                        For adding a student type 'ADD'
                        For deleting a student type 'DEL'
                        To check if a student is present type 'PRESENT'
                        To replace a student type 'REPLACE'
                        replace
Enter the name of the old student to replace: bill
Enter the name of the new student: rahul
david mark rahul sam
"""