from datetime import datetime, time
from pydantic import BaseModel, EmailStr, field_validator, PositiveFloat, PositiveInt
from typing import Tuple
from enum import Enum

class ProdutoEnum(str, Enum):
    produto1 = "Gemini"
    produto2 = "chatGPT"
    produto3 = "Llamma"
    

class Vendas(BaseModel):
    email: EmailStr
    data: datetime
    valor: PositiveFloat
    quantidade: PositiveInt
    produto: ProdutoEnum
    
    @field_validator('produto')
    def categoria_produto_enum(cls, v):
        return v