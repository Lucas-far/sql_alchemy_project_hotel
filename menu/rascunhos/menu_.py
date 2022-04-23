

from utils.tools import *


class App:

    @staticmethod
    def launcher():
        options = [str(number) for number in range(0, 6)]

        while True:
            display_this(keyword='menu', paint=True, to_right=True, right_px=50)
            this_input = input(msg['operation'])

            if this_input in options:

                # TODO: Encerrar sessão
                if this_input == '0':
                    print(ink(msg['exit']))
                    break

                # TODO: Vizualizar banco
                elif this_input == '1':
                    Hotel.database_query(exec_=cursor)
                    print(input(ink(msg['roll'])))

                # TODO: Pesquisar dado
                elif this_input == '2':

                    while True:
                        display_this(keyword='pesquisa', paint=True, to_right=True, right_px=50)
                        this_input = input(ink(msg['which_attribute_to_search']))

                        if this_input in options:

                            # Cancelar
                            if this_input == '0':
                                break

                            # Id do hotel
                            elif this_input == '1':
                                print(msg['object_search'])
                                target = input(msg['object_name_id'])
                                hotel_object_hotel_id = Hotel.database_query_by_hotel_id(exec_=cursor, hotel_id=target)
                                print(ink(msg['object_found_or_not']))
                                print(hotel_object_hotel_id)
                                break

                            # elif this_input == '2':
                            #     print(msg['object_search'])
                            #     target = input(msg['object_name'])
                            #     hotel_object_name = Hotel.to_query_by_name(exec_=cursor, name=target)
                            #     print(ink(msg['object_found_or_not']))
                            #     print(hotel_object_name)
                            #     break
                            #
                            # elif this_input == '3':
                            #     print(msg['object_search'])
                            #     target = input(msg['object_daily_charge'])
                            #     hotel_object_daily_charge = Hotel.to_query_by_daily_charge(exec_=cursor,
                            #                                                                daily_charge=target)
                            #     print(ink(msg['object_found_or_not']))
                            #     print(hotel_object_daily_charge)
                            #     break
                            #
                            # elif this_input == '4':
                            #     print(msg['object_search'])
                            #     target = input(msg['object_city'])
                            #     hotel_object_city = Hotel.to_query_by_city(exec_=cursor, city=target)
                            #     print(ink(msg['object_found_or_not']))
                            #     print(hotel_object_city)
                            #     break

                # TODO: Adicionar dado
                elif this_input == '3':
                    this_msg_error = 'O limite de campos é 5: Nome id, nome do hotel, classificação, diária, cidade.'

                    print(ink(msg['object_add']))
                    # ---------------------- Digitar neste input cada valor separado por vírgula ----------------------
                    input_values = input(ink(msg['object_data']))
                    box = input_values.split(',')

                    if len(box) == 5:
                        new_hotel = Hotel(hotel_id=box[0], name=box[1], stars=box[2], daily_charge=box[3], city=box[4])
                        print(ink(msg['object_added_or_not']))
                        # --------------- A adição do objeto ao banco depende das condições nessa função ---------------
                        Hotel.database_insert(exec_=cursor, hotel_object=new_hotel)
                    else:
                        print(this_msg_error)

                # TODO: Atualizar dado
                elif this_input == '4':

                    while True:
                        # display_this(keyword='atualização', paint=True, to_right=True, right_px=50)

                        # São 3 inputs
                        # Input 1 = usado para coletar os dados do objeto a ser alterado
                        # Input 2 = informar o dado numérico do valor que será alterado (dados serão exibidos)
                        # Input 3 = novo valor para o dado

                        input_hotel_id = input(msg['object_name_id'])  # Input 1

                        hotel_data = Hotel.database_query_by_hotel_id(exec_=cursor, hotel_id=input_hotel_id)
                        hotel_data = list(hotel_data.values())
                        hotel_data = [f"{index} - {data}" for index, data in enumerate(hotel_data)]
                        print(hotel_data)
                        # print([3], hotel_data.values())
                        # hotel_current_data = tuple(
                        #     f"{index} - {data}" for index, data in enumerate(hotel_data.values())
                        # )
                        # print(hotel_current_data)

                        allowed_values = [str(number) for number in range(0, 6)]
                        input_value_chosen = input(msg['object_which_attribute'])  # Input 2

                        if input_value_chosen in allowed_values:
                            if input_value_chosen == '0':
                                print('Acesso negado: chave primária não pode ser alterada')
                                # break
                            else:
                                object_new_data_value = input('Qual o novo valor?')  # Input 3

                                index = 0
                                choices = ('0', '1', '2', '3', '4', '5')
                                attribs = ('id', 'hotel_id', 'name', 'stars', 'daily_charge', 'city')

                                while index < 5:
                                    if input_value_chosen == choices[index]:
                                        Hotel.to_update(exec_=cursor,
                                                        hotel_id=input_hotel_id,
                                                        _key=attribs[index],
                                                        _value=object_new_data_value)
                                        break
                                    else:
                                        index += 1
                                index = 0

                        else:
                            print('Valores aceitos: 0 até 4')

                        break
                        # this_input = input(ink(msg['which_attribute_to_update']))
                        #
                        # if this_input in options:
                        #
                        #     # Cancelar
                        #     if this_input == '0':
                        #         break
                        #
                        #     # Id do hotel
                        #     elif this_input == '1':



                                # hotel_new_data = input(msg['object_type_new_values'])
                                # hotel_new_data = hotel_new_data.split(',')

                                # old, new = input_thrower(label_1st=ink(msg['object_value_now']),
                                #                          label_2nd=ink(msg['object_value_new']))
                                # print(ink(msg['object_updated']))
                                # Hotel.to_update_by_hotel_id(exec_=cursor, current=old, new=new)
                                # break

                            # elif this_input == '2':
                            #     old, new = input_thrower(label_1st=ink(msg['object_value_now']),
                            #                              label_2nd=ink(msg['object_value_new']))
                            #     print(ink(msg['object_updated']))
                            #     Hotel.to_update_by_name(exec_=cursor, current=old, new=new)
                            #     break

                            # elif this_input == '3':
                            #
                            #     old, new = input_thrower(label_1st=ink(msg['object_value_now']),
                            #                              label_2nd=ink(msg['object_value_new']))
                            #     print(ink(msg['object_updated']))
                            #     Hotel.to_update_by_stars(exec_=cursor, current=old, new=new)
                            #     break

                            # elif this_input == '4':
                            #     old, new = input_thrower(label_1st=ink(msg['object_value_now']),
                            #                              label_2nd=ink(msg['object_value_new']))
                            #     print(ink(msg['object_updated']))
                            #     Hotel.to_update_by_daily_charge(exec_=cursor, current=old, new=new)
                            #     break

                # elif this_input == '5':
                #     old, new = input_thrower(label_1st=ink(msg['object_value_now']),
                #                              label_2nd=ink(msg['object_value_new']))
                #     print(ink(msg['object_updated']))
                #     Hotel.to_update_by_city(exec_=cursor, current=old, new=new)
                #     break
                #
                #         else:
                #             print(ink(msg['error']))
                #             print(ink(msg['error_number']))

                elif this_input == '5':

                    while True:
                        display_this(keyword='remoção', paint=True, to_right=True, right_px=50)
                        this_input = input(ink(msg['which_attribute_to_delete']))

                        if this_input in options:

                            if this_input == '0':
                                break

                            elif this_input == '1':
                                target = input(msg['object_value'])
                                print(ink(msg['object_deleted']))
                                Hotel.to_delete_by_hotel_id(exec_=cursor, value=target)
                                break

                            elif this_input == '2':
                                target = input(msg['object_value'])
                                print(ink(msg['object_deleted']))
                                Hotel.to_delete_by_name(exec_=cursor, value=target)
                                break

                            elif this_input == '3':
                                target = input(msg['object_value'])
                                print(ink(msg['object_deleted']))
                                Hotel.to_delete_by_stars(exec_=cursor, value=target)
                                break

                            elif this_input == '4':
                                target = input(msg['object_value'])
                                print(ink(msg['object_deleted']))
                                Hotel.to_delete_by_daily_charge(exec_=cursor, value=target)
                                break

                            elif this_input == '5':
                                target = input(msg['object_value'])
                                print(ink(msg['object_deleted']))
                                Hotel.to_delete_by_city(exec_=cursor, value=target)
                                break

                        else:
                            print(ink(msg['error']))
                            print(ink(msg['error_number']))

                else:
                    print(ink(msg['error']))
                    print(ink(msg['error_number']))

            else:
                print(ink(msg['error']))
                print(ink(msg['error_number']))


if __name__ == '__main__':
    from models.hotel import Hotel
    engine = Hotel.database_config(name='db_var')
    cursor = Hotel.database_cursor(engine=engine)
    Hotel.database_init(engine=engine)
    App.launcher()
