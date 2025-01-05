from Settings.GuesserSettings import GuesserSettings
from Utils.ComputerGuesser import ComputerGuesser
from Pages.MainMenuPage import MainMenuPage
from Pages.SettingPage import SettingPage

def initialize() -> tuple:
    ai: ComputerGuesser = ComputerGuesser("AI", GuesserSettings())
    return ai

if __name__ == "__main__":
    ai = initialize()
    print(ai.computerGuess())
    a = MainMenuPage().userInput()
    print(a)