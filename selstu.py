#import random

def checkname(name):
    return name.isalpha()
    
def no_stu(no_of_stu):
    #empty list to store inputs
    course_bencar = ["Medicine", "Anatomy", "Nursing"]
    course_ces = ["Computer Science", "Software Engineering", "Information Technology"]
    course_sat = ["Medical Laboratory", "Mathematics", "Bio-Chemistry", "Industrial Chemistry", "Public Health"]
    course_vass = ["International law", "Mass Communication", "Public Administration", "Tourism"]
    students  = []
    
    print("  |Departments Available🏫: VASS ,CES, BEN CARSON ,SAT|")
    
    for i in range(no_of_stu):
        #collects student inputs using a dictionary
        student ={} 
        student["fname"] = input(f"{i+1} Firstname: ").title().strip()
        while not checkname(student["fname"]):
            print(f"Enter only first name {student['fname']}.")
            student["fname"] = input("Enter a valid First name: ").title().strip()
            students.append(student)
            
        student["sname"] = input("Surname: ").title().strip()
        while not checkname(student["sname"]):
            print(f"Enter only Surname {student['sname']}.")
            student["sname"] = input("Enter a valid Surname: ").title().strip()
            students.append(student)
            
        student["department"] = (input("Department: ")).upper()
        student["course"]  = input("Course: ").title() 
        students.append(student)
            
        valid_department = ["VASS" ,"CES", "BEN CARSON" ,"SAT"]
        
        #checks if the department is the valid_department list and allows user enter correct department
        while student["department"] not in valid_department:
            print("\nInvalid Department for", student["fname"])
            print(student["fname"], "here are the valid departments!!")
            print("1)VASS 2)CES 3)BEN CARSON 4)SAT")
            student["department"] = input("Enter a valid department:").upper()
            
            students.append(student)
            break
        #checks course selected for the VASS department and allows user enter correct course
        if student["department"] == "VASS":
            
            while student["course"] not in course_vass:
                print("\nInvalid Course for", student["fname"])
                print("Courses Available in Veronica Adeleke School of Social-Sciences")
                print("1)International law\n2)Mass Communication\n3)Public Administration\n4)Tourism")
                student["course"] = input("Enter a valid course: ").title()
                
                students.append(student)
    
        #checks course selected for the CES department and allows user enter correct course
        elif student["department"] == "CES":
            
            while student["course"] not in course_ces:
                print(student["fname"],"\'s",student["course"], "not in Computing and Engineering Sciences department")
                print("Courses Available in School of Computing and Engineering Sciences")
                print("1)Computer Science\n2)Software Engineering\n3)Information Technology")
                student["course"] = input("Enter a valid course: ").title()
                
                students.append(student)
                
        #checks course selected for SAT department and allows user enter correct course        
        elif student["department"] == "SAT":
            
            while student["course"] not in course_sat:
                print(student["fname"], "course: ", student["course"], "not in Science And Technology department")
                print("Courses Available in School of Science And Technology")
                print("1)Medical Laboratory\n2)Mathematics\n3)Bio-Chemistry\n4)Industrial Chemistry\n5)Public Health")
                student["course"] = input("Enter a valid course: ").title()
                
                students.append(student)
                
        #checks course selected for BEN CARSON department and allows user enter correct course
        elif student["department"] == "BEN CARSON":
            
            while student["course"] not in course_bencar:
                print(student["fname"], "course: ", student["course"], "not in Ben Carson department")
                print("Courses Available in School of Ben Carson")
                print("1)Medicine\n2)Nursing\n3)Anatomy")
                student["course"] = input("Enter a valid course: ").title()
                
                students.append(student)
        
        #appends the students input from linto the empty list created
        else:
            students.append(student)
            
    
    #creates a variable to randomly select student
    print("\n")
    student_number = int(input("Enter the student number:"))
    student_no = student_number - 1
    selected_student = students[student_no]
    print(f"\nSelected student\nFirst Name: {selected_student['fname']}")
    print(f"Last Name: {selected_student['sname']}")
    print(f"Department: {selected_student['department']}")
    print(f"Course: {selected_student['course']}")

    """random_stu = random.choice(students)
    print("\n")
    print(f"Name: {random_stu['fname']} {random_stu['sname']}", end="")
    print(f" Department: {random_stu['department']}")
    print(f"Course: {random_stu['course']}")"""
        

    #prints this if no records are passed
        
#asks for the number of students
nos_of_stu = int(input("Enter number of students: "))
no_stu(nos_of_stu)