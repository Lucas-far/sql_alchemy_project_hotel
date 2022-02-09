

"""
Atualizar objeto
"""

from part_1 import cursor
from utils.functions import *
from utils.labels import *
from models.hotel import Hotel


class ObjectEdit:

    @property
    def input_launch(self):
        return self.__input_launch

    @property
    def input_hotel_id(self):
        return self.__input_hotel_id

    @property
    def input_attrib_number(self):
        return self.__input_attrib_number

    @property
    def input_new_attrib_value(self):
        return self.__input_new_attrib_value

    @input_launch.setter
    def input_launch(self, new):
        self.__input_launch = new

    @input_hotel_id.setter
    def input_hotel_id(self, new):
        self.__input_hotel_id = new

    @input_attrib_number.setter
    def input_attrib_number(self, new):
        self.__input_attrib_number = new

    @input_new_attrib_value.setter
    def input_new_attrib_value(self, new):
        self.__input_new_attrib_value = new

    def algorithm_launch(self):
        print(f'{"=" * 10} PARTE 1 {"=" * 10}')
        menu_creator(paint=True, move_to_right=False, right_px=0, menu_content=menu_edit_object)
        self.__input_launch = input(operation)

        if self.__input_launch == '0':
            print(closure)
            exit(0)
        if self.__input_launch == '1':
            ObjectEdit.part_2(self)                    # prosseguir
        else:
            code_block_init(error, warn.format(0, 1))  # erro
            ObjectEdit.algorithm_launch(self)                    # repete a função

    def part_2(self):
        print(f'{"=" * 10} PARTE 2 {"=" * 10}')
        self.__input_hotel_id = input(hotel_id_name_to_edit)
        hotel_data = Hotel.database_query_by_hotel_id(exec_=cursor, hotel_id=self.__input_hotel_id)

        if hotel_data:
            self.__hotel_data = hotel_data  # para uso na função seguinte
            self.__hotel_data = list(self.__hotel_data.values())
            self.__hotel_data = [{index: data} for index, data in enumerate(self.__hotel_data)]
            del self.__hotel_data[0]

            # ObjectEdit.input_2nd.append(self.__input_hotel_id)  # guardar o input 2 (sucesso)
            ObjectEdit.part_3(self)  # prosseguir

        # Se não souber o nome de id: abrir um número de tentativas e lançar erro de aviso
        if not hotel_data:
            # ObjectEdit.input_hotel_id = None
            code_block_init(error, object_hotel_not_found.format(self.__input_hotel_id))  # erro
            ObjectEdit.part_2(self)  # repete a função

    def part_3(self):
        print(f'{"=" * 10} PARTE 3 {"=" * 10}')
        attribs_numbers = ('1', '2', '3', '4', '5')

        # Dados tratados e exibidos
        print(which_one)
        for each_attrib in self.__hotel_data:
            print(str(each_attrib))

        self.__input_attrib_number = input(which_field)

        if self.__input_attrib_number in attribs_numbers:
            ObjectEdit.part_4(self)  # sucesso, prosseguir
        else:
            ObjectEdit.part_3(self)  # falha, repetir

    def part_4(self):
        print(f'{"=" * 10} PARTE 4 {"=" * 10}')
        print(attrib_chosen.format(ink(self.__hotel_data[int(self.__input_attrib_number) - 1])))
        index = 0
        attribs_numbers = ('1', '2', '3', '4', '5')
        attribs = ('hotel_id', 'name', 'stars', 'daily_charge', 'city')

        self.__input_new_attrib_value = input(new_value)

        while index < len(attribs_numbers):
            if self.__input_attrib_number == attribs_numbers[index]:
                Hotel.to_update(exec_=cursor,
                                hotel_id=self.__input_hotel_id,
                                _key=attribs[index],
                                _value=self.__input_new_attrib_value)
                input(roll)
                ObjectEdit.algorithm_launch(self)
            else:
                index += 1

        # if self.__input_attrib_number == attribs_numbers[0]:
        #     Hotel.to_update(exec_=cursor,
        #                     hotel_id=self.__input_hotel_id,
        #                     _key=attribs[0],
        #                     _value=self.__input_new_attrib_value)
        #     input(roll)
        #     ObjectEdit.algorithm_launch(self)
        #     menu_creator(paint=True, move_to_right=True, right_px=50, menu_content=menu_edit_object)
        # elif self.__input_attrib_number == attribs_numbers[1]:
        #     Hotel.to_update(exec_=cursor,
        #                     hotel_id=self.__input_hotel_id,
        #                     _key=attribs[1],
        #                     _value=self.__input_new_attrib_value)
        #     input(roll)
        #     ObjectEdit.algorithm_launch(self)
        #     menu_creator(paint=True, move_to_right=True, right_px=50, menu_content=menu_edit_object)
        # elif self.__input_attrib_number == attribs_numbers[2]:
        #     Hotel.to_update(exec_=cursor,
        #                     hotel_id=self.__input_hotel_id,
        #                     _key=attribs[2],
        #                     _value=self.__input_new_attrib_value)
        #     input(roll)
        #     ObjectEdit.algorithm_launch(self)
        #     menu_creator(paint=True, move_to_right=True, right_px=50, menu_content=menu_edit_object)
        # elif self.__input_attrib_number == attribs_numbers[3]:
        #     Hotel.to_update(exec_=cursor,
        #                     hotel_id=self.__input_hotel_id,
        #                     _key=attribs[3],
        #                     _value=self.__input_new_attrib_value)
        #     input(roll)
        #     ObjectEdit.algorithm_launch(self)
        #     menu_creator(paint=True, move_to_right=True, right_px=50, menu_content=menu_edit_object)
        # elif self.__input_attrib_number == attribs_numbers[4]:
        #     Hotel.to_update(exec_=cursor,
        #                     hotel_id=self.__input_hotel_id,
        #                     _key=attribs[4],
        #                     _value=self.__input_new_attrib_value)
        #     input(roll)
        #     ObjectEdit.algorithm_launch(self)
        #     menu_creator(paint=True, move_to_right=True, right_px=50, menu_content=menu_edit_object)

    def __init__(self, input_launch, input_hotel_id, input_attrib_number, input_new_attrib_value):
        self.__input_launch = input_launch
        self.__input_hotel_id = input_hotel_id
        self.__input_attrib_number = input_attrib_number
        self.__input_new_attrib_value = input_new_attrib_value
        self.__hotel_data = None


if __name__ == '__main__':
    hotel_object = ObjectEdit(input_launch=None,
                              input_hotel_id=None,
                              input_attrib_number=None,
                              input_new_attrib_value=None)

    hotel_object.algorithm_launch()
