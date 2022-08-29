from turtle import title
from urllib import request, response
from flask import Flask
from flask_pydantic_spec import FlaskPydanticSpec, Response
from model import Modelo_de_pedido
from crud import Sqlite_Manipulation

app = Flask(__name__)
spec = FlaskPydanticSpec('api de teste', title='API DE TESTE')
spec.register(app)
db = Sqlite_Manipulation

@app.get('/teste')
def return_teste():
    return 'muito que bem vindo'

@app.post('/teste/insere_pessoa')
@spec.validate(body=Modelo_de_pedido, resp=Response('HTTP_201'))
def insert_db():
    body = request.context.body.dict()
    db.insert(body["nome"], body["idade"])
    return {"status":"recebido"}

@app.get('/teste/seleciona_pessoa')
def query_db():
    return db.query()

if __name__ == "__main__":
    app.run(host='0.0.0.0')
