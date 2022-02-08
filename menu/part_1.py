

"""
Consultar banco
"""

from utils.functions import *
from utils.labels import *
from models.hotel import Hotel

engine_test = Hotel.database_config(name='db.db')
cursor = Hotel.database_cursor(engine=engine_test)
Hotel.database_init(engine=engine_test)


class DatabaseQuery:

    @staticmethod
    def database_view():
        while True:
            menu_creator(paint=True, move_to_right=True, right_px=50, menu_content=menu_see_database)
            this_input = input(operation)

            if this_input in allowed_numbers:

                if this_input == '0':
                    print(closure)
                    break
                elif this_input == '1':
                    Hotel.database_query(exec_=cursor)
                    input(roll)
                else:
                    code_block_init(error, warn.format(0, 1))
                    input(roll)
            else:
                code_block_init(error, warn.format(0, 1))
                input(roll)


if __name__ == '__main__':
    DatabaseQuery.database_view()
