class Person:
    def __init__(self, name, age, gender):
        self._name=name
        self._age=age
        self._gender=gender
    def introduce(self):
            print (f"Heyy my name is {self._name}, i am {self._age} of age and i am a {self._gender}")

myself=Person("Shaleen atieno", 21, "Female")
myself.introduce()
    
