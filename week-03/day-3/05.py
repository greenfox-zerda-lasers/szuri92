# Create a `Stack` class that stores elements
# It should have a `size` method that returns number of elements it has
# It should have a `push` method that adds an element to the stack
# It should have a `pop` method that returns the last element form the stack and also deletes it from it

# please don`t use the built in methods

class Stack():

    list = []

    def push(self, obj):
        self.list += [obj]


    def size(self):
        total = 0
        for i in self.list:
            total += 1
        return total


    def pop(self):
        length = self.size()
        empty = []
        i = 0
        last = self.list[(self.size()-1)]
        while i < self.size()-1:
            empty += [self.list[i]]
            i += 1
        self.list = empty
        return last



valami1 = Stack()
valami1.push(1)
valami1.push(2)
valami1.push(2)
valami1.push(2)
valami1.push(2)
valami1.push(3)
valami1.push(4)
valami1.push(5)
valami1.push(6)
valami1.push(6)
valami1.push(5)
valami1.push(11)

print(valami1.list)
print(valami1.size())
print(valami1.pop())
print(valami1.list)
