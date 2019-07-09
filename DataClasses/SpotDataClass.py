import dataclasses
import math
from pyproj import Geod


@dataclasses.dataclass(frozen=True)
class Spot:
    name: str
    latitude: float
    longitude: float
    stay_time: int

    def difference(self, Spot) -> float:
        g = Geod(ellps='WGS84')
        azimuth, back_azimuth, distance_2d = g.inv(self.longitude, self.latitude, Spot.longitude, Spot.latitude)
        return distance_2d
