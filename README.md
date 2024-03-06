# ScribaVoice

Este é um aplicativo simples de transcrição de áudio desenvolvido em Python com PyQt5, SpeechRecognition e integração com uma Language Model (LLM) usando a API da OpenAI.

## Descrição

O aplicativo permite aos usuários transcrever áudio para texto em tempo real e obter uma resposta gerada por uma IA com base no texto transrito.

## Funcionalidades

- Captura de áudio do microfone.
- Transcrição de fala para texto em tempo real.
- Geração de resposta da IA com base no texto transcrito.
- Exibição de mensagens de erro em caso de falha na transcrição ou na interação com a IA.

## Dependências

Para executar este aplicativo, as seguintes dependências devem ser instaladas:

- pyaudio
- SpeechRecognition
- PyQt5
- openai


Você pode instalar as dependências manualmente ou utilizar o script fornecido para verificar e instalar automaticamente as dependências ausentes.

## Instalação

1. Clone este repositório:

```bash
git clone https://github.com/gabcamargo/scriba-voice.git
```

2. Instale as dependências:

```bash
cd scriba-audio
python dependencies.py
```

3. Execute o aplicativo:

```bash
python app.py
```

## Uso

1. Pressione o botão "Transcrever Áudio" para iniciar a captura de áudio.
2. Fale claramente no microfone para que o aplicativo transcreva o áudio para texto em tempo real.

## Licença

Copyright (c) 2023 Gabriel Camargo

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
