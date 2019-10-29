from dataclasses import dataclass

@dataclass()
class SpotDetail:
    id: int
    sight_spot_id: int
    explanation: str
    picture_URLs: list[str]

