#!/usr/bin/env python3
from .creature import Creature
from .abilities import TransformCapability, HealCapability


class HealBase(Creature, HealCapability):
    def __init__(self, name: str = "Healer") -> None:
        super().__init__(name, "Grass")
        self.didattack = False

    def heal(self) -> str:
        if self.didattack is True:
            self.didattack = False
            return f"{self.name} uses Heal!"
        return f"{self.name} can only heal after attack."

    def attack(self) -> str:
        if self.didattack is False:
            self.didattack = True
        return f"{self.name} uses Leaf Blade!"


class HealEvolved(Creature, HealCapability):
    def __init__(self, name: str = "Heiler") -> None:
        super().__init__(name, "Dark/Electric")
        self.didattack = False

    def heal(self) -> str:
        if self.didattack is True:
            self.didattack = False
            return f"{self.name} uses Heal!"
        return f"{self.name} can only heal after attack."

    def attack(self) -> str:
        if self.didattack is False:
            self.didattack = True
        return f"{self.name} uses Black Thunder!"


class MorphBase(Creature, TransformCapability):
    def __init__(self, name: str = "Shiftling") -> None:
        super().__init__(name, "Normal")
        self.transformed = False

    def attack(self) -> str:
        if self.transformed:
            return f"{self.name} uses Morph Strike!"
        return f"{self.name} uses Tackle!"

    def transform(self) -> str:
        self.transformed = True
        return f"{self.name} shifts into a sharper form!"

    def revert(self) -> str:
        self.transformed = False
        return f"{self.name} returns to normal."


class MorphEvolved(Creature, TransformCapability):
    def __init__(self, name: str = "Morphagon") -> None:
        super().__init__(name, "Normal/Soul Reaper")
        self.transformed = False

    def attack(self) -> str:
        if self.transformed:
            return f"{self.name} uses ~卍解: Senbonzakura Kageyoshi~"
        return f"{self.name} uses front slash!"

    def transform(self) -> str:
        self.transformed = True
        return f"{self.name} morphs into a Shinigami!"

    def revert(self) -> str:
        self.transformed = False
        return f"{self.name} returns to normal."
