

from utils.functions import ink

allowed_numbers = ('0', '1')

# Gerenciamento
empty_database = ink('Banco de dados vazio. Não é possível deletar algo.')
wrong_data_size = ink('Foram fornecidos somente {}/{} dados.')
space_not_allowed = ink('\nPor favor, não usar espaços entre os dados, somente a vírgula.')
comma = ink('(Usar vírgula como separador, evitar espaços)')
hint = '\nDigite após a seta ---> '
operation = ink(f'\n======= Qual operação deseja realizar? ======= {ink(hint)}')
closure = ink('\nSessão encerrada. Volte sempre que precisar!\n')
roll = ink('\nPressione ENTER para continuar')
error = ink('\n========== MENSAGEM DE ERRO ==========')
warn = ink('As opções de menu vão de {} até {}.\n')

# Pesquisar dado do banco
search = ink('\n======= SESSÃO: CONSULTAR OBJETO =======')
hotel_id_name = ink(f'======= Qual o nome id do hotel procurado? ======= {ink(hint)}')
result = ink('\n======= CONTEXTO: RESULTADO DA PROCURA DO OBJETO =======')

# Adicionar dados ao banco
add_object = ink('\n======= SESSÃO: ADICIONAR OBJETO =======')
object_data = ink(f'======= Qual(is) os dados do objeto para criação? {comma} (ex: valor1,valor2,valor3...) ======= {ink(hint)}')
object_report = ink('\n======= CONTEXTO: OBJETO ADICIONADO AO BANCO? =======')
attrib_numbers_warning = ink('O limite de campos é 5: Nome id, nome do hotel, classificação, diária, cidade.')
avoid_special_characters = ink('Único caractere permitido: vírgula.')
attrib_add_tutorial = ink('Para adicionar dados, digite: valor1,valor2,valor3,valor4,valor5.')
attrib_example = ink('EXEMPLO: franciso,Hotel Francisco,4.2,397.20,Cocais.')

# Editar objeto existente do banco
edit_object_label = ink('\n======= SESSÃO: ATUALIZAR OBJETO =======')
hotel_id_name_to_edit = ink(f'\n======= Qual o nome id do hotel procurado para ser alterado? ======= {ink(hint)}')
which_one = ink(f'\n======= Escolha um valor de atributo abaixo que deve ser alterado =======')
which_field = ink(f'\n======= Qual o número do atributo? ======= {ink(hint)}')
new_value = ink(f'======= Qual o novo valor? ======= {ink(hint)}')
attrib_chosen = ink('\nAtributo escolhido: {}')
object_hotel_not_found = ink('O nome de id do hotel "{}" não foi encontrado.\n')
attempts_remaining = ink('Tentativas restantes: {}')
attempts_exceeded = ink('Número de tentativas máxima excedida: {}')
attempts_show = ink('Tentativas restantes: {}')
search_in_the_database = ink('Consulte o banco para saber o hotel de id.\n')

# Deletar objeto
delete_object_label = ink('\n======= SESSÃO: DELETAR OBJETO =======')
hotel_id_name_to_delete = ink(f'======= Qual o nome id do hotel a ser deletado? ======= {ink(hint)}')
object_to_be_deleted = ink(f'\n======= Objeto encontrado. Deseja deletar? =======')
ask_if_remove = ink(f'\n======= Confirmar a remoção? (0 = não deletar) (1 = deletar) ======= {ink(hint)}')
object_removal_canceled = ink('Remoção do objeto cancelada.\n')
object_deleted_label = ink('======= HOTEL DELETADO =======')
announcement = '\n======= INFORMAÇÃO ======='

menu_see_database = (
    '========== MENU ==========',
    'Encerrar sessão  || aperte 0',
    'Vizualizar banco || aperte 1'
)

menu_search_object = (
    '========== MENU ==========',
    'Encerrar sessão  || aperte 0',
    'Pesquisar dado   || aperte 1'
)

menu_add_object = (
    '========== MENU ==========',
    'Encerrar sessão  || aperte 0',
    'Adicionar dado   || aperte 1'
)

menu_edit_object = (
    '========== MENU ==========',
    'Encerrar sessão  || aperte 0',
    'Atualizar dado   || aperte 1'
)

menu_delete_object = (
    '========== MENU ==========',
    'Encerrar sessão  || aperte 0',
    'Deletar dado     || aperte 1'
)

menu_main = (
        "======= MENU PRINCIPAL =======",
        "Encerrar sessão  || aperte 0",
        "Visualizar banco || aperte 1",
        "Procurar dado    || aperte 2",
        "Adicionar dado   || aperte 3",
        "Editar dado      || aperte 4",
        "Deletar dado     || aperte 5",
)
