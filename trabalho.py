import os
dir = ".\planilha.csv"
dir2 = ".\planilharesultado.csv"

# - Apresentar um relatório com o número de linhas do documento original, e os nomes
# das colunas, que descrevem os dados;

def rel_linhas(): 
          
    file = open(dir, "r")
    linhas = file.readlines()
    num_linhas = len(linhas)

    print(f"O arquivo {dir} tem {num_linhas} linhas.")
    print(f"Colunas: {linhas[0]}")

# - Criar arquivo de Resumo - Deverá apresentar dados agrupados, com totalizadores.

# - Apresentar dados estatísticos sobre o arquivo, pode ser gerado média, moda,
# desvio padrão, entre outros.

def media_idade(): 
    soma = 0
    lista = []
    file = open(dir, "r")
    
    for linha in file.readlines():
        partes = linha.split(";")
        idade_str = partes[8].strip()
          
        if idade_str and idade_str != "IDADE":  
            idade = int(idade_str)
            lista.append(idade)
            
    file.close() 

    if lista:
        soma = sum(lista)
        media = soma / len(lista)
        print(f"A média das idades é: {media}")
    else:
        print("Não existem idades válidas para calcular a média.")

# - Realizar uma busca de dados no(s) arquivo(s).
def busca_sexo():
    sexo = input("Você deseja buscar por Masculino [M] ou Feminino [F]")
    file = open (dir, "r")
    
    for linha in file.readlines():
        partes = linha.split(";")
        sep_sexo = partes[7].strip()
        
        if sexo == "M" and sep_sexo == "M":
            print(linha)
        elif sexo == "F" and sep_sexo == "F":
            print(linha)

    file.close()
    
# - Criar um arquivo parcial, com nome informado pelo usuário, que armazenará os
# dados correspondentes a uma filtragem de dados. Para este arquivo, também
# deverá ser possível chamar a função de relatório anterior.

def busca_calibre():
    calibre_busca = input("Digite o calibre para a busca: ")

    file = open (dir, "r")
    temp_file = open (dir2, "w")

    for linha in file:
        partes = linha.strip().split(";")
            
        calibre_arma = partes[6].strip()

        if calibre_arma == calibre_busca:
            temp_file.write(linha)
            print(linha)
            print("Arquivo Adicionado à nova planilha no Diretório.")

def pes_tipoarma():
    tipo_arma_busca = input("Digite o tipo de arma para a busca: ")

    file = open(dir, "r")

    for linha in file:
        partes = linha.strip().split(";")
        
        tipo_arma = partes[4].strip()

        if tipo_arma == tipo_arma_busca:
            print(linha)

    file.close()

def busca_ano():
    ano_busca = input("Digite o ano para a busca: ")

    file = open(dir, "r")

    for linha in file:
        partes = linha.strip().split(";")
        
        ano = partes[0].strip()

        if ano == ano_busca:
            print(linha)

    file.close()

entrada = 1
while entrada != 0:
    entrada = int(input("Qual opção você deseja? \n(1)Número de linhas e nome das colunas do Relatório \n(2)Média de Idade \n(3)Busca por Sexo \n(4)Busca por calibre \n(5)Busca por Tipo de Arma \n(6)Busca por ano \n(0)Sair \n"))
    print()
    
    if entrada == 1:
        print()
        rel_linhas()
    elif entrada == 2:
        print()
        media_idade()    
    elif entrada == 3:
        print()
        busca_sexo()
    elif entrada == 4:
        print()
        busca_calibre()
    elif entrada == 5:
        print()
        pes_tipoarma()     
    elif entrada == 6:
        print()
        busca_ano()        




