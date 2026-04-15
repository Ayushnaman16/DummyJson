from typing import List
from dataclasses import dataclass

@dataclass
class Recipes:
    id:int
    name:str
    ingredients:List[str]
    instructions:List[str]
    prepTimeMinutes:int
    cookTimeMinutes:int
    servings:int
    difficulty:str
    cuisine:str
    caloriesPerServing:int
    tags:List[str]
    userId:int
    image:str
    rating:float
    reviewCount:int
    mealType:List[str]