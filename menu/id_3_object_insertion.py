

"""
Adicionar objeto
"""

from models.hotel import Hotel
from id_1_query import cursor
from utils.functions import (code_block_init, menu_creator)

from utils.labels import (
    closure, error, warn, roll, add_object, object_attribs, object_example, object_report, attrib_numbers_warning,
    avoid_special_characters, attrib_add_tutorial, menu_add_object, operation, object_data
)


class ObjectAdd:
    """
    ========== Parte 1 do algoritmo ==========
    1.0 - Exibição das opções disponíveis
    1.1 - Lançamento da entrada 1 p/ pedir uma escolha
    1.2 - Optar por encerrar o algoritmo
    1.3 - Prosseguir com a criação de um novo objeto do banco
    1.4 - Informar entrada inválida em relação as opções de entrada disponíveis
    1.5 - Inserir dados num iterável e contar sua quantidade, para saber se está no limite permitido
    1.6 - havendo a quantidade de índices correta, pegar os 5 índices e passar como novo objeto
    1.7 - Inserção do objeto ao banco e exibição
    1.8 - Informar erro do usuário e relançar a função que cria objeto novamente
    """

    @staticmethod
    def shut_it_down():
        print(closure)
        exit(0)

    def misleading_input(self):
        code_block_init(error, warn.format(0, 1))
        input(roll)
        ObjectAdd.algorithm_main_window(self)

    @staticmethod
    def how_to_create_new_object():
        code_block_init(add_object, object_attribs, object_example)

    def object_management(self):
        self.__values_as_tuple = self.__input_object_values.split(',')
        self.__data_length = len(self.__values_as_tuple)

    def hotel_validation_and_display(self):
        # 1.6
        new_hotel = Hotel(hotel_id=self.__values_as_tuple[0], name=self.__values_as_tuple[1],
                          stars=self.__values_as_tuple[2], daily_charge=self.__values_as_tuple[3],
                          city=self.__values_as_tuple[4])

        print(object_report)
        Hotel.database_insert(exec_=cursor, hotel_object=new_hotel)  # 1.7
        print(input(roll))
        ObjectAdd.algorithm_main_window(self)  # 1.8

    def misleading_object_data(self):
        # 1.8
        code_block_init(error, attrib_numbers_warning, avoid_special_characters, attrib_add_tutorial, object_example)
        input(roll)
        ObjectAdd.object_creation(self)

    # PRINCIPAIS
    def algorithm_main_window(self):
        menu_creator(paint=True, move_to_right=True, right_px=50, menu_content=menu_add_object)  # 1.0

        self.__input_launcher = input(operation)  # 1.1

        if self.__input_launcher == '0':  # 1.2
            ObjectAdd.shut_it_down()

        elif self.__input_launcher == '1':  # 1.3
            ObjectAdd.object_creation(self)

        else:  # 1.4
            ObjectAdd.misleading_input(self)

    def object_creation(self):

        # 1.5
        ObjectAdd.how_to_create_new_object()

        self.__input_object_values = input(object_data)

        ObjectAdd.object_management(self)

        if self.__data_length == self.__max_length:  # Se 5 índices
            ObjectAdd.hotel_validation_and_display(self)

        else:  # Tamanho != 5
            ObjectAdd.misleading_object_data(self)

    def __init__(self):
        self.__input_launcher = None
        self.__input_object_values = ''
        self.__values_as_tuple = None
        self.__data_length = None
        self.__input_length_object = 0
        self.__max_length = 5


if __name__ == '__main__':
    object_editable = ObjectAdd()
    object_editable.algorithm_main_window()
