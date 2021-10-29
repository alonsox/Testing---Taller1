import os
from typing import Callable, TypeVar

T = TypeVar('T')

def limpiarPantalla() -> None:
   # for mac and linux(here, os.name is 'posix')
   if os.name == 'posix':
      _ = os.system('clear')
   else:
      # for windows platfrom
      _ = os.system('cls')
   # print out some text

def tryWhileError(callback: Callable[[], T]) -> T:
    while(True):
        try:
            return callback()
        except Exception as e:
            print(str(e))