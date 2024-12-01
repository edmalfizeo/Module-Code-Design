from src.drivers.numpy_handler import NumpyHandler
from src.calculators.calculator_3 import Calculator3

def calculator_3_factory():
    numpy_handler = NumpyHandler()
    calculator = Calculator3(numpy_handler)
    return calculator