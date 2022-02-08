

"""
Deletar objeto
"""

from part_1 import cursor
from utils.tools import *
from models.hotel import Hotel

hint = '\nDigite após a seta ---> '
operation = ink(f'\n======= Qual operação deseja realizar? ======= {ink(hint)}')
delete_object_label = ink('\n======= SESSÃO: DELETAR OBJETO =======')
hotel_id_name = ink(f'======= Qual o nome id do hotel a ser deletado? ======= {ink(hint)}')
object_to_be_deleted = ink(f'\n======= Objeto encontrado. Deseja deletar? =======')
ask_if_remove = ink(f'\n======= Confirmar a remoção? (0 = não deletar) (1 = deletar) ======= {ink(hint)}')
object_hotel_not_found = ink('O nome de id do hotel "{}" não foi encontrado.\n')

object_removal_canceled = ink('Remoção do objeto cancelada.\n')
object_deleted_label = ink('======= HOTEL DELETADO =======')

announcement = '\n======= INFORMAÇÃO ======='
closure = ink('\nSessão encerrada. Volte sempre que precisar!\n')
roll = ink('Pressione ENTER para continuar')
brick = ink('\n========== MENSAGEM DE ERRO ==========')
warn = ink('As opções de menu vão de {} até {}.\n')

content = (
    '========== MENU ==========',
    'Encerrar sessão  || aperte 0',
    'Deletar dado     || aperte 1'
)


class ObjectDelete:

    @staticmethod
    def to_delete_from_database():

        hotel_data = False
        input_hotel_id_outer = None
        input_remove_object = None
        allowed_numbers = ('0', '1')

        while True:
            menu_creator(paint=True, move_to_right=True, right_px=50, menu_content=content)
            this_input = input(operation)

            if this_input in allowed_numbers:
                if this_input == '0':
                    print(closure)
                    break
                elif this_input == '1':
                    while not hotel_data:
                        print(delete_object_label)
                        input_hotel_id = input(hotel_id_name)
                        input_hotel_id_outer = input_hotel_id
                        hotel_data = Hotel.database_query_by_hotel_id(exec_=cursor, hotel_id=input_hotel_id)
                        if not hotel_data:
                            code_block_init(brick, object_hotel_not_found.format(input_hotel_id_outer))
                    else:
                        code_block_init(object_to_be_deleted, hotel_data)
                        while input_remove_object not in allowed_numbers:
                            input_remove_object = input(ask_if_remove)
                            if input_remove_object == '0':
                                code_block_init(announcement, object_removal_canceled)
                                break
                            elif input_remove_object == '1':
                                # code_block_init(object_deleted_label, hotel_data)
                                Hotel.to_delete(exec_=cursor, hotel_id=input_hotel_id_outer)
                                input(roll)
                                break
                            else:
                                code_block_init(object_to_be_deleted, hotel_data)
                else:
                    code_block_init(brick, object_hotel_not_found.format(input_hotel_id_outer))
                    input(roll)
            else:
                code_block_init(brick, warn.format(0, 1))
                input(roll)


if __name__ == '__main__':
    database_size = len(Hotel.database_as_var(exec_=cursor))

    if database_size == 0:
        print('======= AVISO =======')
        print('Banco de dados vazio. Não é possível deletar algo.')
    else:
        ObjectDelete.to_delete_from_database()
