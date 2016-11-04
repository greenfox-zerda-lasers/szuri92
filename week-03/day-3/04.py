# Create a student Class
# that has a method `add_grade`, that takes a grade from 1 to 5
# an other method `get_average`, that returns the average of the
# grades

"""class Student():

    grades = []

    def add_grade(self, grades):
        self.grades.append(grades)
        print(self.grades)

    def get_average(self):
        total = 0
        for i in range(len(self.grades)):
            total += self.grades[i]

        average = total / len(self.grades)
        return average



jani = Student()
jani.add_grade(4)
jani.add_grade(4)
jani.add_grade(5)
jani.add_grade(1)
jani.add_grade(2)

print(jani.get_average())"""

class Student():

    grades = []

    def add_grade(self, *grades):
        for i in range(len(grades)):
            self.grades.append(grades[i])
        return self.grades

    def get_average(self):
        total = 0
        for i in range(len(self.grades)):
            total += self.grades[i]

        average = total / len(self.grades)
        return average


jani = Student()
print(jani.add_grade(1, 2, 4, 4, 3, 5, 5, 5, 5, 4, 5, 2))
print(jani.get_average())
