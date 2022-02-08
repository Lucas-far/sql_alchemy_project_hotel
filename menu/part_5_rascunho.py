

"""
Deletar objeto

Escopo 1 = "else" impede se valor != 0/1
Escopo 2 = "else" dispensado
Escopo 3 = "else" caso retorno False
"""

from part_1 import cursor
from utils.tools import *
from models.hotel import Hotel

hint = '\nDigite após a seta ---> '
operation = ink(f'\n======= Qual operação deseja realizar? ======= {ink(hint)}')
delete_object = ink('\n======= SESSÃO: DELETAR OBJETO =======')
hotel_id_name = ink(f'======= Qual o nome id do hotel procurado? ======= {ink(hint)}')
object_to_be_deleted = ink(f'\n======= O seguinte objeto está prestes a ser removido do banco de dados =======')
ask_if_remove = ink(f'\n======= Confirmar a remoção? (0 = não deletar) (1 = deletar) ======= {ink(hint)}')
object_hotel_not_found = ink('O nome de id do hotel "{}" não foi encontrado.\n')
closure = ink('\nSessão encerrada. Volte sempre que precisar!\n')
roll = ink('Pressione ENTER para continuar')
brick = ink('\n========== MENSAGEM DE ERRO ==========')
warn = ink('As opções de menu vão de {} até {}.\n')

content = (
    '========== MENU PRINCIPAL ==========',
    'Encerrar sessão  || aperte 0',
    'Deletar dado     || aperte 1'
)


class ObjectDelete:

    @staticmethod
    def to_delete():
        allowed_numbers = ('0', '1')
        options = [str(number) for number in range(0, 2)]

        while True:
            menu_creator(paint=True, move_to_right=True, right_px=50, menu_content=content)
            this_input = input(operation)

            if this_input in allowed_numbers:  # 1
                if this_input == '0':  # 2
                    print(closure)
                    break
                elif this_input == '1':  # 2
                    # São 2 inputs
                    # Input 1 = usado para coletar os dados do objeto a ser deletado
                    # Input 2 = informar se o objeto exibido deve ser deletado
                    print(delete_object)
                    input_hotel_id = input(hotel_id_name)  # Input 1

                    # Tratamento do input 1 para exibir dados do objeto a ser editado futuramente
                    hotel_data = Hotel.database_query_by_hotel_id(exec_=cursor, hotel_id=input_hotel_id)

                    if hotel_data:  # 3
                        hotel_data = list(hotel_data.values())
                        hotel_data = [{index: data} for index, data in enumerate(hotel_data)]
                        del hotel_data[0]

                        print(object_to_be_deleted)
                        for each_content in hotel_data:
                            print(str(each_content).center(100))

                        # allowed_numbers = [str(number) for number in range(0, 2)]
                        input_remove_object = input(ask_if_remove)  # input 2

                        if input_remove_object in allowed_numbers:  # 4

                            if input_remove_object == '0':
                                code_block_init(brick, warn.format(0, 1))
                                input(roll)

                            elif input_remove_object == '1':
                                Hotel.to_delete(exec_=cursor, hotel_id=input_hotel_id)
                                input(roll)
                        else:  # 4
                            code_block_init(brick, warn.format(0, 1))
                            input(roll)

                            # TODO: Solução do problema
                            while input_remove_object not in allowed_numbers:
                                code_block_init(brick, warn.format(0, 1))
                                print(object_to_be_deleted)
                                for each_content in hotel_data:
                                    print(str(each_content).center(100))
                                input_remove_object = input(ask_if_remove)

                    else:  # 3
                        code_block_init(brick, object_hotel_not_found.format(input_hotel_id))
                        input(roll)
            else:  # 1
                code_block_init(brick, warn.format(0, 1))
                input(roll)


if __name__ == '__main__':
    ObjectDelete.to_delete()
