import sys
import unicodedata
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout,
    QPushButton, QLineEdit, QLabel, QListWidget
)

def normarlizar(texto):
    # remove acentos
    texto = unicodedata.normalize("NFD",texto)
    texto = texto.encode("ascii", "ignore").decode("utf-8")

    # remove espaços e deixa minúsculo
    texto = texto.replace(" ", "").lower()

    return texto

def eh_palindromo(texto):
    return texto == texto[::-1]

class PalindromoApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Verificador de Palindromo")
        self.setGeometry(200, 200, 400, 500)

        layout = QVBoxLayout()

        # Entrada
        self.input_texto = QLineEdit()
        self.input_texto.setPlaceholderText("Digite uma palavra ou frase")
        layout.addWidget(self.input_texto)

        # Botão
        self.btn_verificar = QPushButton("Verificar")
        layout.addWidget(self.btn_verificar)

        # Resultado
        self.resultado = QLabel("Resultado: - ")
        layout.addWidget(self.resultado)

        # Histórico
        self.historico = QListWidget()
        layout.addWidget(self.historico)

        self.setLayout(layout)

        # Evento
        self.btn_verificar.clicked.connect(self.verificar)

    def verificar(self):
        texto = self.input_texto.text()

        if not texto.strip():
            self.resultado.setText("Digite algo.")
            return
        
        texto_norm = normarlizar(texto)

        if eh_palindromo(texto_norm):
            resultado = "É palindromo"
        else:
            resultado = "Não é palindromo"

        self.resultado.setText(resultado)

        # Histórico
        self.historico.addItem(f"{texto} - {resultado}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = PalindromoApp()
    janela.show()
    sys.exit(app.exec())



                         
