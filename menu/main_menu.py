

from utils.functions import code_block_init, menu_creator
from utils.labels import (operation, closure, error, warn)

# TODO: Anteriormente, os imports foram feitos diretamente, mas um erro de importação circular estava acontecendo
# TODO: A solução encontrada foi importar somente via condição, quando a parte do algoritmo for de fato requisitada
# TODO: Porque isso está sendo feito?
# TODO: Temos dois algoritmos: menu/main_menu.py    menu/id_1 até id_5
# TODO: Os algoritmos "menu/id" encerram via função built in "exit(0)", pois está sendo evitado loop While e break
# TODO: Loop e break, nesse contexto, podem ser problemático aos algoritmos, então a solução mais eficaz é "exit(0)"
# TODO: O problema é que "exit(0)" encerra por completo, só podendo ativar novamente com uma nova execução
# TODO: Para evitar isso, nos algoritmos "menu/id", foram configurados uma nova opção via input "2"
# TODO: Esse input permite acesso ao algoritmo principal em "menu/main_menu.py", que usas os algoritmos "menu/id"
# TODO: Assim, o algoritmo principal somente encerra de fato conforme comando específico do usuário


class Menu:

    menu = (
        "======= MENU PRINCIPAL =======",
        "Encerrar sessão  || aperte 0",
        "Visualizar banco || aperte 1",
        "Procurar dado    || aperte 2",
        "Adicionar dado   || aperte 3",
        "Editar dado      || aperte 4",
        "Deletar dado     || aperte 5",
    )

    def database_full_management(self):

        menu_creator(paint=True, move_to_right=False, right_px=0, menu_content=Menu.menu)

        self.__main_input = input(operation)

        if self.__main_input == '0':
            print(closure)
            exit(0)

        elif self.__main_input == '1':
            from menu.id_1_query import DatabaseQuery
            DatabaseQuery.database_view()

        elif self.__main_input == '2':
            from menu.id_2_query_specific import DatabaseQuerySpecific
            request_query = DatabaseQuerySpecific()
            request_query.algorithm_main_window()

        elif self.__main_input == '3':
            from menu.id_3_object_insertion import ObjectAdd
            request_insertion = ObjectAdd()
            request_insertion.algorithm_main_window()

        elif self.__main_input == '4':
            from menu.id_4_object_reshape import ObjectEdit
            request_reshape = ObjectEdit()
            request_reshape.is_database_empty()

        elif self.__main_input == '5':
            from menu.id_5_object_removal import ObjectDelete
            request_removal = ObjectDelete()
            request_removal.is_database_empty()

        else:
            code_block_init(error, warn.format(1, 5))
            Menu.database_full_management(self)

    def __init__(self):
        self.__main_input = None


# Para poder ser chamado em outros módulos
manager_object = Menu()


if __name__ == '__main__':
    manager_object.database_full_management()
