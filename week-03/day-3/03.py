# create a pirate class
# it should have 2 methods
# drink_rum()
# hows_goin_mate()
# if the drink_rum was called at least 5 times:
# hows_goin_mate should return "Arrrr!"
# "Nothin'" otherwise

class Pirate():

    rum_drunk = 0

    def drink_rum(self):
        self.rum_drunk +=1
        return self.rum_drunk

    def hows_going_mate(self):
        if self.rum_drunk >= 5:
            self.rum_drunk = 0
            return "Arrrr!"
        else:
            return "Nothin"



hookhand = Pirate()
print(hookhand.drink_rum())
print(hookhand.drink_rum())
print(hookhand.drink_rum())
print(hookhand.drink_rum())
print(hookhand.drink_rum())
print(hookhand.drink_rum())
print(hookhand.hows_going_mate())
print(hookhand.hows_going_mate())
print(hookhand.drink_rum())
