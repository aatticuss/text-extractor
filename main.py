import whisper
from pytube import YouTube
# Pytube aparentemente está com problemas, testar outra biblioteca

def getAudioFile(yt_url):
    try:
        ytlink = YouTube(yt_url)
        url_audio = ytlink.streams.get_audio_only()
        if url_audio:
            audio_file_path = url_audio.download()
            print('Download do áudio completo!')
            return audio_file_path
        else:
            print("Nenhum stream de áudio disponível para este vídeo.")
            return None
    except Exception as e:
        print(f"Houve um erro no download do áudio: {e}")
        return None

def transcribeAudio(audio):
    try:
        my_model = whisper.load_model('small')
        text_response = my_model.transcribe(audio)
        with open('transcription.txt', 'w') as file:
            file.write(text_response)
            print('Transcrição de áudio completa!')
            return text_response
    except:
        print('Houve um erro durante a transcrição do áudio.')
        return None

ytVideo_link = input('Insira um link do YouTube: ')
if ytVideo_link.startswith('https://www.youtube.com/'):
    print(f'O link recebido foi {ytVideo_link}')
    audio_file = getAudioFile(ytVideo_link)
    if audio_file:
        text_file = transcribeAudio(audio_file)
        print(text_file)
else:
    print('Insira um link válido do YouTube.')