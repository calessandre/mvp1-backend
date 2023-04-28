from sqlalchemy import Column, String, Integer, DateTime, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Union

from  model import Base


class Planta(Base):
    __tablename__ = 'planta'

    id = Column("pk_planta", Integer, primary_key=True)
    nome = Column(String(60), unique=True)
    nome_cientifico = Column(String(100))
    quantidade = Column(Integer)
    forma_aquisicao = Column(String(40))
    porte = Column(String(40))
    luminosidade = Column(String(40))
    observacao = Column(String(200))
    data_insercao = Column(DateTime, default=datetime.now())

    def __init__(self, nome:str, nome_cientifico: str, quantidade:int, forma_aquisicao: str, porte: str, 
                 luminosidade: str, observacao: str, data_insercao:Union[DateTime, None] = None):
        """
        Cria uma instância de planta

        Arguments:
            nome: nome da planta
            nome_cientifico: nome cientifico da planta
            quantidade: quantidade de exemplares da plantas
            forma_aquisicao: forma de aquisição da planta
            porte: porte da planta
            luminosidade: luminosidade exigida pela planta
            observacao: observações adicionais sobre a planta
            data_insercao: data de inserção da planta no banco de dados
        """
        self.nome = nome
        self.nome_cientifico = nome_cientifico
        self.quantidade = quantidade
        self.forma_aquisicao = forma_aquisicao
        self.porte = porte
        self.luminosidade = luminosidade
        self.observacao = observacao

        # se não for informada, será a data exata da inserção no banco
        if data_insercao:
            self.data_insercao = data_insercao
