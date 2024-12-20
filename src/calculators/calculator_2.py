from typing import Dict, List
from src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface
from flask import request as FlaskRequest
from src.errors.http_unprocessable_entity import HTTPUnprocessableEntityError

class Calculator2:
    def __init__(self, driver_handler: DriverHandlerInterface) -> None:
        self.__driver_handler = driver_handler
        
    def calculate(self, request: FlaskRequest) -> Dict: # type: ignore
        body = request.json
        input_data = self.__validate_body(body)
        calculated_number = self.__process_data(input_data)
        
        formatted_response = self.__format_response(calculated_number)
        return formatted_response

    def __validate_body(self, body: Dict) -> List[float]:
        if "numbers" not in body:
            raise HTTPUnprocessableEntityError("Invalid request body")

        input_data = body["numbers"]
        if not isinstance(input_data, list):
            raise HTTPUnprocessableEntityError("Invalid request body")
        
        return input_data 
    
    def __process_data(self, input_data: List[float]) -> float:
        first_process_result = [(number * 11) ** 0.95 for number in input_data]
        result = self.__driver_handler.standart_derivation(first_process_result)

        return 1/result
    
    def __format_response(self, calculated_number: float) -> Dict:
        return {
            "data": {
                "Calculator": 2,
                "result": round(calculated_number, 2)
            }
        }
        