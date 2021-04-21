class MetodosArquivos:
    @staticmethod
    def escrever_dados_arquivo(nome_arquivo, dados):
        try:
            file = open(nome_arquivo, 'w')
            file.write(str(dados))
        except PermissionError:
            raise PermissionError(f'O arquivo \'{nome_arquivo}\' não tem permissão para escrita!')
            escrita_sucesso = False
        except Exception as ex:
            print('Falha na escrita do arquivo {}: {}'.format(nome_arquivo, ex))
            escrita_sucesso = False
        else:
            print('Sucesso na escrita do arquivo {}'.format(nome_arquivo))
            escrita_sucesso = True
        finally:
            file.close()
        return escrita_sucesso

    @staticmethod
    def ler_conteudo_arquivo(nome_arquivo):
        try:
            with open(nome_arquivo) as file:
                return file.read()
        except FileNotFoundError:
            raise FileNotFoundError(f'O arquivo \'{nome_arquivo}\' não existe!')
        except PermissionError:
            raise PermissionError(f'O arquivo \'{nome_arquivo}\' não tem permissão para leitura!')
        except Exception as ex:
            print(f'Falha na leitura do arquivo \'{nome_arquivo}\': {ex}')
