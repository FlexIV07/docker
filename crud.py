from peewee import SqliteDatabse, Model, TextField, IntegerField, AutoField

db = SqliteDatabse('/home/db/pessoas.db')

class BaseModel(Model):
    class Meta:
        database = db
        
class Pessoa(BaseModel):
    id = AutoField()
    nome = TextField()
    idade = IntegerField()
    
class Sqlite_Manipulation:
    def insert(nome, idade):
        novo_pedido = Pessoa(
                                nome = nome,
                                idade = idade
                            )
        novo_pedido.save()
        
    def query(id):
        result = Pessoa.get(Pessoa.id==id)
        return {"id": result.id,
                "nome": result.nome,
                "idade": result.idade
               }