class HTTPBadRequest(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)
        self.message = message
        self.status_code = 400
        self.error_code = "BAD_REQUEST"