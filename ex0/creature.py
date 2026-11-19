#!/usr/bin/env python3
import abc


class Creature(abc.ABC):
    def __init__(self, name: str, type: str) -> None:
        self.name = name
        self.type = type

    @abc.abstractmethod
    def attack(self) -> str:
        pass

    def describe(self) -> str:
        return f"{self.name} is a {self.type} type {self.__class__.__name__}"


class FireBase(Creature):
    def __init__(self, name: str = "Flameling") -> None:
        super().__init__(name, "Fire")

    def attack(self) -> str:
        return f"{self.name} uses Ember!"


class FireEvolved(Creature):
    def __init__(self, name: str = "Pyrodon") -> None:
        super().__init__(name, "Fire")

    def attack(self) -> str:
        return f"{self.name} uses Fire Blast!"


class WaterBase(Creature):
    def __init__(self, name: str = "Aquabub") -> None:
        super().__init__(name, "Water")

    def attack(self) -> str:
        return f"{self.name} uses Water Gun!"


class WaterEvolved(Creature):
    def __init__(self, name: str = "Torragon") -> None:
        super().__init__(name, "Water")

    def attack(self) -> str:
        return f"{self.name} uses Hydro Blast!"

