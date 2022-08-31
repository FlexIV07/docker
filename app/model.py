from pydantic import BaseModel

class Modelo_de_pedido(BaseModel):
    nome: str
    idade: int
    