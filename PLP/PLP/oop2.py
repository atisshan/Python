class Me:
    def __init__(self,name,age,course,hobby):
        self._name=name #encapsulation
        self._age=age
        self._course=course
        self._hobby=hobby

        def display(self):
            return NotImplementedError("Not implememtned")
class me(Me):
    def display(self):
        return f"My name is {self._name}, i am {self._age} years old, i am doing {self._course} nad i love {self._hobby}"
    
class Record(Me):
    def display(self):
        return f"Student:{self._name}\n {self._age}\n {self._course}\n {self._hobby}"
    
class Course(Me):
    def display(self):
        return f"I am pursuing {self._course}"
my_record=me("shakeen", 21, "Computer Science", "Singing")
my_record2=Record("shakeen", 21, "Computer Science", "Singing")
my_record3=Course("shakeen", 21,"Computer Science","singing")

print(my_record.display())
print(my_record2.display())
print(my_record3.display())