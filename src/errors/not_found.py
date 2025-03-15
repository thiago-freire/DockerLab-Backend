from typing import Type

class NotFound(Exception):
    def __init__(self, message: Type[str]) -> None:
        self.message = message
        self.status_code = 404

    def __repr__(self) -> str:
        return super().__repr__()