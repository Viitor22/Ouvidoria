from operacoesbd import *
def removerOcorrenciaPorCodigo(cn):
    codigoRemover = input('Digite o codigo da ocorrencia que deseja remover: ')
    consultaListagem = 'delete from ocorrencias where codigo = %s '
    dados = [codigoRemover]

    linhasRemovidas = excluirBancoDados(cn, consultaListagem, dados)
    if linhasRemovidas > 0:
        print('Ocorrência removida com sucesso!')
    else:
        print('Não existe Ocorrência para o código informado!')