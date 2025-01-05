import random
from Settings.GuesserSettings import GuesserSettings

class ComputerGuesser:
    def __init__(self, computer_name: str, settings = GuesserSettings.range):
        self.__computer_name: str = computer_name
        self.__settings: GuesserSettings.range = settings

    def computerGuess(self) -> int:
        range_from, range_to = self.__settings.range
        return random.randint(range_from, range_to)

    def __repr__(self):
        range_from, range_to = self.__settings.range
        return f"ComputerGuesser(computer_name='{self.__computer_name}', rangeFrom={range_from}, rangeTo={range_to})"

    def __str__(self):
        range_from, range_to = self.__settings.range
        return f"Computer Guesser '{self.__computer_name}' with range [{range_from} - {range_to}]"
