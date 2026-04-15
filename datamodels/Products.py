from dataclasses import dataclass
from typing import List
from datamodels.Product_list import Product_list

@dataclass
class Products:
    products:List[Product_list]