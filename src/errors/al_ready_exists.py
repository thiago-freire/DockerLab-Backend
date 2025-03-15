from typing import Type

class AlReadyExists(Exception):
    def __init__(self, message: Type[str], statusCode: Type[int] = 422) -> None:
        self.message = message
        self.status_code = statusCode

    def __repr__(self) -> str:
        return f"{self.message}"