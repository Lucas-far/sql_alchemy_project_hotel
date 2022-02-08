

"""
Adicionar objeto
"""

from part_1 import cursor
from utils.tools import *
from models.hotel import Hotel

hint = '\nDigite após a seta ---> '
operation = ink(f'\n======= Qual operação deseja realizar? ======= {ink(hint)}')
add_object = ink('\n======= SESSÃO: ADICIONAR OBJETO =======')
object_data = ink(f'======= Qual(is) os dados do objeto para criação? (ex: valor1,valor2,valor3...) ======= {ink(hint)}')
object_report = ink('======= CONTEXTO: OBJETO ADICIONADO AO BANCO? =======')
closure = ink('\nSessão encerrada. Volte sempre que precisar!\n')
roll = ink('\nPressione ENTER para continuar\n')
error = ink('\n========== MENSAGEM DE ERRO ==========')
warn = ink('As opções de menu vão de {} até {}.\n')

this_msg_error = ink('O limite de campos é 5: Nome id, nome do hotel, classificação, diária, cidade.')
this_msg_error2 = ink('Para adicionar dados, digite: valor1,valor2,valor3,valor4,valor5.')
this_msg_error3 = ink('EXEMPLO: franciso,Hotel Francisco,4.2,397.20,Cocais.')

content = (
    '========== MENU ==========',
    'Encerrar sessão  || aperte 0',
    'Adicionar dado   || aperte 1')


class ObjectAdd:

    @staticmethod
    def database_insert():
        allowed_numbers = ('0', '1')

        while True:
            menu_creator(paint=True, move_to_right=True, right_px=50, menu_content=content)
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
                        code_block_init(error, this_msg_error, this_msg_error2, this_msg_error3)
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
