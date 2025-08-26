class Dog:
    def __init__(self, name, age):
        self._name = name  # Conventionally private variable
        self._age = age  # Conventionally private variable

    @property
    def name(self):
        return self._name  # Getter

    @name.setter
    def name(self, value):
        self._name = value  # Setter

    @property
    def age(self):
        return self._age  # Getter

    @age.setter
    def age(self, value):
        if value < 0:
            print("Age cannot be negative!")
        else:
            self._age = value  # Setter
"""__init__: Initializes private attributes _name and _age.
@property name: Returns _name value.
@name.setter: Updates _name.
@property age: Returns _age value.
@age.setter: Updates _age if it’s not negative."""