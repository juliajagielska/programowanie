class Student:
    def __init__(self, name: str, marks: list[int]):
        self.name = name
        self.marks = marks

    def is_passed(self) -> bool:
        average = sum(self.marks) / len(self.marks)
        return average > 50

student1 = Student("Anna", [60, 70, 80])
student2 = Student("Kasia", [10, 40, 50])

print(student1.name, "zaliczył?", student1.is_passed())
print(student2.name, "zaliczył?", student2.is_passed())
