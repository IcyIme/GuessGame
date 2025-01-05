from Utils.Page import Page
from Utils.UserInput import UserInput
from Utils.Menu import Menu

class MainMenuPage(Page):
    def __init__(self):
        self.__menu : list[str] = Menu(["test", "test2"])

    def userInput(self) -> int:
        while True:
            try:
                print(self.__menu)
                __userInputValue = int(input(">> "))
                self.__userInput = UserInput(__userInputValue, "menu", self.__menu.lenOfmenuList)
                if(type(self.__userInput.handleInput()) == int):
                    return self.__userInput.handleInput()
                print("Invalid input or you are out of range")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    def __str__(self):
        return "Main Menu Page"