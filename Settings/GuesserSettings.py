class GuesserSettings:
    __minValue: int = 1
    __maxValue: int = 999

    __minValueEdge: int = 0
    __maxValueEdge: int = 1000

    def __init__(self, rangeFrom=1, rangeTo=10):
        self.__rangeFrom: int = rangeFrom if rangeFrom > self.__minValueEdge else self.__minValue
        self.__rangeTo: int = rangeTo if rangeTo < self.__maxValueEdge else self.__maxValue

    def getRangeFrom(self):
        return self.__rangeFrom

    @property
    def range(self) -> tuple():
        return self.__rangeTo, self.__rangeFrom

    @range.setter
    def range(self, *value) -> None:
        if not isinstance(value, tuple) or len(value) != 2:
            raise ValueError("Range must be a tuple of two elements.")
        if(value[0] > self.__minValueEdge and value[1] < self.__maxValueEdge):
            self.__rangeFrom: int = value[0]
            self.__rangeTo: int = value[1]
        else:
            self.__rangeFrom: int = self.__minValue
            self.__rangeTo: int = self.__maxValue

    def __repr__(self):
        return f"GuesserSettings(rangeFrom={self.__rangeFrom}, rangeTo={self.__rangeTo})"

    def __str__(self):
        return f"Settings: Range [{self.__rangeFrom} - {self.__rangeTo}]"
