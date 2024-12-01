from src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface
from flask import request as FlaskRequest
from typing import Dict, List

class Calculator3:
    def __init__(self, driver_handler: DriverHandlerInterface) -> None:
        self.__driver_handler = driver_handler
        
    def calculate(self, request: FlaskRequest) -> Dict: # type: ignore    
        body = request.json
        input_data = self.__validate_body(body)

        variance = self.__calculate_variance(input_data)
        multiplication = self.__calculate_multiplication(input_data)
        self.__verify_results(variance, multiplication)


    def __validate_body(self, body: Dict) -> List[float]:
        if "numbers" not in body:
            raise Exception("Invalid request, missing 'numbers' key")

        input_data = body["numbers"]
        if not isinstance(input_data, list):
            raise Exception("Invalid request, 'numbers' key must be a list")

        return input_data   
    
    def __calculate_variance(self, numbers: List[float]) -> float:
        variance = self.__driver_handler.variance(numbers)
        return variance
    
    def __calculate_multiplication(self, numbers: List[float]) -> float:
        multiplication = 1
        for number in numbers: multiplication *= number

        return multiplication
    
    def __verify_results(self, variance: float, multiplication: float) -> None:
        if variance < multiplication:
            raise Exception("Process Failed: Variance is less than multiplication")
        
    def __format_response(self, variance: float) -> Dict:
        return {
            "data": {
                "calculator": 3,
                "value": variance
            }
        }    
        
