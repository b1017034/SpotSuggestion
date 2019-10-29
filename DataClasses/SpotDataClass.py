import dataclasses
import math
from pyproj import Geod


@dataclasses.dataclass(frozen=True)
class Spot:
    id: int
    name: str
    latitude: float
    longitude: float
    stay_time: int
    address: str

    def difference(self, spot) -> float:
        g = Geod(ellps='WGS84')
        azimuth, back_azimuth, distance_2d = g.inv(self.longitude, self.latitude, spot.longitude, spot.latitude)
        return distance_2d

    def json_to_spot(self, response):
        pass