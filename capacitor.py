#!/usr/bin/env python3
from ex1 import TransformCreatureFactory, HealingCreatureFactory


if __name__ == "__main__":
    trans = TransformCreatureFactory()
    heal = HealingCreatureFactory()
    for creature_1 in (heal.create_base(), heal.create_evolved()):
        print(creature_1.describe())
        print(creature_1.attack())
        print(creature_1.heal())
        print()
    for creature_2 in (trans.create_base(), trans.create_evolved()):
        print(creature_2.describe())
        print(creature_2.attack())
        print(creature_2.transform())
        print(creature_2.attack())
        print(creature_2.revert())
        print()
