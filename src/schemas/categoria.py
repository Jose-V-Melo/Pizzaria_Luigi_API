from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class Produtos_Categoria(BaseModel):
    id: Optional[int]
    nome: str
    vlr_unit: float

    class Config:
        orm_mode = True

class Categoria(BaseModel):
    id: Optional[int]
    tipo: str
    created_at: Optional[datetime]
    updated_at: Optional[datetime]
    produtos: List[Produtos_Categoria]

    class Config:
        orm_mode = True
