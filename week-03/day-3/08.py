# Create a new class called `Person` that has a first_name and a last_name (takes it in it's constructor)
# It should have a `greet` method that prints it's full name

# Create a `Student` class that is the child class of `Person`
# it should have a method to add grades
# it should have a `salute` method that prints it's full name and the average of it's grades as well
class Person():
    first_name = ''
    last_name = ''
    def __init__(self, first, last):
        self.first_name = first
        self.last_name = last

    def greet(self):
        print(self.first_name, self.last_name)


class Student(Person):

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



laci = Person('Laci', 'Kovacs')
belus = Student('Bela', 'Olah')
belus.add_grade(4)
print(laci.greet())
print(belus.greet())
belus.add_grade(4)
belus.add_grade(2)
belus.add_grade(5)
print(belus.get_average())
