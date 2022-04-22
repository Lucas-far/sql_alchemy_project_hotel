

from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Float, Integer, String
from utils.functions import code_block_init

# Var para criação do banco, com chamada direta na classe abaixo, na função "database_init()"
Base = declarative_base()


class Hotel(Base):

    @staticmethod
    def database_config(name):
        import sqlalchemy
        engine = sqlalchemy.create_engine(f"sqlite:///{name}")
        return engine

    @staticmethod
    def database_cursor(engine):
        from sqlalchemy.orm import sessionmaker
        Session = sessionmaker(bind=engine)
        cursor = Session()
        return cursor

    @staticmethod
    def database_init(engine):
        Base.metadata.create_all(engine)

    @staticmethod
    def json(object_):
        return {
            "id_": object_.id_,
            "hotel_id": object_.hotel_id,
            "name": object_.name,
            "stars": float(object_.stars),
            "daily_charge": float(object_.daily_charge),
            "city": object_.city
        }

    @staticmethod
    def database_as_var(exec_):
        box = []

        for content in exec_.query(Hotel).order_by(Hotel.id_):
            box.append(Hotel.json(object_=content))
        return box

    @staticmethod
    def database_query(exec_):
        available_data = "\n======= CONTEXTO: DADOS ATUAIS DO BANCO ======="
        empty_database = 'Banco de dados encontra-se vazio.\n'

        hotels_database = Hotel.database_as_var(exec_)

        if len(hotels_database) != 0:
            print(available_data)
            for hotel in hotels_database:
                print(hotel)
        else:
            code_block_init(available_data, empty_database)

    # Função GET - verificação
    @staticmethod
    def database_query_by_hotel_id(exec_, hotel_id):
        query_hotel = exec_.query(Hotel).filter_by(hotel_id=hotel_id).first()

        if query_hotel:
            query_hotel_as_dict = Hotel.json(object_=query_hotel)
            return query_hotel_as_dict
        return None

    @staticmethod
    def to_query_by_name(exec_, name):

        this_msg_error = 'O nome do hotel especificado não consta no banco.'

        try:
            query_hotel = exec_.query(Hotel).filter_by(name=name).first()
            query_hotel_as_dict = Hotel.json(object_=query_hotel)
            return query_hotel_as_dict
        except AttributeError:
            return this_msg_error

    # @staticmethod
    # def to_query_by_daily_charge(exec_, daily_charge):
    #
    #     this_msg_error = 'O valor de diária do hotel especificado não consta no banco.'
    #
    #     try:
    #         query_hotel = exec_.query(Hotel).filter_by(daily_charge=daily_charge).first()
    #         query_hotel_as_dict = Hotel.json(object_=query_hotel)
    #         return query_hotel_as_dict
    #     except AttributeError:
    #         return this_msg_error
    #
    # @staticmethod
    # def to_query_by_city(exec_, city):
    #
    #     this_msg_error = 'A cidade do hotel especificado não consta no banco.'
    #
    #     try:
    #         query_hotel = exec_.query(Hotel).filter_by(city=city).first()
    #         query_hotel_as_dict = Hotel.json(object_=query_hotel)
    #         return query_hotel_as_dict
    #     except AttributeError:
    #         return this_msg_error

    @staticmethod
    def database_insert(exec_, hotel_object):
        """
        1.0 - Mensagens de tratamento em caso de erro e sucesso
        1.1 - Var usada em condição. Se ela mudar seu valor, o objeto não será adicionado
        1.2 - Dados do banco armazenados em uma var da função
        1.3 - Iteração sob os dados do banco via atributo "hotel_id" em busca de similaridade com o parâmetro
        1.4 - Achando o que foi passado como parâmetro dentre os atributos do objeto, a var em "1.1" é modificada
        1.5 - Se a var em "1.1" não mudar, significa que o objeto não existe no banco e pode ser adicionado
        1.6 - Exibir o objeto adicionado
        1.7 - Caso contrário, avisar que o objeto já existe e não pode ser criado
        """
        # 1.0
        hotel_object_repeated = 'O nome de id de hotel "{}" já existe. Sua adição ao banco foi cancelada.'
        hotel_object_added = 'Hotel adicionado:\n{}'

        yes = None  # 1.1
        hotels_database = Hotel.database_as_var(exec_)  # 1.2

        for json in hotels_database:  # 1.3
            if json['hotel_id'] == hotel_object.hotel_id:
                yes = True  # 1.4

        if not yes:  # 1.5
            exec_.add(hotel_object)
            exec_.commit()

            # 1.6
            hotel_json = Hotel.database_query_by_hotel_id(exec_=exec_, hotel_id=hotel_object.hotel_id)
            print(hotel_object_added.format(hotel_json))

        else:  # 1.7
            print(hotel_object_repeated.format(hotel_object.hotel_id))

    @staticmethod
    def to_update(exec_, hotel_id, _key, _value):
        object_update = '\n======= ATUALIZAÇÃO DO OBJETO ======='
        _before = '======= ANTES =======\n'
        _after = '======= DEPOIS =======\n'

        target_object_then = Hotel.database_query_by_hotel_id(exec_=exec_, hotel_id=hotel_id)
        exec_.query(Hotel).filter(Hotel.hotel_id == hotel_id).update({_key: _value})
        exec_.commit()
        target_object_now = Hotel.database_query_by_hotel_id(exec_=exec_, hotel_id=hotel_id)
        print(object_update)
        print(_before, target_object_then)
        print(_after, target_object_now)

    @staticmethod
    def to_delete(exec_, hotel_id):
        object_deleted = '\n======= OBJETO DELETADO ======='
        object_to_be_deleted = Hotel.database_query_by_hotel_id(exec_=exec_, hotel_id=hotel_id)
        exec_.query(Hotel).filter(Hotel.hotel_id == hotel_id).delete()
        exec_.commit()
        print(object_deleted)
        print(object_to_be_deleted, '\n')

    # @staticmethod
    # def to_update_by_hotel_id(exec_, current, new):
    #     hotel_object_updated = 'Id do hotel atualizado\nANTES: {}\nDEPOIS: {}'
    #     exec_.query(Hotel).filter(Hotel.hotel_id == current).update({'hotel_id': new})
    #     exec_.commit()
    #     print(hotel_object_updated.format(current, new))
    #
    # @staticmethod
    # def to_update_by_name(exec_, current, new):
    #     hotel_object_updated = 'Nome do hotel atualizado\nANTES: {}\nDEPOIS: {}'
    #     exec_.query(Hotel).filter(Hotel.name == current).update({'name': new})
    #     exec_.commit()
    #     print(hotel_object_updated.format(current, new))

    # @staticmethod
    # def to_update_by_stars(exec_, current, new):
    #     hotel_object_updated = 'Classificação do  hotel atualizada\nANTES: {}\nDEPOIS: {}'
    #     exec_.query(Hotel).filter(Hotel.stars == current).update({'stars': new})
    #     exec_.commit()
    #     print(hotel_object_updated.format(current, new))

    # @staticmethod
    # def to_update_by_daily_charge(exec_, current, new):
    #     hotel_object_updated = 'Valor de diária do hotel atualizado\nANTES: {}\nDEPOIS: {}'
    #     exec_.query(Hotel).filter(Hotel.daily_charge == current).update({'daily_charge': new})
    #     exec_.commit()
    #     print(hotel_object_updated.format(current, new))
    #
    # @staticmethod
    # def to_update_by_city(exec_, current, new):
    #     hotel_object_updated = 'Cidade do hotel atualizada\nANTES: {}\nDEPOIS: {}'
    #     exec_.query(Hotel).filter(Hotel.city == current).update({'city': new})
    #     exec_.commit()
    #     print(hotel_object_updated.format(current, new))

    # @staticmethod
    # def to_delete_by_hotel_id(exec_, value):
    #
    #     exec_.query(Hotel).filter(Hotel.hotel_id == value).delete()
    #     exec_.commit()
    #
    # @staticmethod
    # def to_delete_by_name(exec_, value):
    #
    #     exec_.query(Hotel).filter(Hotel.hotel_name == value).delete()
    #     exec_.commit()

    # @staticmethod
    # def to_delete_by_stars(exec_, value):
    #
    #     exec_.query(Hotel).filter(Hotel.stars == value).delete()
    #     exec_.commit()
    #
    # @staticmethod
    # def to_delete_by_daily_charge(exec_, value):
    #
    #     exec_.query(Hotel).filter(Hotel.daily_charge == value).delete()
    #     exec_.commit()
    #
    # @staticmethod
    # def to_delete_by_city(exec_, value):
    #
    #     exec_.query(Hotel).filter(Hotel.city == value).delete()
    #     exec_.commit()

    __tablename__ = 'hoteis'

    # TODO #4.1
    id_ = Column(Integer, primary_key=True, autoincrement=True)
    hotel_id = Column(String(100))
    name = Column(String(100))
    stars = Column(Float(precision=1))
    daily_charge = Column(Float(precision=2))
    city = Column(String(100))


if __name__ == '__main__':
    # Funções dessa classe chamadas no pacote "menu"
    pass
