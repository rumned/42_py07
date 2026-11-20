#!/usr/bin/env python3
from ex0 import CreatureFactory, FlameFactory, AquaFactory
from ex1 import HealingCreatureFactory
from ex1 import TransformCreatureFactory
from ex2.strategy import BattleStrategy, NormalStrategy
from ex2.strategy import AggressiveStrategy, DefensiveStrategy, StrategyError
from itertools import combinations


def battle(opponents: list[tuple[CreatureFactory, BattleStrategy]],
           number: int,
           evo: bool = False) -> None:
    fighters = []
    for factory, strategy in opponents:
        if evo:
            entity = factory.create_evolved()
        else:
            entity = factory.create_base()
        strategy.check(entity)
        fighters.append((entity, strategy))
    for round_no, ((entity_a, strategy_a), (entity_b, strategy_b)) in \
            enumerate(combinations(fighters, 2), start=1):
        print(f" Round {number}.{round_no}")
        print(f"{entity_a.describe()} vs {entity_b.describe()}")
        for line in strategy_a.act(entity_a) + strategy_b.act(entity_b):
            print(line)


if __name__ == "__main__":
    flame = FlameFactory()
    aqua = AquaFactory()
    heal = HealingCreatureFactory()
    transform = TransformCreatureFactory()
    compatible: list[tuple[CreatureFactory, list[type[BattleStrategy]]]] = [
        (flame, [NormalStrategy]),
        (aqua, [NormalStrategy]),
        (heal, [NormalStrategy, DefensiveStrategy]),
        (transform, [NormalStrategy, AggressiveStrategy]),
    ]
    valid_fighters: list[tuple[CreatureFactory, BattleStrategy]] = [
        (factory,
         next((s for s in strategies
               if s is not NormalStrategy), NormalStrategy)())
        for factory, strategies in compatible]
    tournaments: list[tuple[str,
                            list[tuple[CreatureFactory, BattleStrategy]],
                            bool]] = [
        ("Tournament 1 (valid strat)", valid_fighters, False),
        ("\nTournament 2 (invalid)",
         [(flame, AggressiveStrategy()),
          (heal, AggressiveStrategy()),
          (transform, DefensiveStrategy())],
         False),
        ("\nTournament 3 (evolved)", valid_fighters, True),
    ]

    for number, (title, fighters, evolved) in enumerate(tournaments, start=1):
        try:
            print(title)
            battle(fighters, number, evolved)
        except StrategyError as e:
            print(f"Battle aborted: {e}")
