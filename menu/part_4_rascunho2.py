

"""
Atualizar objeto
"""

from part_1 import cursor
from utils.functions import *
from utils.labels import *
from models.hotel import Hotel


class ObjectEdit:

    input_1st, input_2nd, input_3rd, input_4th, hotel_data_backup = [], [], [], [], None

    @staticmethod
    def part_1():

        menu_creator(paint=True, move_to_right=True, right_px=50, menu_content=menu_edit_object)
        this_input_start = input(f'Qual operação deseja realizar? {ink(hint)}')

        if this_input_start == '0':
            print(ink('\nSessão encerrada. Volte sempre que precisar!\n'))
            exit(0)
        if this_input_start == '1':
            ObjectEdit.input_1st.append(this_input_start)  # guardar o input 1 (sucesso)
            ObjectEdit.part_2()  # prosseguir
        else:
            code_block_init(error, warn.format(0, 1))  # erro
            ObjectEdit.part_1()  # repete a função

    @staticmethod
    def part_2():

        input_hotel_id = input(ink(f'\nQual o nome id do hotel procurado para ser alterado? {ink(hint)}'))
        hotel_data = Hotel.database_query_by_hotel_id(exec_=cursor, hotel_id=input_hotel_id)

        if hotel_data:
            ObjectEdit.hotel_data_backup = hotel_data  # para uso na função seguinte
            ObjectEdit.hotel_data_backup = list(ObjectEdit.hotel_data_backup.values())
            ObjectEdit.hotel_data_backup = [{index: data} for index, data in enumerate(ObjectEdit.hotel_data_backup)]
            del ObjectEdit.hotel_data_backup[0]

            ObjectEdit.input_2nd.append(input_hotel_id)  # guardar o input 2 (sucesso)
            ObjectEdit.part_3()  # prosseguir

        # Se não souber o nome de id: abrir um número de tentativas e lançar erro de aviso
        if not hotel_data:
            code_block_init(error, object_hotel_not_found.format(input_hotel_id))  # erro
            ObjectEdit.part_2()  # repete a função

    @staticmethod
    def part_3():
        attribs_numbers = ('1', '2', '3', '4', '5')

        # Dados tratados e exibidos
        print('\nEscolha um dos valores dos atributos abaixo')
        for each_attrib in ObjectEdit.hotel_data_backup:
            print(str(each_attrib))

        input_value_chosen = input(f'Digite o valor do atributo a ser modificado {ink(hint)}')

        if input_value_chosen in attribs_numbers:
            print(f'\nAtributo escolhido: {ink(ObjectEdit.hotel_data_backup[int(input_value_chosen) - 1])}')

            ObjectEdit.input_3rd.append(input_value_chosen)
            ObjectEdit.part_4()  # sucesso
        else:
            ObjectEdit.part_3()  # falha
            # recycled_hotel_data = ObjectEdit.hotel_data_backup
            # recycled_hotel_data = list(recycled_hotel_data.values())
            # recycled_hotel_data = [{index: data} for index, data in enumerate(recycled_hotel_data)]
            # del recycled_hotel_data[0]
            #
            # print(which_field)
            # for each_attrib in recycled_hotel_data:
            #     print(str(each_attrib).center(100))
            #
            # ObjectEdit.part_3()

    @staticmethod
    def part_4():
        attribs_numbers = ('1', '2', '3', '4', '5')
        attribs = ('hotel_id', 'name', 'stars', 'daily_charge', 'city')

        obj_new_value = input(ink(f'Qual o novo valor? {ink(hint)}'))

        if ObjectEdit.input_3rd[0] == attribs_numbers[0]:
            Hotel.to_update(exec_=cursor, hotel_id=ObjectEdit.input_2nd[0], _key=attribs[0], _value=obj_new_value)
            exit(0)
        elif ObjectEdit.input_3rd[0] == attribs_numbers[1]:
            Hotel.to_update(exec_=cursor, hotel_id=ObjectEdit.input_2nd[0], _key=attribs[1], _value=obj_new_value)
            exit(0)
        elif ObjectEdit.input_3rd[0] == attribs_numbers[2]:
            Hotel.to_update(exec_=cursor, hotel_id=ObjectEdit.input_2nd[0], _key=attribs[2], _value=obj_new_value)
            exit(0)
        elif ObjectEdit.input_3rd[0] == attribs_numbers[3]:
            Hotel.to_update(exec_=cursor, hotel_id=ObjectEdit.input_2nd[0], _key=attribs[3], _value=obj_new_value)
            exit(0)
        elif ObjectEdit.input_3rd[0] == attribs_numbers[4]:
            Hotel.to_update(exec_=cursor, hotel_id=ObjectEdit.input_2nd[0], _key=attribs[4], _value=obj_new_value)
            exit(0)

    # @staticmethod
    # def part_5():
    #     ObjectEdit.input_1st = []
    #     ObjectEdit.input_2nd = []
    #     ObjectEdit.input_3rd = []
    #     ObjectEdit.input_4th = []
    #     ObjectEdit.hotel_data_backup = []
    #
    # @staticmethod
    # def show_inputs(*args):
    #     print('======= DADOS =======')
    #     for data in args:
    #         print(data)
    #
    # @staticmethod
    # def algorithm():
    #     box = []
    #     attribs_numbers = ('1', '2', '3', '4', '5')
    #     attribs = ('hotel_id', 'name', 'stars', 'daily_charge', 'city')
    #
    #     tutorial = """
    #     ======= BEM-VINDO À SESSÃO DE EDITAR OBJETO =======
    #     É necessário o fornecimento de 3 dados, que serão requisitados em sequência.
    #     1 - O nome de id do hotel para obter seus dados
    #     2 - O número do atributo do objeto encontrado
    #     3 - O novo valor do atributo
    #     """
    #
    #     print(tutorial)
    #     input_hotel_id = input(hotel_id_name_to_edit)
    #     box.append(input_hotel_id)
    #     hotel_data = Hotel.database_query_by_hotel_id(exec_=cursor, hotel_id=input_hotel_id)
    #
    #     if hotel_data:
    #
    #         hotel_data = list(hotel_data.values())
    #         hotel_data = [{index: data} for index, data in enumerate(hotel_data)]
    #         del hotel_data[0]
    #
    #         print(which_field)
    #         for each_attrib in hotel_data:
    #             print(str(each_attrib).center(100))
    #
    #         input_value_chosen = input(hint)
    #         box.append(input_value_chosen)
    #
    #         if input_value_chosen in attribs_numbers:
    #             input_object_new_value = input(new_value)
    #             box.append(input_object_new_value)
    #
    #             if input_object_new_value in attribs_numbers:
    #
    #                 if input_object_new_value == attribs_numbers[0]:
    #                     Hotel.to_update(exec_=cursor, hotel_id=ObjectEdit.input_2nd[0], _key=attribs[0],
    #                                     _value=input_object_new_value)
    #                 elif input_object_new_value == attribs_numbers[1]:
    #                     Hotel.to_update(exec_=cursor, hotel_id=ObjectEdit.input_2nd[0], _key=attribs[1],
    #                                     _value=input_object_new_value)
    #                 elif input_object_new_value == attribs_numbers[2]:
    #                     Hotel.to_update(exec_=cursor, hotel_id=ObjectEdit.input_2nd[0], _key=attribs[2],
    #                                     _value=input_object_new_value)
    #                 elif input_object_new_value == attribs_numbers[3]:
    #                     Hotel.to_update(exec_=cursor, hotel_id=ObjectEdit.input_2nd[0], _key=attribs[3],
    #                                     _value=input_object_new_value)
    #                 elif input_object_new_value == attribs_numbers[4]:
    #                     Hotel.to_update(exec_=cursor, hotel_id=ObjectEdit.input_2nd[0], _key=attribs[4],
    #                                     _value=input_object_new_value)
    #                 # else:
    #                 #     print('Dados incorretos, reinicie o procedimento.')
    #         else:
    #             code_block_init(error, 'Opção de atributo inválida. Escolha entre {} a {}'.format(1, 5))
    #             # ObjectEdit.algorithm()
    #     if not hotel_data:
    #         code_block_init(error, 'Hotel não encontrado')
    #         # exit(0)
    #         # ObjectEdit.algorithm()
    #
    #     ObjectEdit.algorithm()
    #
    # @staticmethod
    # def reset_inputs():
    #     ObjectEdit.input_hotel_id = None
    #     ObjectEdit.input_value_chosen = None
    #     ObjectEdit.obj_new_value = None


if __name__ == '__main__':
    ObjectEdit.part_1()
    ObjectEdit.part_2()
    ObjectEdit.part_3()
    ObjectEdit.part_4()
    #     ObjectEdit.part_5()
    #     ObjectEdit.show_inputs(ObjectEdit.input_1st, ObjectEdit.input_2nd, ObjectEdit.input_3rd, ObjectEdit.input_4th)
    # else:
    #     print('Algoritmo finalizado.')
    # ObjectEdit.algorithm()
