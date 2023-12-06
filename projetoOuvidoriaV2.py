'''
Alunos: Luiz Matheus,
Lucas Diniz,
Eduarda Pereira,
Pedro Lucas,
Maria Eduarda Almeida,
Vitor Ian.
'''
from operacoesbd import *
from alterarTituloDaOcorrencia import *
from listarOcorrencias import *
from adicionarOcorrencia import *
from pesquisarPeloCodigo import *
from removerOcorrencia import *
cn = criarConexao("localhost", "root", "12345", "ocorrencias")


opcao = 123
while opcao != 5:
    print(f"1) Listar reclamções \n2) Adicionar reclamções \n3) Pesquisar reclamções por código \n4) Remover reclamção \n5) Mudar título da ocorrência \n6) Sair")

    opcao = int(input("Digite uma opção: "))

    if opcao == 1:
        listarOcorrencias(cn)

    elif opcao == 2:
        adicionarOcorrencia(cn)

    elif opcao == 3:
        pesquisarPeloCodigo(cn)

    elif opcao == 4:
        removerOcorrenciaPorCodigo(cn)
    elif opcao == 5:
        atualizarOcorrencia(cn)
    elif opcao != 6:
        print("Opção inválida.")
encerrarBancoDados(cn)

print(f"Obrigado por usar a ouvidoria!")
