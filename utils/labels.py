

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