from abc import ABC, abstractmethod
from typing import Any

class Person(ABC):
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    @abstractmethod
    def __repr__(self) -> str:
        pass
        return self.width * self.height