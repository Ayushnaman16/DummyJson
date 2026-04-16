from dataclasses import dataclass

@dataclass
class Bank:
    cardExpire:str
    cardNumber:str
    cardType:str
    currency:str
    iban:str
