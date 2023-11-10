import os
import xmltodict
import pandas as pd

# Informaçõs que deseja-se ser coletadas:
# - Numero da nota
# - Emissor da nota 
# - Nome do cliente
# - Endereço completo e separado(Rua numero e municipio)
# - Peso bruto

def pegar_info(nome_arquivo, valores):
    print(f"Arquivo {arquivo} acessado com sucesso!")
    with open(f"nfs/{nome_arquivo}", "rb") as arquivo_xml: 
        dic_arquivo = xmltodict.parse(arquivo_xml)

        try:
            if "NFe" in dic_arquivo:
                infos_nf = dic_arquivo["NFe"]["infNFe"]
            else:
                infos_nf = dic_arquivo["nfeProc"]["NFe"]["infNFe"]
            numero_nota = infos_nf["@Id"]
            empresa_emissora = infos_nf["emit"]["xNome"]
            nome_cliente = infos_nf["dest"]["xNome"]
            endereco = infos_nf["dest"]["enderDest"]
            if "vol" in infos_nf["transp"]:
                peso_bruto = infos_nf["transp"]["vol"]["pesoB"]
            else:
                peso = "Não informado"
            valores.append([numero_nota, empresa_emissora, nome_cliente, endereco, peso_bruto])
        except Exception as e:
            print(f"Erro encontrado em: {e}, no arquivo {nome_arquivo}")



lista_arquivos = os.listdir("nfs")

colunas = ["Numero da nota", "Empresa emissora", "Nome do cliente", "Endereço", "Peso"]
valores = []

for arquivo in lista_arquivos:
    pegar_info(arquivo, valores)


tabela = pd.DataFrame(columns = colunas, data = valores)

tabela.to_excel("NotasFiscais.xlsx", index = False)

print(f"Planilha 'NotasFiscais.xlsx' criado com sucesso!")
