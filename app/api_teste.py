from flask import Flask, request
from flask_pydantic_spec import FlaskPydanticSpec, Response
from app.model import Modelo_de_pedido
from app.crud import Sqlite_Manipulation
import os

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
    teste = os.listdir('/home/bot_pva/db')
    print(teste)
    body = request.context.body.dict()
    db.insert(body["nome"], body["idade"])
    print(body)
    return {"status":"recebido"}

@app.get('/teste/seleciona_pessoa/<int:id>')
def query_db(id):
    return db.query(id)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
