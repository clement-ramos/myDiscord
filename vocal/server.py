import socket
import pyaudio
import threading

# configure audio
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100

# create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# bind the socket to a specific address and port
server_address = ('0.0.0.0', 10000)
sock.bind(server_address)

# create an instance of pyaudio
audio = pyaudio.PyAudio()

# list to keep track of connected clients
clients = []


def handle_client(client_address):
    print(f"New client connected: {client_address}")
    clients.append(client_address)

    # open an audio stream
    stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, output=True, input=True, frames_per_buffer=CHUNK)

    while True:
        # receive audio from client
        data, _ = sock.recvfrom(2048)
        while data:
            stream.write(data)
            print(f"Received {len(data)} bytes from {client_address}")
            try:
                data, _ = sock.recvfrom(2048)
            except socket.error as e:
                break

        # send audio back to client
        for i in range(0, int(RATE / CHUNK * 1)):
            data = stream.read(CHUNK, exception_on_overflow=False)
            for client in clients:
                sock.sendto(data, client)
                print(f"Sent {len(data)} bytes to {client_address}")

    # remove client from the list when disconnected
    print(f"Client disconnected: {client_address}")
    clients.remove(client_address)

while True:
    # wait for a new client to connect
    data, client_address = sock.recvfrom(2048)

    # create a new thread to handle the client
    client_thread = threading.Thread(target=handle_client, args=(client_address,))
    client_thread.start()
