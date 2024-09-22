'''Testing Transactions Class'''
from calculator.transactions import Transactions

def test_add_to_history():
    '''Testing addition of calculations to history'''
    Transactions.clear_history()  # Ensure history is empty before the test
    Transactions.add_to_history('add', 2.0, 3.0, 5.0)
    history = Transactions.get_history()
    assert len(history) == 1, "History should contain one entry"
    assert history[0] == {
        'operation': 'add',
        'operand1': 2.0,
        'operand2': 3.0,
        'result': 5.0
    }, "History entry does not match expected values"

def test_get_history():
    '''Testing retrieval of calculation history'''
    Transactions.clear_history()  # Clear history before test
    Transactions.add_to_history('subtract', 5.0, 3.0, 2.0)
    Transactions.add_to_history('multiply', 3.0, 4.0, 12.0)
    history = Transactions.get_history()
    assert len(history) == 2, "History should contain two entries"
    assert history[0]['operation'] == 'subtract', "First entry should be subtract"
    assert history[1]['operation'] == 'multiply', "Second entry should be multiply"

def test_clear_history():
    '''Testing clearing of calculation history'''
    Transactions.clear_history()  # Start with an empty history
    Transactions.add_to_history('divide', 10.0, 2.0, 5.0)
    Transactions.clear_history()
    assert len(Transactions.get_history()) == 0, "History should be empty after clearing"
