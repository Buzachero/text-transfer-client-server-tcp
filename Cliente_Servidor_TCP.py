import socket
import sys
from MetodosArquivo import MetodosArquivos
from MetodosSocket import MetodosSocket
from constants import *


def apresentar_menu():
    print('-' * 80)
    print('O que deseja fazer?')
    print('(1) Enviar texto')
    print('(2) Receber texto')
    print('-' * 80)
    opcao = input('( ) ')
    try:
        opcao_int = int(opcao)
    except ValueError:
        opcao_int = 0
    return opcao_int


def conectar_servidor(host, port):
    try:
        client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)  # AF_INET: ProtocoloIP | SOCK_STREAM:ProtocoloTCP
    except socket.error as socket_error:
        print('A criação do socket falhou: {}'.format(socket_error))
        sys.exit(1)
    print('Socket criado com sucesso!')

    server_host_port = '{}:{}'.format(host, port)
    try:
        print('Conectando em {} ...'.format(server_host_port), end=' ')
        client_sock.connect((host, int(port)))
        print('Conexão foi estabelecida com o servidor!')
    except socket.error as socket_error:
        print('Não foi possível conectar estabelecer a conexão!')
        print('Erro: {}'.format(socket_error))
        sys.exit(1)
    return client_sock


def transferir_mensagem_servidor(client_sock, server_host, server_port):
    server_host_port = '{}:{}'.format(server_host, server_port)

    opcao = 0
    while int(opcao) != 1 and int(opcao) != 2:
        opcao = apresentar_menu()

    client_sock.send(str(opcao).encode())
    if int(opcao) == 1:
        texto_arquivo = MetodosArquivos.ler_conteudo_arquivo(CLIENT_FILE_PATH)
        print('Enviando texto para {} ...'.format(server_host_port))
        MetodosSocket.enviar_texto(texto_arquivo, client_sock)
        texto_recebido = MetodosSocket.receber_texto(client_sock)
        print(texto_recebido)
    if int(opcao) == 2:
        print('Recebendo texto de {} ...'.format(server_host_port), end=' ')
        texto_recebido = MetodosSocket.receber_texto(client_sock)
        sucesso = MetodosArquivos.escrever_dados_arquivo(CLIENT_FILE_PATH, texto_recebido)
        mensagem = 'Sucesso na gravação do texto no arquivo do cliente!' if sucesso \
            else 'Houve alguma falha na gravação do texto no arquivo do cliente!'
        print(mensagem)
        MetodosSocket.enviar_texto(mensagem, client_sock)


def autenticar(sock):
    MetodosSocket.enviar_texto(AUTHENTICATION_KEY, sock)
    resposta_autenticacao = MetodosSocket.receber_texto(sock)
    return resposta_autenticacao


if __name__ == '__main__':
    server_host = SERVER_HOST
    server_port = PORT
    args = sys.argv
    if len(args) == 2:
        server_host = args[1]
    elif len(args) == 3:
        server_host = args[1]
        try:
            server_port = int(args[2])
        except ValueError:
            print('A porta do servidor nao é um número!')
            sys.exit(1)

    client_sock = conectar_servidor(server_host, server_port)
    if autenticar(client_sock) == SUCCESS_AUTH_REPLY:
        transferir_mensagem_servidor(client_sock, server_host, server_port)
    else:
        print('Autenticação com o servidor falhou!')
