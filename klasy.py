class House:
    color: str
    windows_count: int


    def __init__(self, color: str, windows_count: int) -> None:
        self.color = color
        self.windows_count = windows_count


    def get_color(self) -> str:
        return f'dom jest koloru: {self.color}'


    def add_window(self) -> None:
        self.windows_count += 1


house_1 = House('red', 10)
house_2 = House('blue', 5)

print(f'Dom nr 1 na {house_1.windows_count} okien')
print(f'Dom nr 2 na {house_2.windows_count} okien')

house_1.add_window()
house_2.add_window()

print(f'Dom nr 1 na {house_1.windows_count} okien')
print(f'Dom nr 2 na {house_2.windows_count} okien')

house_2.add_window()

print(f'Dom nr 1 na {house_1.windows_count} okien')
print(f'Dom nr 2 na {house_2.windows_count} okien')
