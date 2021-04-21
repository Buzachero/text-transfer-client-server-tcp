from datetime import datetime


class MetodosData:
    @staticmethod
    def receber_data_hora_atual_formatada():
        data_hora_atual = datetime.now()
        data = data_hora_atual.strftime('%d/%m/%Y')
        hora = data_hora_atual.strftime('%H:%M:%S')
        return data, hora

    @staticmethod
    def prefixar_com_data_hora_atual(mensagem):
        (data, hora) = MetodosData.receber_data_hora_atual_formatada()
        return f'[{data} {hora}] {mensagem}'