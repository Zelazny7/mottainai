from __future__ import annotations
from enum import IntEnum
from abc import ABC, abstractmethod
from typing import Type, Dict
from mottainai import Player, Game


class Material(IntEnum):
    PAPER = 1
    CLOTH = 2
    STONE = 3
    CLAY = 4
    METAL = 5


class Action(ABC):

    actions: Dict[Material, Type[Action]] = {}

    @staticmethod
    def register_action(material: Material, action: Type[Action]) -> None:
        Action.actions.update({material: action})

    @staticmethod
    def create(material: Material) -> Action:
        action = Action.actions.get(material)
        if action is None:
            raise KeyError("No action found for material")
        return action()

    @abstractmethod
    def act(self, player: Player, game: Game) -> None:
        pass

    @abstractmethod
    def pray(self, player: Player, game: Game) -> None:
        pass

    @abstractmethod
    def craft(self, player: Player, game: Game) -> None:
        pass


# TODO implement all of these classes
class ClerkAction(Action):
    pass


class MonkAction(Action):
    pass


class TailorAction(Action):
    pass


class PotterAction(Action):
    pass


class SmithAction(Action):
    pass


Action.register_action(Material.PAPER, ClerkAction)
Action.register_action(Material.STONE, MonkAction)
Action.register_action(Material.CLOTH, TailorAction)
Action.register_action(Material.CLAY, PotterAction)
Action.register_action(Material.METAL, SmithAction)
