import socket
NUM_BYTES_RECV = 8192


class MetodosSocket:
    @staticmethod
    def receber_texto(sock):
        bytes_recv = sock.recv(NUM_BYTES_RECV)
        return bytes_recv.decode()

    @staticmethod
    def receber_texto_endereco_origem(sock):
        bytes, endereco_origem = sock.recvfrom(NUM_BYTES_RECV)
        return bytes.decode(), endereco_origem

    @staticmethod
    def enviar_texto(message, sock):
        sock.send(message.encode())

    @staticmethod
    def enviar_texto_com_destino(mensagem, sock, endereco):
        sock.sendto(mensagem.encode(), endereco)
