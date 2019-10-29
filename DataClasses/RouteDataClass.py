from dataclasses import dataclass
from typing import List


@dataclass()
class Step:
    latitude: float
    longitude: float


@dataclass
class Route:
    id: int
    origin_id: int
    destination_id: int
    steps: List[Step]
    duration: int
    distance: int
