import whisper
import pyaudio
import wave
import subprocess
from answer_window import answer_window, auto_close_window
import time
import logging
import os
from db_module import write_to_db
from datetime import datetime

script_path = (os.path.dirname(os.path.realpath(__file__)))


logging.basicConfig(level=logging.DEBUG, filename='llama_main.log',
                    format='%(asctime)s %(name)s \
                        %(levelname)s:%(message)s')
logger = logging.getLogger(__name__)

FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
CHUNK = 1024
RECORD_SECONDS = 2
WAVE_OUTPUT_FILENAME = "audio.wav"
params = []
AI_IMAGE = script_path + '/data/punk_icon_200x200.png'

 # Set up PyAudio
audio_f = pyaudio.PyAudio()
stream = audio_f.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True,
                      frames_per_buffer=CHUNK)


def listen_write(RECORD_SECONDS):
    """
    Write you voice query in file
    """
    say("im_listen.txt")
    logger.debug('Say "I litening before start recording')

    time.sleep(1)
    stream = audio_f.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)
    frames = []
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)
    waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    waveFile.setnchannels(CHANNELS)
    waveFile.setsampwidth(audio_f.get_sample_size(FORMAT))
    waveFile.setframerate(RATE)
    waveFile.writeframes(b''.join(frames))
    waveFile.close()
    logger.debug('Audio file is writed')


def decode(MODEL):
    """Speech To Text via openai whisper"""
    notify_send("Whisper working")
    logger.debug("Start decode voice via whisper")
    model = whisper.load_model(MODEL)
    audio = whisper.load_audio("audio.wav")
    audio = whisper.pad_or_trim(audio)
    mel = whisper.log_mel_spectrogram(audio).to(model.device)
    options = whisper.DecodingOptions(fp16=False, language='en')
    result = whisper.decode(model, mel, options)
    logger.debug("End decode file in whisper")
    auto_close_window(result.text)
    return result.text


def notify_send(text):
    cmd = ['notify-send', f'"{text}"', '-i', AI_IMAGE, '-t', '2000', '-a', 'Llama voice']
    subprocess.call(cmd, shell=False)
    return True


def write_file_result(result):
    with open("result.txt", 'w') as f:
        logging.debug("Text answer from Llama writed in file")
        f.write(result)


def say(file):
    cmd = ['festival', '--tts', '--language', 'russian', file]
    subprocess.Popen(cmd, shell=False)
    logger.debug(f"Festival say from {file}")


time.sleep(1)
listen_write(5)
question = decode(MODEL="medium")
print(question)
notify_send("Llama is Processing")
logger.debug("Start query to Llama")
cmd = f'echo "{question}" | python3 llama.py'
try:
    result = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
except subprocess.CalledProcessError as e:
    logger.debug(e)
answer = result.communicate()[0].decode('utf8')
logger.debug("Llama is got answer")
write_file_result(answer)
answer_window(answer)
current_date = datetime.now()
data_for_db = []
data_for_db.append(current_date)
data_for_db.append(question)
data_for_db.append(answer.split('A:')[1].replace('\n', ''))
write_to_db(data_for_db)
logger.debug('End the program iteration')
