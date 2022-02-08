

from menu.part_1 import DatabaseQuery
from menu.part_2 import DatabaseQuerySpecific
from menu.part_3 import ObjectAdd
from menu.part_4 import ObjectEdit
from menu.part_5 import ObjectDelete
from utils.functions import code_block_init, ink

if __name__ == '__main__':
    acceptable_values = ('0', '1', '2', '3', '4', '5')
    main_input = None
    options = (
        "======= MENU PRINCIPAL =======",
        "Encerrar sessão  || aperte 0",
        "Visualizar banco || aperte 1",
        "Procurar dado    || aperte 2",
        "Adicionar dado   || aperte 3",
        "Editar dado      || aperte 4",
        "Deletar dado     || aperte 5",
    )

    hint = '\nDigite após a seta ---> '
    operation = ink(f'\n======= Qual operação deseja realizar? ======= {ink(hint)}')
    closure = ink('\nSessão encerrada. Volte sempre que precisar!\n')
    error = ink('\n========== MENSAGEM DE ERRO ==========')
    warn = ink('Menu aceita números de {} a {}\n')

    while main_input not in acceptable_values:
        for data in options:
            print(ink(data))
        main_input = input(operation)
        if main_input not in acceptable_values:
            code_block_init(error, warn.format(0, 5))
        else:
            if main_input == '0':
                print(closure)
                break
            # main_input = reatribuido para "None" para evitar que o programa encerre após as consultas
            elif main_input == '1':
                DatabaseQuery.database_view()
                main_input = None
            elif main_input == '2':
                DatabaseQuerySpecific.query_database_data()
                main_input = None
            elif main_input == '3':
                ObjectAdd.database_insert()
                main_input = None
            elif main_input == '4':
                ObjectEdit.database_update()
                main_input = None
            elif main_input == '5':
                ObjectDelete.to_delete_from_database()
                main_input = None
