

"""
Atualizar objeto
"""

from models.hotel import Hotel
from id_1_query import cursor
from utils.functions import *
from utils.labels import *


class ObjectEdit:
    """
    1.0 - Var com os dados do banco (uso da função do modelo). Se essa var estiver vazia, o algitmo encerra
    1.1 - Havendo algum objeto, este pode ser editado, portanto o algoritmo pode ser iniciado
    1.2 - Exibição das opções disponíveis
    1.3 - Lançamento da entrada 1 p/ pedir uma escolha
    1.4 - Optar por encerrar o algoritmo
    1.5 - Prosseguir com a edição de um dos atributos do objeto do banco
    1.6 - Informar entrada inválida em relação as opções de entrada disponíveis
    1.7 - Lançamento da entrada 2 p/ requisitar o atributo "hotel_id" de um objeto (forma de busca deste algoritmo)
    1.8 - Uso de uma função do modelo, que recebe a entrada como argumento, para busca do atributo no banco
    1.9 - Se dentro os objetos do banco, o seu atributo "hotel_id" == entrada 2. Iniciar o procedimento de edição
    2.0 - Manipular dados do objeto, deletando a PK, para que o usuário possa escolher dados permitidos do objeto
    2.1 - Impedir o usuário de prosseguir em caso de erros de pesquisa contínuos
    2.2 - Lançar contagem de erros caso o banco não consiga encontrar o que o usuário está pesquisando como "hotel_id"
    2.3 - Menu exibindo os dados do objeto a ser editado, oferecendo escolhas de mudança individuais
    2.4 - Lançamento da entrada 3, afim de saber qual o número do atributo a ser editado
    2.5 - Prosseguir com a parte final: edição do atributo escolhido (reatribuição de valor)
    2.6 - Tratamento das opções do menu, impedindo o usuário de avançar caso não forneça uma das opções disponíveis
    2.7 - Exibir a escolha do usuário, mostrando o atributo escolhido, afim de dar ao usuário um lembrete
    2.8 - Lnaçamento da entrada 4, p/ requisitar o novo valor do atributo escolhido
    2.9 - Vars auxiliares para o funcionamento do loop da função que atualiza o valor do atributo do objeto
    2.9 - As tuplas possuem a ordem exata do menu mostrado ao usuário anteriormente, afim de impedir erros no loop
    """

    allowed_attrib_values = ('1', '2', '3', '4', '5')

    # PARTE 1
    def is_database_empty(self):
        database_size = len(Hotel.database_as_var(exec_=cursor))  # 1.0

        if database_size == 0:
            code_block_init(error, empty_database)
            exit(0)

        else:  # 1.1
            ObjectEdit.algorithm_main_window(self)

    @staticmethod
    def shut_it_down():
        print(closure)
        exit(0)

    def misleading_input(self):
        code_block_init(error, warn.format(0, 1))
        ObjectEdit.algorithm_main_window(self)

    def build_menu_through_object_data(self):
        self.__number_attempts = 0
        self.__hotel_data = list(self.__hotel_data.values())
        self.__hotel_data = [{index: data} for index, data in enumerate(self.__hotel_data)]
        del self.__hotel_data[0]
        ObjectEdit.object_attrib_choice(self)

    def max_mistakes_reached(self):
        self.__number_attempts = 0
        code_block_init(error, attempts_exceeded, search_in_the_database)
        exit(0)

    def throw_new_search_attempt(self):
        self.__number_attempts += 1
        code_block_init(error,
                        object_hotel_not_found.format(self.__input_hotel_id),
                        attempts_remaining.format(self.__number_attempts_max - self.__number_attempts))
        # repetir esta função
        ObjectEdit.object_hotel_id_seek(self)

    def display_object_data_menu(self):
        print(which_one)
        for each_object_attrib in self.__hotel_data:
            print(str(each_object_attrib))

    def display_user_choice(self):
        print(attrib_chosen.format(ink(self.__hotel_data[int(self.__input_attrib_number) - 1])))

    def attrib_manager(self):
        # 2.9
        index = 0
        attribs = ('hotel_id', 'name', 'stars', 'daily_charge', 'city')

        while index < len(ObjectEdit.allowed_attrib_values):
            if self.__input_attrib_number == ObjectEdit.allowed_attrib_values[index]:
                Hotel.to_update(exec_=cursor,
                                hotel_id=self.__input_hotel_id,
                                _key=attribs[index],
                                _value=self.__input_new_attrib_value)
                input(roll)
                ObjectEdit.algorithm_main_window(self)  # reiniciar
            else:
                index += 1

    # PARTE 2
    def algorithm_main_window(self):
        menu_creator(paint=True, move_to_right=False, right_px=0, menu_content=menu_edit_object)  # 1.2

        self.__input_launch = input(operation)  # 1.3

        if self.__input_launch == '0':  # 1.4
            ObjectEdit.shut_it_down()

        if self.__input_launch == '1':  # 1.5
            ObjectEdit.object_hotel_id_seek(self)

        else:  # 1.6
            ObjectEdit.misleading_input(self)

    # PARTE 3
    def object_hotel_id_seek(self):

        self.__input_hotel_id = input(hotel_id_name_to_edit)  # 1.7
        self.__hotel_data = Hotel.database_query_by_hotel_id(exec_=cursor, hotel_id=self.__input_hotel_id)  # 1.8

        if self.__hotel_data:  # 1.9
            ObjectEdit.build_menu_through_object_data(self)  # 2.0

        if self.__number_attempts >= 3:  # 2.1
            ObjectEdit.max_mistakes_reached(self)

        if not self.__hotel_data:  # 2.2
            ObjectEdit.throw_new_search_attempt(self)

    # PARTE 4
    def object_attrib_choice(self):
        ObjectEdit.display_object_data_menu(self)  # 2.3

        self.__input_attrib_number = input(which_field)  # 2.4

        if self.__input_attrib_number in ObjectEdit.allowed_attrib_values:  # 2.5
            ObjectEdit.object_attrib_renewal(self)

        else:  # 2.6
            ObjectEdit.object_attrib_choice(self)

    # PARTE 5
    def object_attrib_renewal(self):

        ObjectEdit.display_user_choice(self)  # 2.7

        self.__input_new_attrib_value = input(new_value)  # 2.8

        ObjectEdit.attrib_manager(self)  # 2.9

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
