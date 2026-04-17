from typing import List
from dataclasses import dataclass
from datamodels.Coordinates import Coordinate

@dataclass
class Address:
    address:str
    city:str
    state:str
    stateCode:str
    postalCode:str
    coordinates:Coordinate
    country:str


