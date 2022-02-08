

"""
Atualizar objeto
"""

from part_1 import cursor
from utils.tools import *
from models.hotel import Hotel

hint = '\nDigite após a seta ---> '
operation = ink(f'\n======= Qual operação deseja realizar? ======= {ink(hint)}')
edit_object_label = ink('\n======= SESSÃO: ATUALIZAR OBJETO =======')
hotel_id_name = ink(f'======= Qual o nome id do hotel procurado? ======= {ink(hint)}')
which_field = ink(f'\n======= Escolha um dos valores acima e digite o que corresponde ao que deseja alterar =======')
new_value = ink(f'======= Qual o novo valor? ======= {ink(hint)}')
object_hotel_not_found = ink('O nome de id do hotel "{}" não foi encontrado.\n')

closure = ink('\nSessão encerrada. Volte sempre que precisar!\n')
roll = ink('\nPressione ENTER para continuar\n')
error = ink('\n========== MENSAGEM DE ERRO ==========')
warn = ink('As opções de menu vão de {} até {}.\n')

attempts_remaining = 'Tentativas restantes: {}'
attempts_exceeded = 'Número de tentativas máxima excedida: 3.'
attempts_show = 'Tentativas restantes: {}'
search_in_the_bank = 'Consulte o banco para saber o hotel de id a ser editado.\n'

content = (
    '========== MENU ==========',
    'Encerrar sessão  || aperte 0',
    'Atualizar dado   || aperte 1')


class ObjectEdit:

    @staticmethod
    def database_update():
        number_of_attempts = 0
        number_of_attempts_max = 3
        hotel_data = False
        allowed_numbers = ('0', '1')
        index = 0
        attribs_numbers = ('1', '2', '3', '4', '5')
        attribs = ('hotel_id', 'name', 'stars', 'daily_charge', 'city')

        while True:
            menu_creator(paint=True, move_to_right=True, right_px=50, menu_content=content)
            this_input = input(operation)

            if this_input in allowed_numbers:
                if this_input == '0':
                    print(closure)
                    break
                elif this_input == '1':
                    # Um loop é criado para conseguir editar um dado de um objeto, através do nome de id
                    while not hotel_data:
                        print(edit_object_label)
                        input_hotel_id = input(hotel_id_name)
                        hotel_data = Hotel.database_query_by_hotel_id(exec_=cursor, hotel_id=input_hotel_id)
                        # Se não souber o nome de id: abrir um número de tentativas e lançar erro de aviso
                        if not hotel_data:
                            number_of_attempts += 1
                            code_block_init(error, object_hotel_not_found.format(input_hotel_id))
                            print(attempts_remaining.format(number_of_attempts_max - number_of_attempts))
                        if hotel_data:
                            number_of_attempts = 0
                            hotel_data = list(hotel_data.values())
                            hotel_data = [{index: data} for index, data in enumerate(hotel_data)]
                            del hotel_data[0]

                            print(which_field)
                            for each_attrib in hotel_data:
                                print(str(each_attrib).center(100))

                            input_value_chosen = input(hint)
                            while input_value_chosen not in attribs_numbers:
                                code_block_init(error, warn.format(1, 5))

                                print(which_field)
                                for each_attrib in hotel_data:
                                    print(str(each_attrib).center(100))

                                input_value_chosen = input(hint)
                            else:
                                input_object_new_data_value = input(new_value)

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
