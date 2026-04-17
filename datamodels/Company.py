from dataclasses import dataclass
from datamodels.Address import Address

@dataclass
class Company:
    department:str
    name:str
    title:str
    address:Address



