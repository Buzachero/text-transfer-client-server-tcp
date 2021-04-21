import socket
import sys
from constants import *
from MetodosSocket import MetodosSocket
from MetodosData import MetodosData
from MetodosArquivo import MetodosArquivos

def receber_texto(client_sock, client_address):
    client_host_port = '{}:{}'.format(client_address[0], client_address[1])
    print('Recebendo texto de {} ...'.format(client_host_port))
    bytes_recv = client_sock.recv(8192)
    print('Texto recebido: {}'.format(bytes_recv.decode()))

def autenticar_cliente(client_sock, client_address):
    cliente_autenticado = False
    while cliente_autenticado == False:
        client_host_port = '{}:{}'.format(client_address[0], client_address[1])
        print('Conexão criada com {}'.format(client_host_port))
        authentication_key = MetodosSocket.receber_texto(client_sock)
        cliente_autenticado = validar_chave_autenticacao(authentication_key)
        if cliente_autenticado:
            MetodosSocket.enviar_texto(SUCCESS_AUTH_REPLY, client_sock)
        else:
            print(f'Falha de autenticação de {client_host_port} !')
            MetodosSocket.enviar_texto(FAILURE_AUTH_REPLY, client_sock)

    print(f'Cliente {client_host_port} autenticado com sucesso!')


def transferir_receber_texto_cliente(client_sock, client_address):
    client_host_port = '{}:{}'.format(client_address[0], client_address[1])
    while True:
        opcao = MetodosSocket.receber_texto(client_sock)
        if int(opcao) == 1:
            texto_arquivo = MetodosSocket.receber_texto(client_sock)
            sucesso = MetodosArquivos.escrever_dados_arquivo(SERVER_FILE_PATH, texto_arquivo)
            mensagem = 'Sucesso na gravação do texto no arquivo do servidor!' if sucesso \
                else 'Houve alguma falha na gravação do texto no arquivo do servidor!'
            MetodosSocket.enviar_texto(MetodosData.prefixar_com_data_hora_atual(mensagem), client_sock)
            break
        elif int(opcao) == 2:
            texto_arquivo = MetodosArquivos.ler_conteudo_arquivo(SERVER_FILE_PATH)
            print(MetodosData.prefixar_com_data_hora_atual('Enviando texto  para {} ...'.format(client_host_port)),
                  end=' ')
            MetodosSocket.enviar_texto(texto_arquivo, client_sock)
            print('Texto enviado!')
            break
    print('Fechando conexao ...')



def receber_conexao(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((host, port))
    sock.listen()
    print('Ouvindo na porta {} ...'.format(port), end=' ')
    (client_sock, client_address) = sock.accept()

    return client_sock, client_address

def validar_chave_autenticacao(chave):
    is_chave_valida = True
    if len(chave) < len(AUTHENTICATION_KEY):
        is_chave_valida = False
    if chave != AUTHENTICATION_KEY:
        is_chave_valida = False
        print(MetodosData.prefixar_com_data_hora_atual(f'Chave inválida! Envio de dados pelo host {host} não autorizado!'))
    return is_chave_valida

def formatar_mensagem_sem_chave(mensagem):
    if len(mensagem) < len(AUTHENTICATION_KEY):
        return mensagem
    return mensagem[len(AUTHENTICATION_KEY):len(mensagem)]


if __name__ == '__main__':
    host = SERVER_HOST
    port = PORT
    args = sys.argv
    if len(args) == 2:
        host = args[1]
    elif len(args) == 3:
        host = args[1]
        port = args[2]
    (client_sock, client_address) = receber_conexao(host, port)
    autenticar_cliente(client_sock, client_address)
    transferir_receber_texto_cliente(client_sock, client_address)