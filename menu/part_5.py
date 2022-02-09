

"""
Deletar objeto
"""

from part_1 import cursor
from utils.functions import *
from utils.labels import *
from models.hotel import Hotel


class ObjectDelete:

    def is_database_empty(self):
        database_size = len(Hotel.database_as_var(exec_=cursor))

        if database_size == 0:
            code_block_init(error, empty_database)
            exit(0)
        else:
            ObjectDelete.object_delete(self)

    def object_delete(self):
        menu_creator(paint=True, move_to_right=False, right_px=0, menu_content=menu_delete_object)
        self.__input_launcher = input(operation)

        if self.__input_launcher == '0':
            print(closure)
            exit(0)
        if self.__input_launcher == '1':
            ObjectDelete.part_2(self)  # prosseguir
        else:
            code_block_init(error, warn.format(0, 1))  # erro
            ObjectDelete.object_delete(self)  # repete a função

    def part_2(self):
        self.__input_hotel_id = input(hotel_id_name_to_edit)
        self.__hotel_data = Hotel.database_query_by_hotel_id(exec_=cursor, hotel_id=self.__input_hotel_id)

        if self.__hotel_data:
            self.__number_attempts = 0
            ObjectDelete.part_3(self)  # prosseguir

        if self.__number_attempts >= 3:
            code_block_init(error, attempts_exceeded.format(self.__number_attempts), search_in_the_database)
            self.__number_attempts = 0
            exit(0)

        if not self.__hotel_data:
            self.__number_attempts += 1
            code_block_init(error,
                            object_hotel_not_found.format(self.__input_hotel_id),
                            attempts_remaining.format(self.__number_attempts_max - self.__number_attempts))
            ObjectDelete.part_2(self)   # repetir esta função

    def part_3(self):
        code_block_init(delete_object_label, object_to_be_deleted, self.__hotel_data)
        self.__decision = input(ask_if_remove)

        if self.__decision == '0':
            code_block_init(announcement, object_removal_canceled)
            ObjectDelete.object_delete(self)                               # reiniciar algoritmo
        elif self.__decision == '1':
            Hotel.to_delete(exec_=cursor, hotel_id=self.__input_hotel_id)  # remover objeto
            ObjectDelete.object_delete(self)                               # reiniciar algoritmo
        else:
            code_block_init(error, warn.format(0, 1))
            ObjectDelete.part_3(self)                                      # reiniciar esta função

    def __init__(self):
        self.__input_launcher = None
        self.__input_hotel_id = None
        self.__hotel_data = None
        self.__decision = None
        self.__number_attempts = 0
        self.__number_attempts_max = 3

    @staticmethod
    def to_delete_from_database():

        hotel_data = False
        input_hotel_id_outer = None
        input_remove_object = None
        allowed_numbers = ('0', '1')

        while True:
            menu_creator(paint=True, move_to_right=True, right_px=50, menu_content=menu_delete_object)
            this_input = input(operation)

            if this_input in allowed_numbers:
                if this_input == '0':
                    print(closure)
                    break
                elif this_input == '1':
                    while not hotel_data:
                        print(delete_object_label)
                        input_hotel_id = input(hotel_id_name)
                        input_hotel_id_outer = input_hotel_id
                        hotel_data = Hotel.database_query_by_hotel_id(exec_=cursor, hotel_id=input_hotel_id)
                        if not hotel_data:
                            code_block_init(error, object_hotel_not_found.format(input_hotel_id_outer))
                    else:
                        code_block_init(object_to_be_deleted, hotel_data)
                        while input_remove_object not in allowed_numbers:
                            input_remove_object = input(ask_if_remove)
                            if input_remove_object == '0':
                                code_block_init(announcement, object_removal_canceled)
                                break
                            elif input_remove_object == '1':
                                # code_block_init(object_deleted_label, hotel_data)
                                Hotel.to_delete(exec_=cursor, hotel_id=input_hotel_id_outer)
                                input(roll)
                                break
                            else:
                                code_block_init(object_to_be_deleted, hotel_data)
                else:
                    code_block_init(error, object_hotel_not_found.format(input_hotel_id_outer))
                    input(roll)
            else:
                code_block_init(error, warn.format(0, 1))
                input(roll)


if __name__ == '__main__':
    object_exclusion = ObjectDelete()
    object_exclusion.is_database_empty()
