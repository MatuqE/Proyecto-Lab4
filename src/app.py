import speech_recognition as sr

from pydub import AudioSegment


# # Ruta del archivo MP3
# file = "src/public/chancho.mp3"

# # Ruta de salida para el archivo WAV
# wav_file = "src/public/wav/audio.wav"

# # Cargar el archivo MP3
# audio = AudioSegment.from_mp3(file)

# # Convertir a WAV
# audio.export(wav_file, format="wav")


# ###################

# # Crear un reconocedor
# recognizer = sr.Recognizer()

# # Abrir el archivo de audio
# audio_file = 'src/public/wav/audio.wav'  # Reemplaza con la ruta de tu archivo de audio

# with sr.AudioFile(audio_file) as source:
#     audio_data = recognizer.record(source)  # Grabar el audio

#     # Convertir audio a texto
#     text = recognizer.recognize_google(audio_data, language='es-ES')  # Idioma puede variar

#     print("Texto extraído:", text)







# # Crear un objeto de reconocimiento
# recognizer = sr.Recognizer()

# # Cambiar la tasa de muestreo a 16000Hz (opcional, ajusta según la calidad de tu audio)
# sr.AudioFile.default_samplerate = 22000

# audio_file = "src/public/wav/audio.wav"  # Reemplaza con la ruta de tu archivo de audio

# with sr.AudioFile(audio_file) as source:
#     # Escuchar el archivo de audio
#     audio = recognizer.record(source)

#     try:
#         # Utilizar Google Speech Recognition para convertir audio a texto
#         texto = recognizer.recognize_google(audio, language='es-ES')
#         print("Texto reconocido: ", texto)
#     except sr.UnknownValueError:
#         print("No se pudo entender el audio")
#     except sr.RequestError as e:
#         print("Error al recuperar resultados; {0}".format(e))


########


# from pydub import AudioSegment
# import os

# audio_file = "src/public/audio.wav"  # Reemplaza con la ruta de tu archivo de audio

# # Crear una carpeta para los segmentos si no existe
# carpeta_segmentos = "src/public/wav"
# if not os.path.exists(carpeta_segmentos):
#     os.makedirs(carpeta_segmentos)

# # Cargar el audio
# audio = AudioSegment.from_wav(audio_file)

# # Duración del segmento en milisegundos
# segment_duration = 10000  # 10 segundos

# # Dividir el audio en segmentos de duración especificada y guardar en la carpeta
# for i in range(0, len(audio), segment_duration):
#     segment = audio[i:i + segment_duration]
#     segment.export(os.path.join(carpeta_segmentos, f"segmento_{i}.wav"), format="wav")




import speech_recognition as sr
import os

# Función para convertir audio a texto
def audio_a_texto(ruta_audio):
    recognizer = sr.Recognizer()
    with sr.AudioFile(ruta_audio) as source:
        audio = recognizer.record(source)
        try:
            texto = recognizer.recognize_google(audio, language='es-ES')
            return texto
        except sr.UnknownValueError:
            return "No se pudo entender el audio"
        except sr.RequestError as e:
            return f"Error al recuperar resultados; {e}"

carpeta_segmentos = "src/public/wav"

# Recorrer los archivos en la carpeta y convertir cada segmento a texto
for archivo in os.listdir(carpeta_segmentos):
    if archivo.endswith(".wav"):
        ruta_segmento = os.path.join(carpeta_segmentos, archivo)
        texto = audio_a_texto(ruta_segmento)
        print(f"Texto del segmento '{archivo}': {texto}")
