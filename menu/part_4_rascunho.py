

"""
Atualizar objeto
"""

from part_1 import cursor
from utils.functions import *
from utils.labels import *
from models.hotel import Hotel


class ObjectEdit:

    @staticmethod
    def database_update():
        number_of_attempts = 0
        number_of_attempts_max = 3
        hotel_data = False
        index = 0
        attribs_numbers = ('1', '2', '3', '4', '5')
        attribs = ('hotel_id', 'name', 'stars', 'daily_charge', 'city')

        while True:
            menu_creator(paint=True, move_to_right=True, right_px=50, menu_content=menu_edit_object)
            this_input = input(operation)

            if this_input in allowed_numbers:

                if this_input == '0':
                    print(closure)
                    break
                elif this_input == '1':

                    # Um loop é criado para conseguir editar um dado de um objeto, através do nome de id
                    while not hotel_data:
                        print(edit_object_label)
                        input_hotel_id = input(hotel_id_name_to_edit)
                        hotel_data = Hotel.database_query_by_hotel_id(exec_=cursor, hotel_id=input_hotel_id)

                        # Se não souber o nome de id: abrir um número de tentativas e lançar erro de aviso
                        if not hotel_data:
                            number_of_attempts += 1
                            code_block_init(error, object_hotel_not_found.format(input_hotel_id))
                            print(attempts_remaining.format(number_of_attempts_max - number_of_attempts))

                        # Se o objeto foi achado, tratar os dados e mostrar ao usuário para que ele escolha
                        if hotel_data:
                            number_of_attempts = 0
                            hotel_data = list(hotel_data.values())
                            hotel_data = [{index: data} for index, data in enumerate(hotel_data)]
                            del hotel_data[0]

                            # Dados tratados e exibidos
                            print(which_field)
                            for each_attrib in hotel_data:
                                print(str(each_attrib).center(100))

                            # Pedir ao usuário o valor correspondente do dado que deseja editar
                            input_value_chosen = input(hint)

                            # Tratar o input acima, p/ impedir que opções inválidas sejam digitadas, repetindo o input
                            while input_value_chosen not in attribs_numbers:
                                code_block_init(error, warn.format(1, 5))

                                print(which_field)
                                for each_attrib in hotel_data:
                                    print(str(each_attrib).center(100))

                                input_value_chosen = input(hint)

                            # Se o valor digitado no input acima for correto, pedir um novo valor para editar o objeto
                            else:
                                # Usuário fornece o valor aqui
                                input_object_new_data_value = input(new_value)

                                # Esse loop usa os dados passados nessa seção para editar o objeto corretamente
                                # Para dar certo, as vars com "index" têm mesmo tamanho (5) e estão em ordem apropriada
                                # O valor "4" é: 0, 1, 2, 3, 4 = tamanho 5
                                while index < 4:
                                    if input_value_chosen == attribs_numbers[index]:
                                        Hotel.to_update(exec_=cursor,
                                                        hotel_id=input_hotel_id,
                                                        _key=attribs[index],
                                                        _value=input_object_new_data_value)
                                        break
                                    else:
                                        index += 1
                                index = 0

                        # Tratamento para impedir o usuário de ficar tentando erros contínuos
                        if number_of_attempts >= 3:
                            code_block_init(error,
                                            attempts_exceeded,
                                            attempts_show.format(number_of_attempts_max - number_of_attempts),
                                            search_in_the_bank)
                            break
            else:
                code_block_init(error, warn.format(0, 1))
                input(roll)


if __name__ == '__main__':
    ObjectEdit.database_update()
