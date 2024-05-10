from dataclasses import dataclass

class Rectangle:
    def __init__(self, height, width) -> None:
        self.height = height
        self.width = width


@dataclass
class Square(Rectangle):
    side: float

    def __post_init__(self):
        super().__init__(self.side, self.side)