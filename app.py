from flask_openapi3 import OpenAPI, Info, Tag
from sqlalchemy.exc import IntegrityError
from flask_cors import CORS
from flask import redirect

from model import Session, Planta
from schemas import *


info = Info(title="API para gerenciamento de coleção de plantas", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)


# Definindo tags
home_tag = Tag(name="Documentação", description="Documentação da API.")
planta_tag = Tag(name="API", description="Adição, visualização, remoção e listagem de plantas.")

# Implementando as rotas
@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi/swagger - abre a documentação swagger da API proposta.
    """
    return redirect('/openapi/swagger')

# Adicionar planta

@app.post('/planta', tags=[planta_tag],
          responses={"200": PlantaViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def add_planta(form: PlantaSchema):
    """Adiciona uma nova planta e retorna uma representação da planta.
    """
    planta = Planta(
        nome=form.nome,
        nome_cientifico=form.nome_cientifico,
        quantidade=form.quantidade,
        forma_aquisicao=form.forma_aquisicao,
        porte=form.porte,
        luminosidade=form.luminosidade
        )

    try:
        # criando conexão com a base
        session = Session()
        # adicionando planta
        session.add(planta)
        # efetivando o comando de adição de novo item na tabela
        session.commit()
        return apresenta_planta(planta), 200

    except IntegrityError as e:
        # como a duplicidade do nome é a provável razão do IntegrityError
        error_msg = "Planta de mesmo nome já salva na base."
        return {"message": error_msg}, 409

    except Exception as e:
        # caso ocorra um erro fora dos previstos
        error_msg = "Não foi possível salvar novo item."
        return {"message": error_msg}, 400


# Buscar todas as plantas cadastradas

@app.get('/plantas', tags=[planta_tag],
         responses={"200": ListagemPlantasSchema, "404": ErrorSchema})
def get_plantas():
    """Faz a busca por todos as plantas cadastradas e retorna uma representação da listagem de plantas.
    """
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    plantas = session.query(Planta).all()

    if not plantas:
        # se não há plantas cadastradas
        return {"plantas": []}, 200
    else:
        # retorna a representação de planta
        print(plantas)
        return apresenta_plantas(plantas), 200


# Buscar uma planta pelo id passado.

@app.get('/planta', tags=[planta_tag],
         responses={"200": PlantaViewSchema, "404": ErrorSchema})
def get_planta(query: PlantaBuscaSchema):
    """Faz a busca por um planta a partir do id da planta e retorna uma representação das plantas.
    """
    planta_id = query.planta_id
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    planta = session.query(Planta).filter(Planta.id == planta_id).first()

    if not planta:
        # se a planta não foi encontrada
        error_msg = "Planta não encontrada na base."
        return {"message": error_msg}, 404
    else:
        # retorna a representação de planta
        return apresenta_planta(planta), 200

# Apagar uma planta pelo id passado.

@app.delete('/planta', tags=[planta_tag],
            responses={"200": PlantaDelSchema, "404": ErrorSchema})
def del_planta(query: PlantaBuscaSchema):
    """Deleta uma planta a partir do id informado e retorna uma mensagem de confirmação da remoção.
    """
    planta_id = query.planta_id

    # criando conexão com a base
    session = Session()
    # fazendo a remoção
    count = session.query(Planta).filter(Planta.id == planta_id).delete()
    session.commit()

    if count:
        # retorna a representação da mensagem de confirmação
        return {"message": "Planta removida.", "id": planta_id}
    else:
        # se o planta não foi encontrado
        error_msg = "Planta não encontrada na base."
        return {"message": error_msg}, 404
