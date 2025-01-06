from Utils.Page import Page
from Utils.UserInput import UserInput
from Utils.Menu import Menu

class MainMenuPage(Page):
    def __init__(self):
        self.__menu : list[str] = Menu(["Play", "Settings"])

    def userInput(self) -> int:
        try:
            self.__userInput = UserInput("menu", self.__menu.lenOfmenuList)
            return self.__userInput.handleInput()
            print("Invalid input or you are out of range")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    def __str__(self):
        return self.__menu