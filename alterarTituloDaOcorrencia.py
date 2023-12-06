from operacoesbd import *
def atualizarOcorrencia(cn):
    codigo = input('Digite o código da ocorrência que deseja alterar: ')
    novoTitulo = input('Digite o novo titulo da ocorrência: ')

    atualizarTituloDaOcorrencia = 'update ocorrencias set titulo = %s where codigo = %s'
    valores = [novoTitulo, codigo]

    linhasAtualizadas = atualizarBancoDados(cn, atualizarTituloDaOcorrencia, valores)
    if linhasAtualizadas:
        print('Título da ocorrência alterado com sucesso!')
    else:
        print(f"Não foi possível concluir a operação.")