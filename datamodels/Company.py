from dataclasses import dataclass
from Address import Address

@dataclass
class Company:
    department:str
    name:str
    title:str
    address:Address



