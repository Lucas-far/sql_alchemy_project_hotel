

"""
Deletar objeto
"""

from models.hotel import Hotel
from id_1_query import cursor

from utils.functions import (
    code_block_init, menu_creator
)

from utils.labels import (
    roll,
    error, empty_database,
    operation,
    closure,
    warn,
    type_hotel_id_to_be_deleted,
    attempts_exceeded, search_in_the_database,
    object_hotel_not_found, attempts_remaining,
    ask_if_remove,
    query_result,
    announcement, object_removal_canceled
)

# TODO: Na função "is_database_empty()" a função built in "exit(0)" foi comentada para impedir a encerramento direto
# TODO: A função foi substituída por um "input" e uma repetição
# TODO: A função "exit(0)" não representa um erro, ela apenas não serve para o novo contexto
# TODO: Os outros "todo" deste módulos mostram as mudanças feitas


class ObjectDelete:
    """
    1.0 - Var com os dados do banco (uso da função do modelo). Se essa var estiver vazia, o algitmo encerra
    1.1 - Havendo algum objeto, este pode ser editado, portanto o algoritmo pode ser iniciado
    1.2 - Exibição das opções disponíveis
    1.3 - Lançamento da entrada 1 p/ pedir uma escolha
    1.4 - Optar por encerrar o algoritmo
    1.5 - Prosseguir com a remoção de algum dos objeto do banco
    1.6 - Informar entrada inválida em relação as opções de entrada disponíveis
    1.7 - Lançamento da entrada 2 p/ requisitar o atributo "hotel_id" de um objeto (forma de busca deste algoritmo)
    1.8 - Uso de uma função do modelo, que recebe a entrada como argumento, para busca do atributo no banco
    1.9 - Se dentro os objetos do banco, o seu atributo "hotel_id" == entrada 2. Iniciar o procedimento de remoção
    2.0 - Impedir o usuário de prosseguir em caso de erros de pesquisa contínuos
    2.1 - Lançar contagem de erros caso o banco não consiga encontrar o que o usuário está pesquisando como "hotel_id"
    2.2 - Exibir informações da consulta com sucesso + exibição do objeto encontrado
    2.3 - Optar por não deletar o objeto do banco
    2.4 - Uso da função do modelo para remover o objeto do banco
    2.5 - Tratamento das opções do menu, impedindo o usuário de avançar caso não forneça uma das opções disponíveis
    """

    menu = (
        '\n========== REMOÇÃO DE OBJETO ==========',
        'Encerrar sessão   || aperte 0',
        'Deletar dado      || aperte 1',
        'Sair sem encerrar || aperte 2'
    )

    # PARTE 1
    def is_database_empty(self):
        database_size = len(Hotel.database_as_var(exec_=cursor))  # 1.0

        if database_size == 0:
            code_block_init(error, empty_database)
            input(roll)
            ObjectDelete.is_database_empty(self)
            # exit(0)

        else:  # 1.1
            ObjectDelete.algorithm_main_window(self)

    # PARTE 2
    def algorithm_main_window(self):
        menu_creator(paint=False, move_to_right=False, right_px=0, menu_content=ObjectDelete.menu)  # 1.2

        self.__input_launcher = input(operation)  # 1.3

        if self.__input_launcher == '0':  # 1.4
            ObjectDelete.shut_it_down()

        if self.__input_launcher == '1':  # 1.5
            ObjectDelete.object_hotel_id_seek(self)

        # TODO: Controlar o algoritmo principal (dar uma opção de retorno ao menu principal sem encerrar)
        elif self.__input_launcher == '2':
            from menu.main_menu import manager_object
            manager_object.database_full_management()

        else:  # 1.6
            ObjectDelete.misleading_input(self)

    @staticmethod
    def shut_it_down():
        print(closure)
        exit(0)

    def misleading_input(self):
        code_block_init(error, warn.format(0, 1))
        ObjectDelete.algorithm_main_window(self)

    # PARTE 3
    def object_hotel_id_seek(self):
        self.__input_hotel_id = input(type_hotel_id_to_be_deleted)  # 1.7
        self.__hotel_data = Hotel.database_query_by_hotel_id(exec_=cursor, hotel_id=self.__input_hotel_id)  # 1.8

        if self.__hotel_data:  # 1.9
            self.__number_attempts = 0
            ObjectDelete.object_removal(self)

        if self.__number_attempts >= 3:  # 2.0
            ObjectDelete.max_mistakes_reached(self)

        if not self.__hotel_data:  # 2.1
            ObjectDelete.throw_new_search_attempt(self)

    def max_mistakes_reached(self):
        self.__number_attempts = 0
        code_block_init(error, attempts_exceeded, search_in_the_database)
        exit(0)

    def throw_new_search_attempt(self):
        self.__number_attempts += 1
        code_block_init(error,
                        object_hotel_not_found.format(self.__input_hotel_id),
                        attempts_remaining.format(self.__number_attempts_max - self.__number_attempts))
        ObjectDelete.object_hotel_id_seek(self)

    # PARTE 4
    def object_removal(self):
        ObjectDelete.hotel_id_found(self)  # 2.2

        self.__decision = input(ask_if_remove)

        if self.__decision == '0':  # 2.3
            ObjectDelete.hotel_id_removal_aborted(self)

        elif self.__decision == '1':  # 2.4
            ObjectDelete.hotel_id_removal(self)

        else:  # 2.5
            ObjectDelete.misleading_decision(self)

    def hotel_id_found(self):
        code_block_init(query_result, self.__hotel_data)

    def hotel_id_removal_aborted(self):
        code_block_init(announcement, object_removal_canceled)
        ObjectDelete.algorithm_main_window(self)

    def hotel_id_removal(self):
        Hotel.to_delete(exec_=cursor, hotel_id=self.__input_hotel_id)
        ObjectDelete.algorithm_main_window(self)

    def misleading_decision(self):
        code_block_init(error, warn.format(0, 1))
        ObjectDelete.object_removal(self)

    def __init__(self):
        self.__input_launcher = None
        self.__input_hotel_id = None
        self.__hotel_data = None
        self.__decision = None
        self.__number_attempts = 0
        self.__number_attempts_max = 3


if __name__ == '__main__':
    object_exclusion = ObjectDelete()
    object_exclusion.is_database_empty()
