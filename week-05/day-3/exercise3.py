# Write a Person class that have a name and a birth_date property
# It should raise an error of the birthdate is less than 0 or more than 2016

class Person:
    def __init__(self, first_name, last_name, birth_date):
        if birth_date < 0 or birth_date > 2016:
            raise ValueError
        else:
            self.name = first_name + last_name
            self.birth_date = birth_date




#person1 = Person('Kovacs', 'Bela', -2)
#print(person1.birth_date)
