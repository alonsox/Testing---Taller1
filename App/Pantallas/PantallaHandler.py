from typing import Any


class PantallaHandler:
    def setNext(self, handler: 'PantallaHandler') -> 'PantallaHandler':
        self._nextHandler = handler
        return handler

    def next(self, data: Any = None) -> None:
        if self._nextHandler:
            self._nextHandler.handle(data)

    def handle(self, data: Any = None) -> None:
        self.next(data)
