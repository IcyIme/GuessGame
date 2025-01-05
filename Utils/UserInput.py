class UserInput:
    def __init__(self, inputValue: int, mode :str, *args: int):
        self.__inputValue: int = inputValue
        self.__mode: str = mode
        self.__maxInputValue: int = int(args[0]) if args else 0

    def handleInput(self):
        try:
            if(self.__processInput() >= 1000):
                return "Error"
            return self.__processInput()
        except Exception:
            return "Error"

    def __processInput(self) -> int:
        if self.__mode == "menu":
            if 1 <= self.__inputValue <= self.__maxInputValue:
                return self.__inputValue
            else:
                return 1001
        elif self.__mode == "Hello World":
            return 0
        else:
            return 1000