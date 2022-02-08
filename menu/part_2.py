

"""
Pesquisar objeto
"""

from part_1 import cursor
from utils.functions import *
from utils.labels import *
from models.hotel import Hotel


class DatabaseQuerySpecific:

    @staticmethod
    def query_database_data():
        while True:
            menu_creator(paint=True, move_to_right=True, right_px=50, menu_content=menu_search_object)
            this_input = input(operation)

            if this_input in allowed_numbers:

                if this_input == '0':
                    print(closure)
                    break
                elif this_input == '1':
                    print(search)
                    target = input(hotel_id_name)
                    hotel_object_hotel_id = Hotel.database_query_by_hotel_id(exec_=cursor, hotel_id=target)
                    code_block_init(result, hotel_object_hotel_id)
                    input(roll)
                else:
                    code_block_init(error, warn.format(0, 1))
                    input(roll)
            else:
                code_block_init(error, warn.format(0, 1))
                input(roll)


if __name__ == '__main__':
    DatabaseQuerySpecific.query_database_data()
