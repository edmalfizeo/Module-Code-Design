from typing import Dict
from pytest import raises
from src.calculators.calculator_2 import Calculator2

class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body

def test_calculate():
    mock_request = MockRequest(body={"numbers": [2.12, 4.62, 1.32]})

    calculator_2 = Calculator2()
    formatted_response = calculator_2.calculate(mock_request)
    
    assert isinstance(formatted_response, dict)
    assert formatted_response == { "data": { "Calculator": 2, "result": 0.08 } }