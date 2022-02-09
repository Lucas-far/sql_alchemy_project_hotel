

"""
Atualizar objeto
"""

from part_1 import cursor
from utils.functions import *
from utils.labels import *
from models.hotel import Hotel


class ObjectEdit:

    def is_database_empty(self):
        database_size = len(Hotel.database_as_var(exec_=cursor))

        if database_size == 0:
            code_block_init(error, empty_database)
            exit(0)
        else:
            ObjectEdit.object_update(self)

    def object_update(self):
        # Mostrar painel
        menu_creator(paint=True, move_to_right=False, right_px=0, menu_content=menu_edit_object)

        # Input de decisão de execução do algoritmo
        self.__input_launch = input(operation)

        # Encerrar
        if self.__input_launch == '0':
            print(closure)
            exit(0)
        # Continuar
        if self.__input_launch == '1':
            ObjectEdit.part_2(self)
        # Lançar erro e reinicar, até indicar a opção condizente
        else:
            code_block_init(error, warn.format(0, 1))
            ObjectEdit.object_update(self)

    def part_2(self):
        print(f'{"=" * 10} PARTE 2 {"=" * 10}')
        # Coletar o objeto por um input
        self.__input_hotel_id = input(hotel_id_name_to_edit)
        self.__hotel_data = Hotel.database_query_by_hotel_id(exec_=cursor, hotel_id=self.__input_hotel_id)

        if self.__hotel_data:
            # Se o objeto existe, manipular para mostrar somente os valores
            self.__number_attempts = 0
            self.__hotel_data = list(self.__hotel_data.values())
            self.__hotel_data = [{index: data} for index, data in enumerate(self.__hotel_data)]
            del self.__hotel_data[0]
            # Continuar
            ObjectEdit.part_3(self)

        if self.__number_attempts >= 3:
            # Lançar erro e parar o algoritmo
            code_block_init(error, attempts_exceeded.format(self.__number_attempts), search_in_the_database)
            self.__number_attempts = 0
            exit(0)

        # Abrir uma contagem, se errar 3 vezes, o algoritmo encerra
        if not self.__hotel_data:
            self.__number_attempts += 1
            code_block_init(error,
                            object_hotel_not_found.format(self.__input_hotel_id),
                            attempts_remaining.format(self.__number_attempts_max - self.__number_attempts))
            # repetir esta função
            ObjectEdit.part_2(self)

    def part_3(self):
        print(f'{"=" * 10} PARTE 3 {"=" * 10}')
        attribs_numbers = ('1', '2', '3', '4', '5')

        # Exibição dos dados tratados e exibidos na função anterior
        print(which_one)
        for each_attrib in self.__hotel_data:
            print(str(each_attrib))

        # Coletar o valor do atributo (1 a 5)
        self.__input_attrib_number = input(which_field)

        # Se a escolha estiver entre 1 a 5, continuar, senão, repetir esta função
        if self.__input_attrib_number in attribs_numbers:
            ObjectEdit.part_4(self)
        else:
            ObjectEdit.part_3(self)

    def part_4(self):
        # Mostrar o atributo escolhido, para ajudar
        print(attrib_chosen.format(ink(self.__hotel_data[int(self.__input_attrib_number) - 1])))

        # Variáveis de ajuda para fazer um loop for de condição
        index = 0
        attribs_numbers = ('1', '2', '3', '4', '5')
        attribs = ('hotel_id', 'name', 'stars', 'daily_charge', 'city')

        # Informar o novo valor do atributo
        self.__input_new_attrib_value = input(new_value)

        # Loop que faz a atualização de acordo com as informações passadas
        while index < len(attribs_numbers):
            if self.__input_attrib_number == attribs_numbers[index]:
                Hotel.to_update(exec_=cursor,
                                hotel_id=self.__input_hotel_id,
                                _key=attribs[index],
                                _value=self.__input_new_attrib_value)
                input(roll)
                # Reiniciar algoritmo
                ObjectEdit.object_update(self)
            else:
                index += 1

        # if self.__input_attrib_number == attribs_numbers[0]:
        #     Hotel.to_update(exec_=cursor,
        #                     hotel_id=self.__input_hotel_id,
        #                     _key=attribs[0],
        #                     _value=self.__input_new_attrib_value)
        #     input(roll)
        #     ObjectEdit.object_edit(self)
        #     menu_creator(paint=True, move_to_right=True, right_px=50, menu_content=menu_edit_object)
        # elif self.__input_attrib_number == attribs_numbers[1]:
        #     Hotel.to_update(exec_=cursor,
        #                     hotel_id=self.__input_hotel_id,
        #                     _key=attribs[1],
        #                     _value=self.__input_new_attrib_value)
        #     input(roll)
        #     ObjectEdit.object_edit(self)
        #     menu_creator(paint=True, move_to_right=True, right_px=50, menu_content=menu_edit_object)
        # elif self.__input_attrib_number == attribs_numbers[2]:
        #     Hotel.to_update(exec_=cursor,
        #                     hotel_id=self.__input_hotel_id,
        #                     _key=attribs[2],
        #                     _value=self.__input_new_attrib_value)
        #     input(roll)
        #     ObjectEdit.object_edit(self)
        #     menu_creator(paint=True, move_to_right=True, right_px=50, menu_content=menu_edit_object)
        # elif self.__input_attrib_number == attribs_numbers[3]:
        #     Hotel.to_update(exec_=cursor,
        #                     hotel_id=self.__input_hotel_id,
        #                     _key=attribs[3],
        #                     _value=self.__input_new_attrib_value)
        #     input(roll)
        #     ObjectEdit.object_edit(self)
        #     menu_creator(paint=True, move_to_right=True, right_px=50, menu_content=menu_edit_object)
        # elif self.__input_attrib_number == attribs_numbers[4]:
        #     Hotel.to_update(exec_=cursor,
        #                     hotel_id=self.__input_hotel_id,
        #                     _key=attribs[4],
        #                     _value=self.__input_new_attrib_value)
        #     input(roll)
        #     ObjectEdit.object_edit(self)
        #     menu_creator(paint=True, move_to_right=True, right_px=50, menu_content=menu_edit_object)

    def __init__(self):
        self.__input_launch = None
        self.__input_hotel_id = None
        self.__input_attrib_number = None
        self.__input_new_attrib_value = None
        self.__hotel_data = None
        self.__number_attempts = 0
        self.__number_attempts_max = 3


if __name__ == '__main__':
    object_edit = ObjectEdit()
    object_edit.is_database_empty()
