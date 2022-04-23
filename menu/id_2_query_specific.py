

"""
Pesquisar objeto de forma específica: pelo
"""

from models.hotel import Hotel
from id_1_query import cursor

from utils.functions import (
    code_block_init, menu_creator
)

from utils.labels import (
    operation,
    closure,
    error, warn, roll,
    ask_hotel_id_name,
    query_result,
    attempts_exceeded, search_in_the_database,
    object_hotel_not_found, attempts_remaining,
)


class DatabaseQuerySpecific:

    # TODO
    menu = (
        '\n========== PESQUISA DE OBJETO ==========',
        'Encerrar sessão  || aperte 0',
        'Iniciar pesquisa || aperte 1',
        'Sair sem encerrar || aperte 2'
    )

    # PARTE 1
    def algorithm_main_window(self):
        """
        1.0 - Exibição das opções disponíveis
        1.1 - Lançamento da entrada 1 p/ pedir uma escolha
        1.2 - Optar por encerrar o algoritmo
        1.3 - Optar por pesquisar algum id de hotel
        1.4 - Informar opção inválida e retorno à janela principal
        """

        menu_creator(paint=False, move_to_right=True, right_px=50, menu_content=DatabaseQuerySpecific.menu)  # 1.0

        self.__input_launcher = input(operation)  # 1.1

        if self.__input_launcher == '0':  # 1.2
            DatabaseQuerySpecific.shut_it_down()

        elif self.__input_launcher == '1':  # 1.3
            DatabaseQuerySpecific.display_query_content(self)

        # TODO: Controlar o algoritmo principal (dar uma opção de retorno ao menu principal sem encerrar)
        elif self.__input_launcher == '2':
            from menu.main_menu import manager_object
            manager_object.database_full_management()

        else:  # 1.4
            DatabaseQuerySpecific.misleading_input(self)

    @staticmethod
    def shut_it_down():
        print(closure)
        exit(0)

    def misleading_input(self):
        code_block_init(error, warn.format(0, 1))
        input(roll)
        DatabaseQuerySpecific.algorithm_main_window(self)

    # PARTE 2
    def display_query_content(self):
        """
        1.5 - Lançamento da entrada 2 para saber se ela é == a algum atributo 2 dentre os objetos do modelo/banco

        1.6 - Função em "models/hotel.py" responsável pela pesquisa, que recebe a entrada 2
              (retorno: objeto json ou None)

        1.7 - Quando o atributo 2 de algum objeto do banco == entrada 2 (objeto achado)
              Resetar contagem de erros, exibir resultado do pesquisa e oferecer um comando de retorno à janela principal

        1.8 - Entrada 2 != todos os atributo "hotel_id" dos objetos do banco + contagem de erros excedida
              Encerramento do algoritmo e pedido ao usuário para consultar o banco

        1.9 - Entrada 2 != todos os atributo "hotel_id" dos objetos do banco + contagem de erros iniciada
              Entrada 2 reseta conforme a função repete (máx. de 3 repetições)
        """

        self.__input_hotel_id = input(ask_hotel_id_name)  # 1.5

        hotel_object_hotel_id = Hotel.database_query_by_hotel_id(exec_=cursor, hotel_id=self.__input_hotel_id)  # 1.6

        if hotel_object_hotel_id:  # 1.7
            DatabaseQuerySpecific.hotel_id_found(self, hotel_query_var=hotel_object_hotel_id)

        if self.__number_attempts >= 3:  # 1.8
            DatabaseQuerySpecific.max_mistakes_reached(self)

        else:  # 1.9
            DatabaseQuerySpecific.throw_new_search_attempt(self)

    def hotel_id_found(self, hotel_query_var):
        self.__number_attempts = 0
        code_block_init(query_result, hotel_query_var)
        input(roll)
        DatabaseQuerySpecific.algorithm_main_window(self)

    def max_mistakes_reached(self):
        self.__number_attempts = 0
        code_block_init(error, attempts_exceeded, search_in_the_database)
        exit(0)

    def throw_new_search_attempt(self):
        self.__number_attempts += 1
        code_block_init(error,
                        object_hotel_not_found.format(self.__input_hotel_id),
                        attempts_remaining.format(self.__number_attempts_max - self.__number_attempts))
        DatabaseQuerySpecific.display_query_content(self)

    def __init__(self):
        self.__input_launcher = None
        self.__input_hotel_id = None
        self.__number_attempts = 0
        self.__number_attempts_max = 3


if __name__ == '__main__':
    hotel_object_search = DatabaseQuerySpecific()
    hotel_object_search.algorithm_main_window()
