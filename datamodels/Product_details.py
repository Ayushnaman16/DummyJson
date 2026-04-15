from typing import List
from dataclasses import dataclass

@dataclass
class Product_details:
    id:int
    title:str
    price:float
    quantity:int
    total:float
    discountPercentage:float
    discountedTotal:float
    thumbnail:str