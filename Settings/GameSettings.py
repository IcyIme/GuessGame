from Settings.GuesserSettings import GuesserSettings
from Utils.ComputerGuesser import ComputerGuesser
from Utils.UserInput import UserInput
import random

class GameSettings:
    __minRounds: int = 1
    __maxRounds: int = 15

    def __init__(self, rounds: int = 5):
        self.rounds: int = rounds if rounds >= self.__minRounds and rounds <= self.__maxRounds else 5

    def play(self) -> str:
        self.__userWins: int = 0
        self.__aiWins: int = 0
        self.__draws: int = 0
        self.__rangeTo, self.__rangeFrom = GuesserSettings().range

        for i in range(self.rounds):
            self.__randNum = random.randint(self.__rangeFrom, self.__rangeTo)
            self.__computerStep: int = ComputerGuesser("AI", GuesserSettings())
            self.__input = UserInput("play", self.__rangeTo, self.__rangeFrom)
            self.__userStep: int = self.__input.handleInput()
            if self.__userStep == self.__computerStep and self.__userStep == self.__rangeFrom and self.__computerStep == self.__randNum:
                self.__draws += 1
            elif self.__userStep == self.__randNum :
                self.__userWins += 1
            else:
                self.__aiWins += 1

        if self.__userWins <= self.__draws >= self.__aiWins:
            return "Its a Draw"
        elif self.__userWins > self.__aiWins:
            return "You Win"
        else:
            return "You Lose"

