from operacoesbd import *
def listarOcorrencias(cn):
    consultaListarOcorrencias = 'select * from ocorrencias'
    listaOcorrencias = listarBancoDados(cn, consultaListarOcorrencias)

    if listaOcorrencias:
        print('Listagem de ocorrências:')
        for ocorrencia in listaOcorrencias:
            print(
                f"Título da ocorrência: {ocorrencia[1]} \nTipo de ocorrência: {ocorrencia[2]} \nUsuário: {ocorrencia[3]} \nTítulo da ocorrência: \n Ocorrência: {ocorrencia[4]}")
    else:
        print('Não há ocorrências cadastradas no momento.')
def listarOcorrenciasTypeReclamacao(cn):
    consultaListarOcorrencias = "select * from ocorrencias where tipoDeOcorrencia = 'Reclamação'"
    listaOcorrencias = listarBancoDados(cn, consultaListarOcorrencias)

    if listaOcorrencias:
        print('Listagem de reclamações:')
        for ocorrencia in listaOcorrencias:
            print(
                f"Título da ocorrência: {ocorrencia[1]} \nTipo de ocorrência: {ocorrencia[2]} \nUsuário: {ocorrencia[3]} \nTítulo da ocorrência: \n Ocorrência: {ocorrencia[4]}")
    else:
        print('Não há ocorrências cadastradas no momento.')

def listarOcorrenciasTypeSugestao(cn):
    consultaListarOcorrencias = "select * from ocorrencias where tipoDeOcorrencia = 'Sugestão'"
    listaOcorrencias = listarBancoDados(cn, consultaListarOcorrencias)

    if listaOcorrencias:
        print('Listagem de sugestões:')
        for ocorrencia in listaOcorrencias:
            print(
                f"Título da ocorrência: {ocorrencia[1]} \nTipo de ocorrência: {ocorrencia[2]} \nUsuário: {ocorrencia[3]} \nTítulo da ocorrência: \n Ocorrência: {ocorrencia[4]}")
    else:
        print('Não há ocorrências cadastradas no momento.')

def listarOcorrenciasTypeElogio(cn):
    consultaListarOcorrencias = "select * from ocorrencias where tipoDeOcorrencia = 'Elogio'"
    listaOcorrencias = listarBancoDados(cn, consultaListarOcorrencias)

    if listaOcorrencias:
        print('Listagem de elogios:')
        for ocorrencia in listaOcorrencias:
            print(
                f"Título da ocorrência: {ocorrencia[1]} \nTipo de ocorrência: {ocorrencia[2]} \nUsuário: {ocorrencia[3]} \nTítulo da ocorrência: \n Ocorrência: {ocorrencia[4]}")
    else:
        print('Não há ocorrências cadastradas no momento.')


