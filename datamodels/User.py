from typing import List
from dataclasses import dataclass
from datamodels.Hair import Hair
from datamodels.Address import Address
from datamodels.Bank import Bank
from datamodels.Company import Company
from datamodels.Crypto import Crypto

@dataclass
class User:
    id:int
    firstName:str
    lastName:str
    maidenName:str
    age:int
    gender:str
    email:str
    phone:str
    username:str
    password:str
    birthDate:str
    image:str
    bloodGroup:str
    height:float
    weight:float
    eyeColor:str
    hair:Hair
    ip:str
    address:Address
    macAddress:str
    university:str
    bank:Bank
    company:Company
    ein:str
    ssn:str
    userAgent:str
    crypto:Crypto
    role:str