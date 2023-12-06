from operacoesbd import *
def pesquisarPeloCodigo(cn):

    codigoOcorrenciaPesquisada = input('Digite o código da ocorrência que deseja: ')
    consultaListarOcorrencias = 'select * from ocorrencias where codigo = ' + codigoOcorrenciaPesquisada
    listaOcorrencias = listarBancoDados(cn, consultaListarOcorrencias)

    if listaOcorrencias:
        print('Ocorrência pesquisada: ')
        for ocorrencia in listaOcorrencias:
            print(f"Título da ocorrência: {ocorrencia[1]} \nReclamante: {ocorrencia[2]} \nDescrição da ocorrência: {ocorrencia[3]}")
    else:
        print("Nenhuma ocorrência com o código informado foi encontrada.")