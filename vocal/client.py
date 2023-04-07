import socket
import pyaudio

# configure audio
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100

# create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# server address and port
server_address = ('10.10.9.125', 10000)

# create an instance of pyaudio
audio = pyaudio.PyAudio()

# open an audio stream
stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, output=True, input=True, frames_per_buffer=CHUNK)

while True:
    # capture audio from microphone
    data = stream.read(CHUNK)

    # send audio to server
    for i in range(0, int(RATE / CHUNK * 1)):
        sock.sendto(data[i * CHUNK:(i + 1) * CHUNK], server_address)

    # receive audio from server
    data, server = sock.recvfrom(2048)
    while data:
        stream.write(data)
        try:
            data, server = sock.recvfrom(2048)
        except socket.error as e:
            break
