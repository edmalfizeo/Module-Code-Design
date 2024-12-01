from typing import Dict
from .http_unprocessable_entity import HTTPUnprocessableEntityError
from .http_bad_request import HTTPBadRequest

def handle_errors(error: Exception) -> Dict:
    if isinstance(error, (HTTPUnprocessableEntityError, HTTPBadRequest)):
        return {
            "error": {
                "message": error.message,
                "error_code": error.error_code
            }
        }
    
    return {
        "error": {
            "status_code": 500,
            "message": "Internal Server Error",
        }
    }