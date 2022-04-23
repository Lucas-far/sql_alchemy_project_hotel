
"""
Consultar banco
"""

from models.hotel import Hotel
from utils.functions import (code_block_init, menu_creator)

from utils.labels import (
    operation, closure, roll, error, warn
)

engine_test = Hotel.database_config(name='db.db')
cursor = Hotel.database_cursor(engine=engine_test)
Hotel.database_init(engine=engine_test)


class DatabaseQuery:
    """
    ========== Parte 1 do algoritmo ==========
    1.0 - Exibição das opções disponíveis
    1.1 - Lançamento da entrada 1 p/ pedir uma escolha
    1.2 - Optar por encerrar o algoritmo
    1.3 - Mostrar o banco de dados
    1.4 - Mostrar erro, e instruir para as opções certas
    """

    # TODO
    menu = (
        '\n========== VISUALIZAR DADOS DO BANCO ==========',
        'Encerrar sessão   || aperte 0',
        'Vizualizar banco  || aperte 1',
        'Sair sem encerrar || aperte 2'
    )

    @staticmethod
    def database_view():
        menu_creator(paint=False, move_to_right=False, right_px=0, menu_content=DatabaseQuery.menu)  # 1.0
        this_input = input(operation)  # 1.1

        if this_input == '0':  # 1.2
            DatabaseQuery.shut_it_down()

        elif this_input == '1':  # 1.3
            DatabaseQuery.show_database_content()

        # TODO: Controlar o algoritmo principal (dar uma opção de retorno ao menu principal sem encerrar)
        elif this_input == '2':
            from menu.main_menu import manager_object
            manager_object.database_full_management()

        else:  # 1.4
            DatabaseQuery.misleading_input()

    @staticmethod
    def shut_it_down():
        print(closure)
        exit(0)

    @staticmethod
    def show_database_content():
        Hotel.database_query(exec_=cursor)
        input(roll)
        DatabaseQuery.database_view()

    @staticmethod
    def misleading_input():
        code_block_init(error, warn.format(0, 1))
        input(roll)
        DatabaseQuery.database_view()


if __name__ == '__main__':
    DatabaseQuery.database_view()
