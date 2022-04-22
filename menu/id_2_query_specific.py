

"""
Pesquisar objeto de forma específica: pelo
"""

from models.hotel import Hotel
from id_1_query import cursor
from utils.functions import (code_block_init, menu_creator)

from utils.labels import (
    menu_search_object, result, attempts_exceeded, search_in_the_database, object_hotel_not_found, attempts_remaining,
    hotel_id_name, operation, closure, roll, error, warn
)


class DatabaseQuerySpecific:
    """
    ========== Parte 1 do algoritmo ==========
    1.0 - Exibição das opções disponíveis
    1.1 - Lançamento da entrada 1 p/ pedir uma escolha
    1.2 - Optar por encerrar o algoritmo
    1.3 - Optar por pesquisar algum id de hotel
    1.4 - Informar opção inválida e retorno à janela principal (parte 1 do algoritmo)

    ========== Parte 2 do algoritmo ==========
    1.5 - Lançamento da entrada 2 para saber se ela é == a algum atributo 2 dentre os objetos do modelo/banco
    1.6 - Função em "models/hotel.py" responsável pela pesquisa, que recebe a entrada 2 (retorno: objeto json ou None)

    1.7 - Quando o atributo 2 de algum objeto do banco == entrada 2 (objeto achado)
          Resetar contagem de erros, exibir resultado do pesquisa e oferecer um comando de retorno à janela principal

    1.8 - Quando a entrada 2 for incompatível com todos os atributo 2 dos objetos do banco + contagem de erros excedida
          Encerramento do algoritmo e pedido ao usuário para consultar o banco

    1.9 - Quando a entrada 2 for incompatível com todos os atributo 2 dos objetos do banco + início da contagem
          Entrada 2 reseta conforme a função repete (máx. de 3 repetições)
    """

    @staticmethod
    def shut_it_down():
        print(closure)
        exit(0)

    @staticmethod
    def misleading_input():
        code_block_init(error, warn.format(0, 1))
        input(roll)

    def hotel_id_found(self, hotel_query_var):
        self.__number_attempts = 0
        code_block_init(result, hotel_query_var)
        input(roll)
        DatabaseQuerySpecific.query_init(self)

    def shut_it_down_by_attempts(self):
        self.__number_attempts = 0
        code_block_init(error, attempts_exceeded, search_in_the_database)
        exit(0)

    def try_again(self):
        self.__number_attempts += 1
        code_block_init(error,
                        object_hotel_not_found.format(self.__input_hotel_id),
                        attempts_remaining.format(self.__number_attempts_max - self.__number_attempts))
        DatabaseQuerySpecific.query_content(self)

    # PRINCIPAIS
    def query_init(self):
        menu_creator(paint=True, move_to_right=True, right_px=50, menu_content=menu_search_object)  # 1.0

        self.__input_launcher = input(operation)  # 1.1

        if self.__input_launcher == '0':  # 1.2
            DatabaseQuerySpecific.shut_it_down()

        if self.__input_launcher == '1':  # 1.3
            DatabaseQuerySpecific.query_content(self)

        else:  # 1.4
            DatabaseQuerySpecific.misleading_input()
            DatabaseQuerySpecific.query_init(self)

    def query_content(self):
        self.__input_hotel_id = input(hotel_id_name)  # 1.5

        hotel_object_hotel_id = Hotel.database_query_by_hotel_id(exec_=cursor, hotel_id=self.__input_hotel_id)  # 1.6

        if hotel_object_hotel_id:  # 1.7
            DatabaseQuerySpecific.hotel_id_found(self, hotel_query_var=hotel_object_hotel_id)

        if self.__number_attempts >= 3:  # 1.8
            DatabaseQuerySpecific.shut_it_down_by_attempts(self)

        else:  # 1.9
            DatabaseQuerySpecific.try_again(self)

    def __init__(self):
        self.__input_launcher = None
        self.__input_hotel_id = None
        self.__number_attempts = 0
        self.__number_attempts_max = 3


if __name__ == '__main__':
    hotel_object_search = DatabaseQuerySpecific()
    hotel_object_search.query_init()
