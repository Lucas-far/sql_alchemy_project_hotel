

from utils.functions import ink

allowed_numbers = ('0', '1')

# Common labels
hint = '\nDigite após a seta ---> '
operation = f'\n======= Qual operação deseja realizar? ======= {ink(hint)}'
closure = ink('\nSessão encerrada. Volte sempre que precisar!\n')
roll = ink('Pressione ENTER para continuar\n')
error = ink('\n========== MENSAGEM DE ERRO ==========')
warn = 'As opções de menu vão de {} até {}.\n'

# múltiplos: menu/id_2_query_specific.py
attempts_exceeded = 'Número de tentativas excedida.'
search_in_the_database = 'Consulte o banco para saber o id do hotel.\n'
object_hotel_not_found = 'O nome de id do hotel "{}" não foi encontrado.\n'
attempts_remaining = 'Tentativas restantes: {}'

# menu/id_2_query_specific.py
ask_hotel_id_name = f'======= Qual o nome id do hotel procurado? ======= {ink(hint)}'
query_result = ink('\n======= RESULTADO DA BUSCA DO OBJETO =======')

# menu/id_3_insert
object_attribs = ink('\nATRIBUTOS POSSÍVEIS (5): hotel_id,name,stars,daily_charge,city')
object_data = f'======= Qual(is) os dados do objeto para criação? ======= {ink(hint)}'
object_report = ink('\n======= OBJETO ADICIONADO =======')
# Tratamento
attrib_numbers_warning = 'O limite de campos é 5: Nome id, nome do hotel, classificação, diária, cidade.'
object_data_rules = ink('Usar vírgula como separador, não usar espaços')
object_example = f'{ink(object_data_rules)}    EXEMPLO: franciso,Hotel Francisco,4.2,397.20,Cocais'

# menu/id_4_object_reshape.py
ask_target_hotel_id = f'\n======= Qual o nome id do hotel procurado para ser alterado? ======= {ink(hint)}'
ask_attrib_value = f'\n======= Escolha um valor de atributo abaixo que deve ser alterado ======='
type_attrib_value = f'\n======= Qual o número do atributo a ser editado (apenas o número)? ======= {ink(hint)}'
back_to_menu = ink('Pressione 0 caso tenha desistido')
new_attrib_value = f'======= Qual o novo valor? ======= {ink(hint)}'
attrib_chosen = ink('\nAtributo escolhido: {}')

# Gerenciamento
empty_database = ink('Banco de dados vazio. Não é possível deletar algo.')
wrong_data_size = ink('Foram fornecidos somente {}/{} dados.')
space_not_allowed = ink('\nPor favor, não usar espaços entre os dados, somente a vírgula.')

# Deletar objeto
type_hotel_id_to_be_deleted = f'\n======= Qual o nome id do hotel a ser deletado? ======= {ink(hint)}'
ask_if_remove = f'\n======= Confirmar a remoção? {ink("(0 = cancelar)")} {ink("(1 = deletar)")} ======= {ink(hint)}'
announcement = ink('\n======= INFORMAÇÃO =======')
object_removal_canceled = 'Remoção do objeto cancelada.\n'
