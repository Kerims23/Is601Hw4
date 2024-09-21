'''
So from what I understand the @staticmethod does not need self or class.
It also cannot modifiy object state or class state
Its kind of like a regular function

@classmethod is similar but needs cls to pass in a variable etc
This can change the class state unlike the static one

Instance Method (self): 
### (a function that passes self basically)
This is a regular method that takes self as its first parameter.
It operates on an instance of the class, meaning it can access and modify instance attributes.
Use it when you need to work with data specific to that instance.

Class Method (cls): 
### (works with entire class making code more adjustable)
This method uses @classmethod and takes cls as its first parameter.
It operates on the class itself, not on instances. You can use it to access or modify class attributes.
Use it when you need to work with data shared across all instances (like a count of all instances).

Static Method: 
### (relate to the class but dont need to interact with its data.)
This method uses @staticmethod and doesnt take self or cls.
It behaves like a regular function that belongs to the class but doesnt access instance or class data.
Use it for utility functions that are related to the class but dont need any context from it.

### in the example below @staticmethod is used for the overall functions 
# while the @classmethod was used for the the history that records things that the overall class tracks

Another good example chatgpt gave me that helped me for future reference is bank account
__init__ for self.owner and self.balance as the account

deposit function would be an instance because it puts money into an account for the self.owner

withdraw is another instance because it takes money out of account 

TransactionHistory is a class method because it is a historical use of the entire class

ValidAmount is a static method to check if balance will be negative. 

Basically instance are literally instances a person can use 
Class are things to check historcal things 
Static are things to check validation 

'''
# calculator/__init__.py
class Calculator:
    '''this is to record the history of all inputs'''
    history = []  

    @staticmethod
    def add(a: float, b: float) -> float:
        '''adding docstring to get in the habit'''
        result = a + b
        Calculator.history.append(f"Added {a} and {b}: {result}")
        return result

    @staticmethod
    def subtract(a: float, b: float) -> float:
        '''this function is to do the subtractions for calculator'''
        result = a - b
        Calculator.history.append(f"Subtracted {b} from {a}: {result}")
        return result

    @staticmethod
    def multiply(a: float, b: float) -> float:
        '''this function is to multiply for calculator'''
        result = a * b
        Calculator.history.append(f"Multiplied {a} by {b}: {result}")
        return result

    @staticmethod
    def divide(a: float, b: float) -> float:
        '''this function is to divide for calculator'''
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        result = a / b
        Calculator.history.append(f"Divided {a} by {b}: {result}")
        return result

    @classmethod
    def get_history(cls):
        '''this function is to call the history list'''
        return cls.history

    @classmethod
    def clear_history(cls):
        '''this function is to clear history'''
        cls.history.clear()
