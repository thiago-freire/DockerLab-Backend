from typing import Type

class BadRequest(Exception):
    def __init__(self, message: Type[str]) -> None:
        self.message = message
        self.status_code = 400

    def __repr__(self) -> str:
        return super().__repr__()