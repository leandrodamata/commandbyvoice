import os
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound


# Função responsável por falar
def cria_audio(audio):
    # Verifica se o diretório 'audios' existe, caso contrário, cria o diretório
    if not os.path.exists('audios'):
        os.makedirs('audios')

    tts = gTTS(audio, lang='pt-br')
    # Salva o arquivo de áudio
    tts.save('audios/hello.mp3')
    print("Estou aprendendo o que você disse...")
    # Dá play ao áudio
    playsound('audios/hello.mp3')


# Função responsável por ouvir e reconhecer a fala
def ouvir_microfone():
    # Habilita o microfone para ouvir o usuário
    microfone = sr.Recognizer()
    with sr.Microphone() as source:
        # Chama a função de redução de ruído disponível na speech_recognition
        microfone.adjust_for_ambient_noise(source)
        # Avisa ao usuário que está pronto para ouvir
        print("Diga alguma coisa: ")
        # Armazena a informação de áudio na variável
        audio = microfone.listen(source)

    try:
        # Passa o áudio para o reconhecedor de padrões do speech_recognition
        frase = microfone.recognize_google(audio, language='pt-BR')
        # Após alguns segundos, retorna a frase falada
        print("Você disse: " + frase)
    # Caso não tenha reconhecido o padrão de fala, exibe esta mensagem
    except sr.UnknownValueError:
        print("Não entendi")

    return frase


frase = ouvir_microfone()
cria_audio(frase)