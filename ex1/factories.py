#!/usr/bin/env python3
from ex0.factories import CreatureFactory
from .monsters import HealBase, HealEvolved, MorphBase, MorphEvolved


class HealingCreatureFactory(CreatureFactory):
    def create_base(self) -> HealBase:
        return HealBase()

    def create_evolved(self) -> HealEvolved:
        return HealEvolved()


class TransformCreatureFactory(CreatureFactory):
    def create_base(self) -> MorphBase:
        return MorphBase()

    def create_evolved(self) -> MorphEvolved:
        return MorphEvolved()
