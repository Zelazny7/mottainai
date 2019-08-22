from typing import List, Optional
from mottaini import Card


class Player:
    """Class representing the state of a player's board"""

    def __init__(self) -> None:
        self.craft_bench: List[Card] = []
        self.helpers: List[Card] = []
        self.sales: List[Card] = []
        self.gallery: List[Card] = []
        self.gift_shop: List[Card] = []
        self.task: Optional[Card] = None

