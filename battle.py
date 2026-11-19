#!/usr/bin/env python3
from ex0 import CreatureFactory, FlameFactory, AquaFactory


def test_factory(factory: CreatureFactory) -> None:
    base = factory.create_base()
    if not base:
        print("Base Creature not instantiated")
        return None
    print(base.describe())
    print(base.attack())
    evolved = factory.create_evolved()
    if not evolved:
        print("Evolved Creature not instantiated")
        return None
    print(evolved.describe())
    print(evolved.attack())


def test_battle(factory1: CreatureFactory, factory2: CreatureFactory) -> None:
    fighter1 = factory1.create_base()
    fighter2 = factory2.create_base()
    print(f"{fighter1.name} vs {fighter2.name}")
    print(fighter1.attack())
    print(fighter2.attack())


if __name__ == "__main__":
    flame_factory = FlameFactory()
    aqua_factory = AquaFactory()
    print("Testing factory")
    test_factory(flame_factory)
    print()
    test_factory(aqua_factory)
    print()
    print("Testing battle")
    test_battle(flame_factory, aqua_factory)
