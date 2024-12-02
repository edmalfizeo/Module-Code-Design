from typing import Dict, List
from pytest import raises
from src.calculators.calculator_4 import Calculator4

class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body

class MockDriverHandler:
    def mean(self, numbers: List[float]) -> float:
        return 4.0
    
def test_calculate():
    mock_request = MockRequest({"numbers": [2, 4, 6]})
    calculator = Calculator4(MockDriverHandler())

    response = calculator.calculate(mock_request)
    
    assert response == {'data': {'Calculator': 4, 'result': 4.0} }

def test_calculate_with_body_error():
    mock_request = MockRequest({"number": [2, 4, 6]})
    calculator = Calculator4(MockDriverHandler())

    with raises(Exception) as excinfo:
        calculator.calculate(mock_request)

    assert str(excinfo.value) == "Invalid request body"     

def test_calculate_with_body_error_2():
    mock_request = MockRequest({"numbers": ""})
    calculator = Calculator4(MockDriverHandler())

    with raises(Exception) as excinfo:
        calculator.calculate(mock_request)

    assert str(excinfo.value) == "Invalid request body"