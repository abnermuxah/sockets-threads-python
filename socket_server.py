import socket 
import threading
def agenda(nome):
    #if nome == 'nome':
    #   retunr DD N MMMM MMMM
    if nome == 'glaucia':
        return '84 9 9988 7766'
    elif nome == 'abner':
        return '84 9 8899 7666'
    elif nome == 'marcos':
        return '84 9 123 456'
    elif nome == 'alberto':
        return '84 9 123 456'
    else :
        return ' nao encontrado na lista :( '

HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname()) # salvar o IPV4 da maquina do  (cmd > ipconfig)
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONECT = "sair"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def atender_client(conn, addr):
    print("[NOVA CONEXAO] ",addr," Conectado ")
    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT) # decodificar bytes para string
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT) # transformar para string a MSG
            if msg == DISCONECT:
                connected = False
            num = agenda(msg)
            print(addr," Digitou: ", msg)
            conn.send((num).encode(FORMAT))
    conn.close()  

def start():
    server.listen()
    print("[OUVINDO] O servidor esta ouvindo no endereco:", SERVER)
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=atender_client, args=(conn, addr))
        thread.start()
        print("[CONEXOES ATIVAS]" , threading.activeCount() - 1)
print("[INICIADO] O SERVIDOR ESTA INICIADO...")

start()


