from abc import ABC, abstractmethod

from Utils.Menu import Menu
from Utils.UserInput import UserInput

class Page(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def userInput(self) -> int:
        pass

    def __init__(self):
        self._menu = Menu(["Hello", "World"])

    def userInput(self) -> int:
        while True:
            try:
                print(self._menu)
                user_input_value = int(input(">> "))
                user_input_handler = UserInput(user_input_value, "Hello World", len(self._menu))
                return user_input_handler.handleInput()
            except ValueError:
                print("Invalid input. Please enter a valid number.")
