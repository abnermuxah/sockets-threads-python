import socket
HEADER = 64
PORT = 5050
SERVER = "192.168.0.8"
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT) # transformar strings para bytes
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT) # enviar para o servidor o tamanho da mensagem em bytes
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT)) # depois que o servidor tratar vai devolver o retorno em string


print("Digite o nome da pessoa e receba o numero dela // digite duas vezes 'sair' para encerrar: ")

while True:
    nome = input()
    send(nome)

