

"""
Adicionar objeto
"""

from part_1 import cursor
from utils.functions import *
from utils.labels import *
from models.hotel import Hotel


class ObjectAdd:

    @staticmethod
    def database_insert():
        while True:
            menu_creator(paint=True, move_to_right=True, right_px=50, menu_content=menu_add_object)
            this_input = input(operation)

            if this_input in allowed_numbers:

                if this_input == '0':
                    print(closure)
                    break
                elif this_input == '1':
                    # Para add objeto: tamanho = 5, senão:
                    print(add_object)
                    input_values = input(object_data)
                    allowed_data_length = len(input_values.split(','))

                    # Senão: inicia um loop, que recria o input até conseguir um que tenha 5 de tamanho
                    while allowed_data_length != 5:
                        code_block_init(error, attrib_numbers_warning, attrib_add_tutorial, attrib_example)
                        print(add_object)
                        input_values = input(object_data)
                        allowed_data_length = len(input_values.split(','))

                    # Se tiver tamanho 5: cria o objeto para adição ao banco
                    if allowed_data_length == 5:
                        box = input_values.split(',')
                        new_hotel = Hotel(hotel_id=box[0], name=box[1], stars=box[2], daily_charge=box[3], city=box[4])
                        print(object_report)
                        Hotel.database_insert(exec_=cursor, hotel_object=new_hotel)
                        print(input(roll))
                else:
                    code_block_init(error, warn.format(0, 1))
                    input(roll)
            else:
                code_block_init(error, warn.format(0, 1))
                input(roll)


if __name__ == '__main__':
    ObjectAdd.database_insert()
