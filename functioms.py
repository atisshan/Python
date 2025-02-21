class Person:
    def __init__(self,j,id):
        self.j=j
        self.id=id
    def talk(self):
        print(f"My name is {self.j}")

name=Person('john',4098)
name.j="John"
name.talk()
print(f'My id is{name.id}')