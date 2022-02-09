

"""
Pesquisar objeto
"""

from part_1 import cursor
from utils.functions import *
from utils.labels import *
from models.hotel import Hotel


class DatabaseQuerySpecific:

    def query_database_data(self):
        menu_creator(paint=True, move_to_right=True, right_px=50, menu_content=menu_search_object)
        self.__input_launcher = input(operation)

        if self.__input_launcher == '0':
            print(closure)
            exit(0)
        if self.__input_launcher == '1':
            DatabaseQuerySpecific.part_2(self)
        else:
            code_block_init(error, warn.format(0, 1))
            input(roll)
            DatabaseQuerySpecific.query_database_data(self)

    def part_2(self):
        self.__input_hotel_id = input(hotel_id_name)
        hotel_object_hotel_id = Hotel.database_query_by_hotel_id(exec_=cursor, hotel_id=self.__input_hotel_id)

        if hotel_object_hotel_id:
            self.__number_attempts = 0
            code_block_init(result, hotel_object_hotel_id)
            input(roll)
            DatabaseQuerySpecific.query_database_data(self)

        if self.__number_attempts >= 3:
            code_block_init(error, attempts_exceeded.format(self.__number_attempts), search_in_the_database)
            self.__number_attempts = 0
            exit(0)

        else:
            self.__number_attempts += 1
            code_block_init(error,
                            object_hotel_not_found.format(self.__input_hotel_id),
                            attempts_remaining.format(self.__number_attempts_max - self.__number_attempts))
            DatabaseQuerySpecific.part_2(self)

    @property
    def input_launcher(self):
        return self.__input_launcher

    @input_launcher.setter
    def input_launcher(self, new):
        self.__input_launcher = new

    @property
    def input_hotel_id(self):
        return self.__input_hotel_id

    @input_hotel_id.setter
    def input_hotel_id(self, new):
        self.__input_hotel_id = new

    def __init__(self, input_launcher, input_hotel_id):
        self.__input_launcher = input_launcher
        self.__input_hotel_id = input_hotel_id
        self.__number_attempts = 0
        self.__number_attempts_max = 3


if __name__ == '__main__':
    hotel_object_search = DatabaseQuerySpecific(input_launcher=None, input_hotel_id=None)
    hotel_object_search.query_database_data()
