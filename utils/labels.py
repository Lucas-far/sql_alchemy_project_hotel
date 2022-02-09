

from utils.functions import ink

allowed_numbers = ('0', '1')

# Gerenciamento
hint = '\nDigite após a seta ---> '
operation = ink(f'\n======= Qual operação deseja realizar? ======= {ink(hint)}')
closure = ink('\nSessão encerrada. Volte sempre que precisar!\n')
roll = ink('\nPressione ENTER para continuar\n')
error = ink('\n========== MENSAGEM DE ERRO ==========')
warn = ink('As opções de menu vão de {} até {}.\n')

# Pesquisar dado do banco
search = ink('\n======= SESSÃO: CONSULTAR OBJETO =======')
hotel_id_name = ink(f'======= Qual o nome id do hotel procurado? ======= {ink(hint)}')
result = ink('\n======= CONTEXTO: RESULTADO DA PROCURA DO OBJETO =======')

# Adicionar dados ao banco
add_object = ink('\n======= SESSÃO: ADICIONAR OBJETO =======')
object_data = ink(f'======= Qual(is) os dados do objeto para criação? (ex: valor1,valor2,valor3...) ======= {ink(hint)}')
object_report = ink('\n======= CONTEXTO: OBJETO ADICIONADO AO BANCO? =======')
attrib_numbers_warning = ink('O limite de campos é 5: Nome id, nome do hotel, classificação, diária, cidade.')
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
attempts_remaining = 'Tentativas restantes: {}'
attempts_exceeded = 'Número de tentativas máxima excedida: 3.'
attempts_show = 'Tentativas restantes: {}'
search_in_the_bank = 'Consulte o banco para saber o hotel de id a ser editado.\n'


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
    'Atualizar dado   || aperte 1')
