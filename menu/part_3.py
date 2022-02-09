

"""
Adicionar objeto
"""

from part_1 import cursor
from utils.functions import *
from utils.labels import *
from models.hotel import Hotel


class ObjectAdd:

    def database_insert(self):
        # Mostrar informações
        menu_creator(paint=True, move_to_right=True, right_px=50, menu_content=menu_add_object)

        # Pergunta se quer executar a tarefa
        self.__input_launcher = input(operation)

        # Encerrar sessão
        if self.__input_launcher == '0':
            print(closure)
            exit(0)

        # Prosseguir com o algoritmo
        elif self.__input_launcher == '1':
            ObjectAdd.part_2(self)

        # Opção diferente das acima, lançar erro informando as opções permitidas, reiniciar algoritmo
        else:
            code_block_init(error, warn.format(0, 1))
            input(roll)
            ObjectAdd.database_insert(self)

    def part_2(self):

        # Informar os dados do objeto, verificar se o tamanho está certo
        print(add_object)
        self.__input_object_values = input(object_data)
        self.__values_as_tuple = self.__input_object_values.split(',')
        self.__data_length = len(self.__values_as_tuple)

        # Tamanho == 5
        if self.__data_length == self.__max_length:

            # Pegar os 5 índices e passar como novo objeto
            new_hotel = Hotel(hotel_id=self.__values_as_tuple[0], name=self.__values_as_tuple[1],
                              stars=self.__values_as_tuple[2], daily_charge=self.__values_as_tuple[3],
                              city=self.__values_as_tuple[4])

            # Objeto criado com o tamanho certo, inserido ao banco
            print(object_report)
            Hotel.database_insert(exec_=cursor, hotel_object=new_hotel)
            print(input(roll))
            ObjectAdd.database_insert(self)  # reiniciar algoritmo

        # Tamanho != 5
        else:
            code_block_init(error, attrib_numbers_warning, avoid_special_characters, attrib_add_tutorial, attrib_example)
            input(roll)
            ObjectAdd.part_2(self)  # reiniciar esta função

    def __init__(self):
        self.__input_launcher = None
        self.__input_object_values = ''
        self.__values_as_tuple = None
        self.__data_length = None
        self.__input_length_object = 0
        self.__max_length = 5


if __name__ == '__main__':
    object_editable = ObjectAdd()
    object_editable.database_insert()
