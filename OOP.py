"""def main():
    name = getname()
    dep = get_dep()
    print(f"{name} is studying {dep}")
def getname():
    return input("Your name:").title()
def get_dep():
    return input("Your department:").title()

if __name__ == "__main__":
    main()"""

class Student:
    def __init__(self, club, dep):
        self.club = club
        self.dep = dep
    def __str__(self):
        return f"{self.club} is also {self.dep}"

    @classmethod
    def get_items(cls):
        club = input("Club Name: ")
        dep = input("Department Name: ")
        return cls(club,dep)
    @property
    def club(self):
        return self._club

    @club.setter
    def club(self,club):
        if not club:
            raise ValueError("Missing Club")
        self._club = club
        
    @property
    def dep(self):#getter
        return self._dep
    
    @dep.setter
    def dep(self,dep):#setter
        if dep not in ["VASS", "CES", "SAT", "BEN CARSON"]:
            raise ValueError("Invalid Department")
        self._dep= dep
        
    def courseofst(self): #created method
        match self.course:
            case "CS"|"Computer Science"|"CIS"|"Computer Information System":
                return "Department of Computer Science"
            case "SE"|"Software Engineering":
                return "Department of Software Engineering"
            case "IT"|"Information Technology":
                return "Department of Information Technology"
            case _:
                return "Not in Computing and Engineering SCIENCES"
def main():
    stu = Student.get_items()
    print(stu)
    stu = get_student()
    #if stu["club"] = "BUCC":
        #stu["dep"] = "Computing and Engineering Sciences"
    print(stu.courseofst())
    name, dep = get_student()
    print(f"{name} is studying {dep}")
    
def get_student():
    club = input("Student Club: ")
    dep = input("Student Department: ").upper()
    course= input("Course: ")
    return student(club,dep,course)
    
    name = input("Name: ").title()
    dep = input("Department:").title()
    return name, dep

if __name__ == "__main__":
    main()
    
