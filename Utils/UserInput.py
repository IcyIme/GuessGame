class UserInput:
    __errorCode: int = 1000

    def __init__(self, mode: str, *args: int):
        self.__mode: str = mode
        self.__maxInputValue: int = int(args[0]) if args else 0
        self.__minInputValue: int = args[1] if len(args) > 1 else 1

    def handleInput(self) -> int:
        while True:
            try:
                self.__inputValue: int = int(input(f"{'Player' if self.__mode == "play" else 'AI'} >> " if self.__mode == "play" else ">> "))
                if self.__processInput() == self.__errorCode:
                    print("Invalid input. Please enter a valid number.")
                else:
                    return self.__processInput()
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    def __processInput(self) -> int:
        if self.__mode == "menu":
            if self.__minInputValue <= self.__inputValue <= self.__maxInputValue:
                return self.__inputValue
            else:
                return self.__errorCode

        elif self.__mode == "play":
            if self.__minInputValue <= self.__inputValue <= self.__maxInputValue:
                return self.__inputValue
            else:
                return self.__errorCode

        elif self.__mode == "Hello World":
            return 0

        else:
            return self.__errorCode
