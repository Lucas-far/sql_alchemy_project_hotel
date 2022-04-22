

from menu.part_1 import DatabaseQuery
from menu.part_2 import DatabaseQuerySpecific
from menu.part_3 import ObjectAdd
from menu.part_4 import ObjectEdit
from menu.part_5 import ObjectDelete
from utils.functions import code_block_init, ink, menu_creator
from utils.labels import *


class Menu:
    def database_management(self):
        menu_creator(paint=True, move_to_right=False, right_px=0, menu_content=menu_main)
        self.__main_input = input(operation)

        if self.__main_input == '0':
            print(closure)
            exit(0)

        elif self.__main_input == '1':
            DatabaseQuery.database_view()
            Menu.database_management(self)

        elif self.__main_input == '2':
            an_object = DatabaseQuerySpecific()
            an_object.query_database_data()

        elif self.__main_input == '3':
            an_object = ObjectAdd()
            an_object.database_insert()

        elif self.__main_input == '4':
            an_object = ObjectEdit()
            an_object.object_update()

        elif self.__main_input == '5':
            an_object = ObjectDelete()
            an_object.object_delete()

        else:
            code_block_init(error, warn.format(1, 5))
            Menu.database_management(self)

    def __init__(self):
        self.__main_input = None


if __name__ == '__main__':
    manager_object = Menu()
    manager_object.database_management()
