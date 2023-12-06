from operacoesbd import *

def adicionarOcorrencia(cn):

    tipoDeOcorrencia = int(input(f"Digite o tipo de ocorrência que deseja adicionar: \n1) Reclamação \n2) Elogio \n3) Sugestão"))
    if tipoDeOcorrencia == 1:
        tipoDeOcorrencia = "Reclamação"
    elif tipoDeOcorrencia == 2:
        tipoDeOcorrencia = "Elogio"
    elif tipoDeOcorrencia == 3:
        tipoDeOcorrencia = "Sugestão"
    else:
        print(f"Opção inválida")
        tituloNovaOcorrencia = input("Digite o título da nova ocorrência: ")
        if len(tituloNovaOcorrencia) == 0:
            print(f"Título inválido.")
        else:
            verificacaoUsuario = input("Deseja permanecer anônimo? \n1) Sim \n2) Não")
            if verificacaoUsuario == 1:
                usuarioNovaOcorrencia = "Anônimo"
            else:
                usuarioNovaOcorrencia = input("Digite seu nome de usuário: ")
                if len(usuarioNovaOcorrencia) == 0:
                    print("Nome de usuário inválido.")
                else:
                    descricaoNovaOcorrencia = input("Digite a descrição da nova ocorrência: ")
                    if descricaoNovaOcorrencia == 0:
                        print("Número de caracteres insuficiente.")
                    else:
                        consultaNovaOcorrencia = "insert into ocorrencias (tipo_de_ocorrencia, titulo, reclamante, descricao,) values(%s, %s, %s, %s)"

                        dados = [tipoDeOcorrencia, tituloNovaOcorrencia, usuarioNovaOcorrencia,descricaoNovaOcorrencia]
                        insertNoBancoDados(cn, consultaNovaOcorrencia, dados)

                        print(f"Ocorrência adicionada com sucesso!")
