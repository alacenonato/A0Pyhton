from flask import Flask, render_template, request, redirect, session
import datetime

app = Flask(__name__)
app.secret_key = "segredo"

# ==== Dados =====
saldo = 1000.0
senha_correta = "1234"
extrato = []
limite_saque_diario = 500.0
saque_realizado_hoje = 0.0

def data_hora():
    return datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")

# ==== Rotas =====

@app.route("/", methods = ["GET", "POST"])
def login():
    if request.method == "POST":
        senha = request.form["senha"]

        if senha == senha_correta:
            session["logado"] = True
            return redirect("/dashboard")
        else:
            return render_template("login.html", erro ="senha incorreta")
    
    return render_template("login.html")

@app.route("/dashboard", methods=["GET", "POST"])
def dashboard():
    global saldo, saque_realizado_hoje

    if not session.get("logado"):
        return redirect("/")
    
    if request.method == "POST":
        acao = request.form["acao"]
        valor = float(request.form.get("valor", 0))

        if acao == "depositar":
            if valor > 0:
                saldo += valor
                extrato.append(f"{data_hora()} - Depósito: +R$ {valor:.2f}")
        
        elif acao == "sacar":
            if valor <= saldo and valor > 0:
                if saque_realizado_hoje + valor <= limite_saque_diario:
                    saldo -= valor
                    saque_realizado_hoje += valor
                    extrato.append(f"{data_hora()} - Saque: -R$ {valor:.2f}")

    return render_template(
        "dashboard.html", 
        saldo = saldo,
        extrato = extrato
    )

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

# ==== EXECUÇÃO =====
if __name__ == "__main__":
    app.run(debug=True)
    