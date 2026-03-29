import sys
import math
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel,
    QLineEdit, QPushButton, QTextEdit, QMessageBox
)


# -----------------------------
# LÓGICA
# -----------------------------
def eh_primo(numero):
    if numero <= 1:
        return False

    for i in range(2, int(math.sqrt(numero)) + 1):
        if numero % i == 0:
            return False

    return True


def listar_divisores(numero):
    return [i for i in range(1, numero + 1) if numero % i == 0]


def contar_primos(limite):
    return sum(1 for i in range(2, limite + 1) if eh_primo(i))


# -----------------------------
# INTERFACE
# -----------------------------
class App(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Verificador de Números Primos")
        self.setGeometry(200, 200, 500, 400)

        layout = QVBoxLayout()

        self.label = QLabel("Digite um número ou vários (separados por vírgula):")
        layout.addWidget(self.label)

        self.input = QLineEdit()
        layout.addWidget(self.input)

        # Botões
        self.btn_verificar = QPushButton("Verificar Número(s)")
        self.btn_verificar.clicked.connect(self.verificar)
        layout.addWidget(self.btn_verificar)

        self.btn_contar = QPushButton("Contar Primos até N")
        self.btn_contar.clicked.connect(self.contar)
        layout.addWidget(self.btn_contar)

        # Área de saída
        self.output = QTextEdit()
        self.output.setReadOnly(True)
        layout.addWidget(self.output)

        self.setLayout(layout)

    # -----------------------------
    # FUNÇÃO: VERIFICAR
    # -----------------------------
    def verificar(self):
        entrada = self.input.text()

        try:
            numeros = [int(n.strip()) for n in entrada.split(",")]

            self.output.clear()

            for numero in numeros:
                resultado = "PRIMO ✅" if eh_primo(numero) else "NÃO primo ❌"
                divisores = listar_divisores(numero)

                self.output.append(f"Número: {numero}")
                self.output.append(f"Resultado: {resultado}")
                self.output.append(f"Divisores: {divisores}")
                self.output.append("-" * 30)

        except ValueError:
            QMessageBox.critical(self, "Erro", "Digite apenas números válidos!")

    # -----------------------------
    # FUNÇÃO: CONTAR PRIMOS
    # -----------------------------
    def contar(self):
        entrada = self.input.text()

        try:
            limite = int(entrada)

            if limite < 0:
                raise ValueError

            total = contar_primos(limite)

            self.output.clear()
            self.output.append(f"Existem {total} números primos até {limite}")

        except ValueError:
            QMessageBox.critical(self, "Erro", "Digite um número inteiro positivo!")


# -----------------------------
# EXECUÇÃO
# -----------------------------
if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = App()
    janela.show()
    sys.exit(app.exec())