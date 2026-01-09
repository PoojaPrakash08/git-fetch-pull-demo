class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def total_marks(self):
        return sum(self.marks)

    def average_marks(self):
        return self.total_marks() / len(self.marks)

    def grade(self):
        avg = self.average_marks()
        if avg >= 85:
            return "A"
        elif avg >= 70:
            return "B"
        elif avg >= 50:
            return "C"
        else:
            return "Fail"


def main():
    student = Student("Pooja", [78, 85, 90, 88, 80])

    print("Student Name:", student.name)
    print("Total Marks:", student.total_marks())
    print("Average Marks:", student.average_marks())
    print("Grade:", student.grade())


if __name__ == "__main__":
    main()
