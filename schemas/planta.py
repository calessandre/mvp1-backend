from pydantic import BaseModel
from typing import Optional, List
from model.planta import Planta

class PlantaSchema(BaseModel):
    """ Define como uma nova planta a ser inserida na base deve ser representada.
    """
    nome: str = "Anturio"
    nome_cientifico = "Anturio Antuirius"
    quantidade: Optional[int] = 12
    forma_aquisicao: str = "compra"
    porte: str = "grande"
    luminosidade: str = "meia sombra"
    observacao: str = "Exemplo de observacoes sobre a planta"


class PlantaBuscaSchema(BaseModel):
    """ Define como será a estrutura que representa a busca de uma planta pelo seu id.
    """
    planta_id: int = 1


def apresenta_plantas(plantas: List[Planta]):
    """ Retorna uma representação de plantas seguindo o schema definido em PlantaViewSchema.
    """
    result = []
    for planta in plantas:
        result.append({
            "id": planta.id,
            "nome": planta.nome,
            "nome_cientifico": planta.nome_cientifico,
            "quantidade": planta.quantidade,
            "forma_aquisicao": planta.forma_aquisicao,
            "porte": planta.porte,
            "luminosidade": planta.luminosidade,
            "observacao": planta.observacao
        })

    return {"plantas": result}


class PlantaViewSchema(BaseModel):
    """ Define como uma planta será retornada.
    """
    id: int = 1
    nome: str = "Anturio"
    nome_cientifico: str = "Anturio Anturius"
    quantidade: Optional[int] = 12
    forma_aquisicao: str = "compra"
    porte: str = "grande"
    luminosidade: str = "meia sombra"
    observacao: str = "Exemplo de observacoes sobre a planta"
    

class PlantaDelSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição de remoção de uma planta.
    """
    message: str
    id: int

def apresenta_planta(planta: Planta):
    """ Retorna uma representação da planta seguindo o schema definido em PlantaViewSchema.
    """
    return {
        "id": planta.id,
        "nome": planta.nome,
        "nome_cientifico": planta.nome_cientifico,
        "quantidade": planta.quantidade,
        "forma_aquisicao": planta.forma_aquisicao,
        "luminosidade": planta.luminosidade,
        "porte": planta.porte,
        "observacao": planta.observacao
    }

class ListagemPlantasSchema(BaseModel):
    """ Define como uma listagem de plantas será retornada.
    """
    plantas:List[PlantaViewSchema]
    