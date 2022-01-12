from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Categoria_Produto(BaseModel):
    id: Optional[int]
    tipo: str

    class Config:
        orm_mode = True

class Produto(BaseModel):
    id: Optional[int]
    nome: str
    vlr_unit: float
    tamanho: str
    descricao: str
    ingredientes: Optional[str]
    created_at: Optional[datetime]
    updated_at: Optional[datetime]
    categoria_id: int
    categoria: Optional[Categoria_Produto]

    class Config:
        orm_mode = True