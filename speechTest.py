#Função para ouvir e reconhecer a fala
def ouvir_microfone():
    #Habilita o microfone do usuário
    microfone = sr.Recognizer()

    #usando o microfone
    with sr.Microphone() as source:

        #Chama um algoritmo de reducao de ruidos no som
        microfone.adjust_for_ambient_noise(source)

        #Frase para o usuario dizer algo
        print("Diga alguma coisa: ")

        #Armazena o que foi dito numa variavel
        audio = microfone.listen(source)

    try:

        #Passa a variável para o algoritmo reconhecedor de padroes
        frase = microfone.recognizer.recognize_sphinx(audio)

        #Retorna a frase pronunciada
        print("Você disse: " + frase)

    #Se nao reconheceu o padrao de fala, exibe a mensagem
    except sr.UnkownValueError:
        print("Não entendi")

    return frase



import speech_recognition as sr
from gtts import gTTS
from playsound import playsound

#Funcao responsavel por falar 
def cria_audio(audio):
    tts = gTTS(audio)
    #Salva o arquivo de audio
    tts.save('test.mp3')
    print("Estou aprendendo o que você disse...")
    #Da play ao audio
    playsound('test.mp3')
