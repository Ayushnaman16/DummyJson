from typing import List
from dataclasses import dataclass
from Hair import Hair
from Address import Address
from Bank import Bank
from Company import Company
from Crypto import Crypto

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