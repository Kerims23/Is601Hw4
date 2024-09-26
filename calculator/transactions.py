class Transactions:
    '''Class to track history of calculations.'''
    history = []  # Class variable to store history of calculations

    @classmethod
    def add_to_history(cls, operation: str, a: float, b: float, result: float) -> None:
        '''Adds a calculation to the history.'''
        cls.history.append({
            'operation': operation,
            'operand1': a,
            'operand2': b,
            'result': result
        })

    @classmethod
    def get_history(cls) -> list:
        '''Returns the history of calculations.'''
        return cls.history

    @classmethod
    def clear_history(cls) -> None:
        '''Clears the history of calculations.'''
        cls.history.clear()
