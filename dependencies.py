import subprocess
import sys

def verificar_dependencias():
    dependencias = ['pyaudio', 'SpeechRecognition', 'PyQt5', 'openai']
    for dependencia in dependencias:
        try:
            __import__(dependencia)
        except ImportError:
            resposta = input(f"A dependência '{dependencia}' não está instalada. Deseja instalá-la agora? (S/N): ")
            if resposta.lower() == 's':
                instalar_dependencia(dependencia)
            else:
                sys.exit(0)

def instalar_dependencia(dependencia):
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', dependencia])
        print(f"{dependencia} instalada com sucesso!")
    except subprocess.CalledProcessError:
        print(f"Falha ao instalar {dependencia}. Certifique-se de ter permissões suficientes ou tente instalar manualmente.")

if __name__ == "__main__":
    verificar_dependencias()
