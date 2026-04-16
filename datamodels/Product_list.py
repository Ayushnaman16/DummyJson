from dataclasses import dataclass
# from datamodels.Dimensions import Dimensions
from Dimensions import Dimensions
from Individual_Review import IndividualReview
from Meta import Meta
# from datamodels.Individual_Review import IndividualReview
# from datamodels.Meta import Meta
from typing import List

@dataclass
class Product_list:
    id:int
    title:str
    description:str
    category:str
    price:float
    discountPercentage:float
    rating:float
    stock:int
    tags:List[str]
    brand:str
    sku:str
    weight:int
    dimensions:Dimensions
    warrantyInformation:str
    shippingInformation:str
    availabilityStatus:str
    reviews:List[IndividualReview]
    returnPolicy:str
    minimumOrderQuantity:int
    meta:Meta
    thumbnail:str
    images:List[str]

