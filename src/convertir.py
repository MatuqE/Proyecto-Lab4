from pydub import AudioSegment


# Ruta del archivo MP3
mp3_file = "src/public/chancho.mp3"

# Ruta de salida para el archivo WAV
wav_file = "src/public/wav/chancho.wav"

# Cargar el archivo MP3
audio = AudioSegment.from_mp3(mp3_file)

# Convertir a WAV
audio.export(wav_file, format="wav")