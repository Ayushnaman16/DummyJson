from typing import List
from dataclasses import dataclass

@dataclass
class Address:
    address:str
    city:str
    state:str
    stateCode:str
    postalCode:str
    coordinates:Cordinates
    country:str


