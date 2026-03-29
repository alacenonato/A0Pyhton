from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Tarefa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(200), nullable=False)
    concluida = db.Column(db.Boolean, default=False)
    prioridade = db.Column(db.String(20))
    data = db.Column(db.String(20))



