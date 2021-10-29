from typing import Generic, TypeVar


T = TypeVar('T')


class ValueObject(Generic[T]):
    def __init__(self, valor: T) -> None:
        self._valor = valor

    def valor(self) -> T:
        return self._valor
