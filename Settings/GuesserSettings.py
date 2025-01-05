def rangeTypeValidation(rangeFrom: int, rangeTo: int) -> tuple:
    __rangeFrom: int = rangeFrom
    __rangeTo: int = rangeTo
    return rangeFrom, rangeTo

class GuesserSettings:
    def __init__(self, rangeFrom=1, rangeTo=10):
        self.__rangeFrom, self.__rangeTo = rangeTypeValidation(rangeFrom, rangeTo)

    @property
    def range(self) -> range:
        return self.__rangeFrom, self.__rangeTo

    @range.setter
    def range(self, value) -> None:
        if not isinstance(value, tuple) or len(value) != 2:
            raise ValueError("Range must be a tuple of two elements.")
        self.__rangeFrom, self.__rangeTo = rangeTypeValidation(*value)

    def __repr__(self):
        return f"GuesserSettings(rangeFrom={self.__rangeFrom}, rangeTo={self.__rangeTo})"

    def __str__(self):
        return f"Settings: Range [{self.__rangeFrom} - {self.__rangeTo}]"
