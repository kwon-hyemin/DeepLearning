from dataclasses import dataclass


@dataclass
class Member:
    name: str
    height: float
    weight: float


    @property
    def name(self) -> str: return self._name

    @property
    def weight(self) -> float: return self._weight

    @property
    def height(self) -> float: return self._height

    @name.setter
    def name(self, name): self._name = name

    @weight.setter
    def weight(self, weight): self._weight = weight

    @height.setter
    def height(self, height): self._height = height
