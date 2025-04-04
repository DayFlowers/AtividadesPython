import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QComboBox, QLineEdit, QMessageBox
from PySide6.QtGui import QPixmap, QColor
from PySide6.QtCore import Qt

import mysql.connector

class TelaCadastro(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Cadastro de Usuário")
        layout = QVBoxLayout()

        # Campos para cadastro
        self.usuario_input = QLineEdit(self)
        self.usuario_input.setPlaceholderText("Usuário")
        layout.addWidget(self.usuario_input)

        self.senha_input = QLineEdit(self)
        self.senha_input.setPlaceholderText("Senha")
        self.senha_input.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.senha_input)

        # Botão de cadastro
        self.cadastrar_button = QPushButton("Cadastrar")
        self.cadastrar_button.clicked.connect(self.cadastrar_usuario)
        layout.addWidget(self.cadastrar_button)

        self.setLayout(layout)

    def cadastrar_usuario(self):
        # Obtém as credenciais inseridas
        usuario = self.usuario_input.text()
        senha = self.senha_input.text()

        # Verificar se os campos estão preenchidos
        if usuario and senha:
            with open("usuarios.txt", "a") as f:
                f.write(f"{usuario},{senha}\n")  # Salva no arquivo
            QMessageBox.information(self, "Cadastro", "Usuário cadastrado com sucesso!")
            self.close()
            self.login = TelaLogin()  # Abre a tela de login após cadastro
            self.login.show()
        else:
            QMessageBox.warning(self, "Erro", "Preencha todos os campos!")

class TelaLogin(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Tela de Login")
        layout = QVBoxLayout()

        # Adicionando a imagem no fundo
        self.imagem_label = QLabel(self)
        self.pixmap = QPixmap("lan4.jpg")  # Carrega a imagem "lan4.jpg"
        self.imagem_label.setPixmap(self.pixmap)
        self.imagem_label.setAlignment(Qt.AlignCenter)  # Centraliza a imagem
        self.imagem_label.setScaledContents(True)  # Ajusta o tamanho da imagem para a janela

        layout.addWidget(self.imagem_label)

        # Container para campos de login e senha
        container = QWidget(self)
        container_layout = QVBoxLayout()

        # Campos de login
        self.usuario_input = QLineEdit(self)
        self.usuario_input.setPlaceholderText("Usuário")
        self.usuario_input.setStyleSheet("color: white; background-color: rgba(0, 0, 0, 100); padding: 5px;")
        container_layout.addWidget(self.usuario_input)

        self.senha_input = QLineEdit(self)
        self.senha_input.setPlaceholderText("Senha")
        self.senha_input.setEchoMode(QLineEdit.Password)
        self.senha_input.setStyleSheet("color: white; background-color: rgba(0, 0, 0, 100); padding: 5px;")
        container_layout.addWidget(self.senha_input)

        # Botões de login e cadastro
        self.login_button = QPushButton("Login", self)
        self.login_button.setStyleSheet("color: white; background-color: #4CAF50; padding: 10px;")
        self.login_button.clicked.connect(self.tentar_login)
        container_layout.addWidget(self.login_button)

        self.cadastrar_button = QPushButton("Cadastrar Novo Usuário", self)
        self.cadastrar_button.setStyleSheet("color: white; background-color: #4CAF50; padding: 10px;")
        self.cadastrar_button.clicked.connect(self.ir_para_cadastro)
        container_layout.addWidget(self.cadastrar_button)

        container.setLayout(container_layout)
        container.setStyleSheet("background-color: rgba(0, 0, 0, 100); border-radius: 10px;")  # Fundo escuro e arredondado para o container
        layout.addWidget(container)

        self.setLayout(layout)

    def tentar_login(self):
        # Obtém as credenciais inseridas
        usuario = self.usuario_input.text()
        senha = self.senha_input.text()

        # Verifica se as credenciais estão no arquivo
        try:
            with open("usuarios.txt", "r") as f:
                usuarios = f.readlines()

            for usuario_line in usuarios:
                u, s = usuario_line.strip().split(",")
                if u == usuario and s == senha:
                    # Login bem-sucedido
                    self.menu = LanchoneteApp()
                    self.menu.show()
                    self.close()
                    return
            QMessageBox.warning(self, "Erro", "Usuário ou senha inválidos!")
        except FileNotFoundError:
            QMessageBox.warning(self, "Erro", "Arquivo de usuários não encontrado.")

    def ir_para_cadastro(self):
        self.cadastro = TelaCadastro()
        self.cadastro.show()
        self.close()

class LanchoneteApp(QWidget):
    def __init__(self):
        super().__init__()

        # Produtos disponíveis
        self.produtos = {
            "Hamburguer": 15.00,
            "Refrigerante": 5.00,
            "Batata Frita": 7.00
        }

        # Layout principal
        self.setWindowTitle("Sistema de Pedidos - Lanchonete")
        layout = QVBoxLayout()

        # Label para mostrar o total
        self.total_label = QLabel("Total: R$ 0.00")
        layout.addWidget(self.total_label)

        # ComboBox para selecionar produto
        self.combo_box = QComboBox()
        self.combo_box.addItems(self.produtos.keys())
        layout.addWidget(self.combo_box)

        # Botões para adicionar produto e finalizar
        button_layout = QHBoxLayout()
        self.adicionar_button = QPushButton("Adicionar Produto")
        self.adicionar_button.clicked.connect(self.adicionar_produto)
        button_layout.addWidget(self.adicionar_button)

        self.finalizar_button = QPushButton("Finalizar Pedido")
        self.finalizar_button.clicked.connect(self.finalizar_pedido)
        button_layout.addWidget(self.finalizar_button)

        layout.addLayout(button_layout)

        self.setLayout(layout)

        # Armazenar o total do pedido
        self.total = 0

    def adicionar_produto(self):
        # Obtém o produto selecionado
        produto_nome = self.combo_box.currentText()
        produto_preco = self.produtos[produto_nome]

        # Atualiza o total
        self.total += produto_preco
        self.total_label.setText(f"Total: R$ {self.total:.2f}")

    def finalizar_pedido(self):
        # Exibe o total final
        self.total_label.setText(f"Pedido Finalizado. Total: R$ {self.total:.2f}")
        self.total = 0  # Reseta o total após finalizar
    
    def conectar():
       return mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database= "meu_banco"
        )

# Função principal para rodar o aplicativo
if __name__ == "__main__":
    app = QApplication(sys.argv)
    login_window = TelaLogin()  # Exibe a tela de login primeiro
    login_window.show()
    sys.exit(app.exec())
