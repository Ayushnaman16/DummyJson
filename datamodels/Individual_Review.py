import datetime
from dataclasses import dataclass

@dataclass
class IndividualReview:
    rating:int
    comment:str
    date:str
    reviewerName:str
    reviewerEmail:str