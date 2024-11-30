from typing import Dict, List
from src.drivers.numpy_handler import NumpyHandler
from flask import request as FlaskRequest

class Calculator2:
    def calculate(self, request: FlaskRequest) -> Dict: # type: ignore
        body = request.json
        input_data = self.__validate_body(body)
        calculated_number = self.__process_data(input_data)
        
        formatted_response = self.__format_response(calculated_number)
        return formatted_response

    def __validate_body(self, body: Dict) -> List[float]:
        if "numbers" not in body:
            raise Exception("Invalid request body")

        input_data = body["numbers"]
        if not isinstance(input_data, list):
            raise Exception("Invalid request body")
        
        return input_data 
    
    def __process_data(self, input_data: List[float]) -> float:
        numpy_handler = NumpyHandler()
        first_process_result = [(number * 11) ** 0.95 for number in input_data]
        result = numpy_handler.standart_derivation(first_process_result)

        return 1/result
    
    def __format_response(self, calculated_number: float) -> Dict:
        return {
            "data": {
                "Calculator": 2,
                "result": round(calculated_number, 2)
            }
        }
        