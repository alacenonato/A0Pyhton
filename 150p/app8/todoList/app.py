from flask import Flask, render_template, request, redirect, url_for
from models import db, Tarefa

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATION"] = False

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route("/", methods=["GET","POST"])
def index():
    if request.method == "POST":
        titulo = request.form.get("titulo")
        prioridade = request.form.get("prioridade")
        data = request.form.get("data")

        if titulo:
            nova = Tarefa(
                titulo=titulo,
                prioridade=prioridade,
                data=data
            )
            db.session.add(nova)
            db.session.commit()

        return redirect(url_for("index"))
    
    filtro = request.args.get("filtro", "todas")

    if filtro == "concluidas":
        tarefas = Tarefa.query.filter_by(concluida=True).all()
    elif filtro == "pendentes":
        tarefas = Tarefa.query.filter_by(concluida=False).all()
    else:
        tarefas = Tarefa.query.all()
    
    return render_template("index.html", tarefas=tarefas, filtro=filtro)

@app.route("/concluir/<int:id>")
def concluir(id):
    tarefa = Tarefa.query.get_or_404(id)
    tarefa.concluida = True
    db.session.commit()
    return redirect(url_for("index"))

@app.route("/remover/<int:id>")
def remover(id):
    tarefa = Tarefa.query.get_or_404(id)
    db.session.delete(tarefa)
    db.session.commit()
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
    

