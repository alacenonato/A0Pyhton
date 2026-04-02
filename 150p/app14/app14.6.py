import sys
import random
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton,
    QVBoxLayout, QHBoxLayout, QSpinBox, QTextEdit
)

# =========================
# LÓGICA (mesma do projeto)
# =========================
def gerar_jogo(qtd):
    return sorted(random.sample(range(1, 61), qtd))

def gerar_varios(qtd_jogos, qtd_nums):
    return [gerar_jogo(qtd_nums) for _ in range(qtd_jogos)]

def gerar_resultado():
    return sorted(random.sample(range(1, 61), 6))

def verificar(jogo, resultado):
    acertos = len(set(jogo) & set(resultado))
    
    if acertos == 6:
        status = "SENA 🥇"
    elif acertos == 5:
        status = "QUINA 🥈"
    elif acertos == 4:
        status = "QUADRA 🥉"
    else:
        status = "-"
    
    return acertos, status

def formatar(jogo):
    return " ".join(f"{n:02d}" for n in jogo)

# =========================
# INTERFACE
# =========================
class MegaSenaApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("🎰 Mega-Sena Pro")
        self.setGeometry(200, 200, 600, 500)

        layout = QVBoxLayout()

        # Inputs
        input_layout = QHBoxLayout()

        self.qtd_jogos = QSpinBox()
        self.qtd_jogos.setMinimum(1)
        self.qtd_jogos.setMaximum(100)
        self.qtd_jogos.setValue(5)

        self.qtd_numeros = QSpinBox()
        self.qtd_numeros.setMinimum(6)
        self.qtd_numeros.setMaximum(15)
        self.qtd_numeros.setValue(6)

        input_layout.addWidget(QLabel("Jogos:"))
        input_layout.addWidget(self.qtd_jogos)
        input_layout.addWidget(QLabel("Números:"))
        input_layout.addWidget(self.qtd_numeros)

        # Botão
        self.btn_gerar = QPushButton("Gerar Jogos")
        self.btn_gerar.clicked.connect(self.executar)

        # Área de texto
        self.resultado = QTextEdit()
        self.resultado.setReadOnly(True)

        layout.addLayout(input_layout)
        layout.addWidget(self.btn_gerar)
        layout.addWidget(self.resultado)

        self.setLayout(layout)

    def executar(self):
        qtd_jogos = self.qtd_jogos.value()
        qtd_numeros = self.qtd_numeros.value()

        jogos = gerar_varios(qtd_jogos, qtd_numeros)
        resultado = gerar_resultado()

        texto = "🎯 Jogos:\n\n"

        for i, jogo in enumerate(jogos, 1):
            texto += f"Jogo {i}: {formatar(jogo)}\n"

        texto += "\n🏆 Resultado Oficial:\n"
        texto += formatar(resultado) + "\n\n"

        ranking = []

        for i, jogo in enumerate(jogos, 1):
            acertos, status = verificar(jogo, resultado)
            ranking.append((i, jogo, acertos, status))

        ranking.sort(key=lambda x: x[2], reverse=True)

        texto += "📊 Resultado:\n\n"

        for item in ranking:
            texto += (
                f"Jogo {item[0]}: {formatar(item[1])} "
                f"→ {item[2]} acertos {item[3]}\n"
            )

        melhor = ranking[0]

        texto += "\n🔥 Melhor jogo:\n"
        texto += (
            f"Jogo {melhor[0]} com {melhor[2]} acertos {melhor[3]}"
        )

        self.resultado.setText(texto)


# =========================
# EXECUÇÃO
# =========================
if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = MegaSenaApp()
    janela.show()
    sys.exit(app.exec())