from Settings.GuesserSettings import GuesserSettings
from Settings.GameSettings import GameSettings
from Utils.ComputerGuesser import ComputerGuesser
from Pages.MainMenuPage import MainMenuPage
from Pages.SettingPage import SettingPage

def initialize() -> tuple:
    ai: ComputerGuesser = ComputerGuesser("AI", GuesserSettings())
    gameSettings: GameSettings = GameSettings()
    mainMenuPage = MainMenuPage()
    return ai,gameSettings, mainMenuPage

def main():
    ai, gameSettings, mainMenuPage = initialize()
    print(mainMenuPage.__str__())
    mainMenu = mainMenuPage.userInput()

    if mainMenu == 1:
        result: str = gameSettings.play()
    else:
        print("Comming soon!")

    print(result)

if __name__ == "__main__":
    main()