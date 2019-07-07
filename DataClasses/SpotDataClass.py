import dataclasses


@dataclasses.dataclass(frozen=True)
class Spot:
    name: str
    latitude: int = 0
    longitude: int = 0
