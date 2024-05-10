from dataclasses import dataclass
from typing import ClassVar

# without dataclass
# class Point:
#     x: int
#     y: int

#     def __init__(self, x, y) -> None:
#         self.x = x
#         self.y = y

#     def __repr__(self) -> str:
#         return f"point (x={self.x}, y={self.y})"
    

#     def __eq__(self, value: object):
#         return self.x == value.x and self.y == value.y
    

# with dataclass
# @dataclass
# class Point:
#     x: int
#     y: int


# p1 = Point(1, 2)
# p2 = Point(1, 2)
# print(p1, p2)
# print(p1.__eq__(p1))
# print(p1 == p2)


@dataclass()
class InventoryItem:
    name: str
    unit_price: float
    quantity_on_hand: int = 0
    # class variable
    standard_price: ClassVar[int] = 200

    def total_cost(self) -> float:
        return self.unit_price * self.quantity_on_hand
    

inv = InventoryItem("m6 rifle", 1230.1, 3)
inv2 = InventoryItem("m4 rifle", 1300, 4)
inv3 = InventoryItem("m7 rifle", 1230.1, 3)

print(inv)
print(inv.standard_price)
InventoryItem.standard_price = 300
print(inv2.standard_price)
print(inv.total_cost())
print(inv.__eq__(inv3))