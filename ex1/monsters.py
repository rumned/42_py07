#!/usr/bin/env python3
from .abilities import TransformCapability, HealCapability
from ex0.creature import Creature


class HealBase(Creature, HealCapability):
    def __init__(self, name: str = "Sproutling") -> None:
        super().__init__(name, "Grass")

    def heal(self) -> str:
        return f"{self.name} uses Leech Seed! It heals itself!"

    def attack(self) -> str:
        return f"{self.name} uses Vine Whip!"


class HealEvolved(Creature, HealCapability):
    def __init__(self, name: str = "Bloomelle") -> None:
        super().__init__(name, "Grass/Poison")

    def heal(self) -> str:
        return f"{self.name} uses Absorb! It heals itself by a large amount!"

    def attack(self) -> str:
        return f"{self.name} uses Leaf Blade!"


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
