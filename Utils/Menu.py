class Menu():
    def __init__(self, menuList: list[str]):
        self.__menuList: list[str] = [f"[{i + 1}] {item}" for i, item in enumerate(menuList)]

    @property
    def lenOfmenuList(self) -> int:
        return len(self.__menuList)

    def __str__(self):
        return "\n".join(self.__menuList)