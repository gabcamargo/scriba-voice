import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from threading import Thread
import speech_recognition as sr
import openai

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ScribaVoice")
        self.setWindowIcon(QIcon("./assets/icon-microphone.png"))  # Ícone da janela
        self.setGeometry(100, 100, 400, 200)

        layout = QVBoxLayout()

        # Label para exibir o texto transcrito
        self.texto_label = QLabel("Texto transcrito aqui")
        self.texto_label.setAlignment(Qt.AlignCenter)
        self.texto_label.setStyleSheet("font-size: 14px; color: #333333;")  # Estilo do texto
        layout.addWidget(self.texto_label)

        # Label para exibir o status da captura de voz
        self.status_label = QLabel("")  
        self.status_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.status_label)

        # Botão para iniciar a transcrição de áudio
        self.transcrever_button = QPushButton("Transcrever Áudio")
        self.transcrever_button.setStyleSheet("background-color: #4CAF50; color: white; border: none; padding: 10px 20px; border-radius: 5px; font-size: 14px;")  # Estilo do botão
        self.transcrever_button.clicked.connect(self.transcrever_audio)
        layout.addWidget(self.transcrever_button)

        self.setLayout(layout)

    # Função para transcrever o áudio e gerar resposta da IA
    def transcrever_audio(self):
        # Função interna para realizar a transcrição e a interação com a IA em uma thread separada
        def transcrever():
            self.status_label.setText("Capturando voz...")  
            self.transcrever_button.setEnabled(False)  

            recognizer = sr.Recognizer()
            with sr.Microphone() as source:
                print("Diga algo...")
                try:
                    audio = recognizer.listen(source, timeout=5)
                    texto = recognizer.recognize_google(audio, language='pt-BR')
                    self.texto_label.setText(texto)
                    resposta_lm = self.gerar_texto_lm(texto)  # Gera uma resposta usando a IA
                    self.mostrar_resposta_lm(resposta_lm)  # Mostra a resposta na interface
                    self.status_label.setText("")  
                except sr.WaitTimeoutError:
                    self.mostrar_mensagem("Tempo Limite Excedido", "Não foi detectado áudio. Tente novamente.")
                    self.status_label.setText("")  
                except sr.UnknownValueError:
                    self.mostrar_mensagem("Fala não Reconhecida", "Não foi possível entender o áudio.")
                    self.status_label.setText("")  
                except sr.RequestError as e:
                    self.mostrar_mensagem("Erro de Requisição", f"Erro na requisição ao serviço de reconhecimento de fala: {e}")
                    self.status_label.setText("")  
                finally:
                    self.transcrever_button.setEnabled(True)  

        # Inicia uma nova thread para transcrever o áudio
        t = Thread(target=transcrever)
        t.start()

    # Função para gerar texto com a IA
    def gerar_texto_lm(self, texto):
        openai.api_key = 'sua_chave_de_api'  # Insira sua chave de API da OpenAI
        prompt = texto + "\nIA:"  # Prompt para a LM responder
        resposta = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=50
        )
        return resposta.choices[0].text.strip()

    # Função para exibir a resposta da IA em uma caixa de diálogo
    def mostrar_resposta_lm(self, resposta):
        self.mostrar_mensagem("Resposta da IA", resposta)

    # Função para exibir mensagens de aviso em uma caixa de diálogo
    def mostrar_mensagem(self, title, message):
        msg_box = QMessageBox()
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.setIcon(QMessageBox.Warning)  
        msg_box.setStyleSheet("QLabel{min-width: 200px;}")  
        msg_box.exec_()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
