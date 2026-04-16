from typing import List
from dataclasses import dataclass
# from datamodels.Product_details import Product_details
from Product_details import Product_details

@dataclass
class Cart:
    id:int
    products:List[Product_details]
    total:float
    discountedTotal:int
    userId:int
    totalProducts:int
    totalQuantity:int

