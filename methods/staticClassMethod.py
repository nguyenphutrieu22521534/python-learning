class Dog:
    @staticmethod
    def info():
        print("Dogs are loyal animals.")

    @classmethod
    def count(cls):
        print("There are many dogs of class", cls)

dog = Dog()
dog.info()  # Static method call
dog.count()  # Class method call
"""@staticmethod info(): No access to instance or class; prints a general message.
@classmethod count(cls): Receives the class as cls and prints a message including the class."""