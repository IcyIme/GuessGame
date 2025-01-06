import random
from Settings.GuesserSettings import GuesserSettings

class ComputerGuesser:
    def __init__(self, computer_name: str, settings = GuesserSettings.range):
        self.__computer_name: str = computer_name
        self.__settings: GuesserSettings.range = settings

    def computerGuess(self) -> int:
        rangeTo, rangeFrom = self.__settings.range
        return random.randint(rangeFrom, rangeTo)

    def __repr__(self):
        rangeFrom, rangeTo = self.__settings.range
        return f"ComputerGuesser(computer_name='{self.__computer_name}', rangeFrom={rangeFrom}, rangeTo={rangeTo})"

    def __str__(self):
        range_from, range_to = self.__settings.range
        return f"Computer Guesser '{self.__computerName}' with range [{self.rangeFrom} - {self.rangeTo}]"
