import sys
from PySide6.QtWidgets import (
    QApplication, QListWidget, QWidget, QVBoxLayout,
    QPushButton, QLineEdit, QLabel, QListView
)

def calcular_imc(peso, altura):
    return peso / (altura ** 2)

def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif imc < 25:
        return "Peso normal"
    elif imc < 30:
        return "Sobrepeso"
    else:
        return "Obesidade"
    
class IMCApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Calculador de IMC")
        self.setGeometry(200, 200, 400, 500)

        layout = QVBoxLayout()

        # Entradas
        self.input_peso = QLineEdit()
        self.input_peso.setPlaceholderText("Peso (kg)")

        self.input_altura = QLineEdit()
        self.input_altura.setPlaceholderText("Altura (m)")

        layout.addWidget(self.input_peso)
        layout.addWidget(self.input_altura)

        # Botão
        self.btn_calcular = QPushButton("Calcular IMC")
        layout.addWidget(self.btn_calcular)

        # Resultado
        self.resultado = QLabel("Resultado: - ")
        layout.addWidget(self.resultado)

        # Histórico
        self.historico = QListWidget()
        layout.addWidget(self.historico)

        self.setLayout(layout)

        # Evento
        self.btn_calcular.clicked.connect(self.executar)

    def executar(self):
        try:
            peso = float(self.input_peso.text())
            altura = float(self.input_altura.text())

            if peso <= 0 or altura <= 0:
                raise ValueError
            
        except:
            self.resultado.setText("Valores inválidos")
            return

        imc = calcular_imc(peso, altura)
        classificacao = classificar_imc(imc)

        texto = f"IMC: {imc:.2f} - {classificacao}"
        self.resultado.setText(texto)

        # Histórico
        self.historico.addItem(f"{peso}kg / {altura}m - {texto}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = IMCApp()
    janela.show()
    sys.exit(app.exec())

