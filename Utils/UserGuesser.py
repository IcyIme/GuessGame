from Settings.GuesserSettings import GuesserSettings

class Guesser:
    def __init__(self, name: str, settings: GuesserSettings.range):
        self.__name = name
        self.__settings = settings

    def guess(self, guessNumber : int):
        __guessNumber: int = guessNumber

        __rangeFrom, __rangeTo = self.__settings.range

        if guessNumber >= __rangeFrom and guessNumber <= __rangeTo:
            return __guessNumber
        else:
            print(f"{self.__name} cannot guess number because you are out of range, range is {__rangeFrom} and {__rangeTo}.")
            return self.guess(input(f"{self.__name} try again >> "))