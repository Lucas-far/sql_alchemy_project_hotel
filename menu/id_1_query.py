
"""
Consultar banco
"""

from models.hotel import Hotel
from utils.functions import (code_block_init, menu_creator)

from utils.labels import (
    menu_see_database, operation, closure, roll, error, warn
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

    @staticmethod
    def database_view():
        menu_creator(paint=True, move_to_right=False, right_px=0, menu_content=menu_see_database)  # 1.0
        this_input = input(operation)  # 1.1

        if this_input == '0':  # 1.2
            DatabaseQuery.shut_it_down()

        elif this_input == '1':  # 1.3
            DatabaseQuery.show_database_content()

        else:  # 1.4
            DatabaseQuery.misleading_input()


if __name__ == '__main__':
    DatabaseQuery.database_view()
