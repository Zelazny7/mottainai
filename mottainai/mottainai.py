
from __future__ import annotations
from enum import IntEnum
from abc import ABC, abstractmethod
from typing import List, Type, Dict
from collections import Counter
import json

class Material(IntEnum):
    PAPER = 1
    CLOTH = 2
    STONE = 3
    CLAY  = 4
    METAL = 5

class Action(ABC):

    actions: Dict[Material, Type[Action]] = {}

    @staticmethod
    def register_action(material: Material, action: Type[Action]) -> None:
        Action.actions.update({material : action})

    @staticmethod
    def create(material: Material) -> Action:
        action = Action.actions.get(material)
        if action is None:
            raise KeyError("No action found for material")
        return action()

    #@abstractmethod
    def act(self) -> None:
        pass
    
    #@abstractmethod
    def pray(self) -> None:
        pass
    
    #@abstractmethod
    def craft(self) -> None:
        pass

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

# class Board():

#     def __init__(self):
#         self.task: Optional[Card] = None
#         self.helpers: List[Card] = []
#         self.craftbench: List[Card] = []
#         self.sales: List[Card] = []
#         self.gallery: List[Card] = []
#         self.giftshop: List[Card] = []
    
#     def add_helper(self, card: Card):
#         self.helpers.append(card)
    
#     def add_material(self, card: Card):
#         self.craftbench.append(card)
    
#     def add_sale(self, card: Card):
#         self.sales.append(card)
    
#     def helper_support(self): 
#         cnt = Counter()
#         for card in self.gallery:
#             cnt[card.material] += 1
#         print(cnt)
        

# class Card():
#     def __init__(self, title: str, material: str, **kwargs):
#         self.title = title
#         self.material = Material[material.upper()]
#         self.location = None

#     @classmethod
#     def from_dict(cls, card_as_dict: Dict[str, str]) -> Card:
#         return cls(**card_as_dict)
    
#     def is_covered(self, works: List[Card]) -> bool:
#         pass
    
#     def get_action(self, works: List[Card]) -> Action:
#         out = Action.factory(self.material)
#         if self.is_covered(works):
#             out.append(Action.factory(self.material))
#         return out
    
#     def __repr__(self):
#         return f"< {self.title} >"
        

# class Game():

#     def __init__(self):
#         self.turn = 0
#         self.players = []
#         self.floor: List[Card] = []
#         self.deck: List[Card] = []
    
#     def _shuffle(self):
#         pass
    
#     def reset(self):
#         return Game()
    
#     def new_game(self):
#         pass


if __name__ == "__main__":

    Action.create(Material.PAPER)

    Action.create(Material.STONE)

    Action.create(Material.METAL)


    # board = Board()
    # kite = Card(title="Kite", material="cloth")
    # bangle = Card(title="Bangle", material="clay")

    # board.gallery.append(bangle)
    # board.gallery.append(kite)

    # board.helper_support()

    # import json
    # with open ('cards.json', 'r') as f:
    #     res = json.load(f)
    
    # deck = [Card.from_dict(j) for j in res]

    # print(deck)
    

    