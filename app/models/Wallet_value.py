from pydantic import BaseModel


class Wallet_values(BaseModel):
    value: float
    initial_value: float
