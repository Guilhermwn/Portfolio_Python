# README - Gerador Info Usuario

O script utiliza duas APIs externas para coletar informações e criar um arquivo de texto personalizado com base nos dados fornecidos pelo usuário. A seguir, fornecemos uma visão geral do código e do que ele faz.

## Funcionalidades

- Coleta informações do usuário, como nome e idade.
- Utiliza a API [https://ipfind.com/](https://ipfind.com/) para obter informações relacionadas ao endereço IP, como endereço IP, cidade e região/estado.
- Utiliza a API [http://worldtimeapi.org/api/ip](http://worldtimeapi.org/api/ip) para obter informações sobre data e hora com base no IP do usuário.
- Gera um arquivo de texto personalizado com as informações coletadas.
- Nomeia o arquivo com um número aleatório e o nome do usuário.
- Armazena as informações no arquivo, incluindo nome, idade, endereço IP, cidade, região/estado, data atual e hora atual.

## Pré-requisitos

- O programa utiliza a biblioteca `requests`, portanto, certifique-se de que ela esteja instalada em seu ambiente Python.

```bash
pip install requests
```

## Utilização

1. Execute o programa e siga as instruções para fornecer seu nome e idade.
2. O programa usará a API IPFind para obter informações sobre seu endereço IP, como cidade e região/estado.
3. Em seguida, ele usará a API WorldTimeAPI para obter informações sobre a data e a hora com base no seu IP.
4. Todas essas informações serão armazenadas em um arquivo de texto personalizado com um nome gerado aleatoriamente.
5. O programa indicará que o arquivo foi gerado com sucesso.
6. **Arquivo gerado:**

   Após a execução bem-sucedida do código, um arquivo de texto será gerado com um nome aleatório que inclui o número gerado aleatoriamente, seu nome e a extensão ".txt". Por exemplo, "42 - SeuNome.txt".

Este código é útil para coletar informações relacionadas à localização e ao horário do usuário e pode ser adaptado para atender a diversas necessidades. Sinta-se à vontade para usá-lo como ponto de partida e personalizá-lo de acordo com seus requisitos.

## Funções Auxiliares

O módulo `new_file` é uma parte do projeto que lida com a criação e manipulação de arquivos. Ele contém duas funções auxiliares: `Create_File` e `Append_InFile`, que são usadas para criar e atualizar um arquivo com informações específicas.

1. `Create_File(file_Name, idade, nome)`: Esta função é responsável por criar um novo arquivo com o nome especificado (definido pelo usuário) e preenche esse arquivo com informações iniciais, como o nome e a idade da pessoa. Aqui está o que cada parte da função faz:
   - `file = open(file_Name, "w")`: Abre o arquivo especificado para escrita.
   - `file.write("-" * 20)`: Escreve uma linha de traços para criar uma barreira.
   - `file.write("Nome: ")` e `file.write(idade)`: Escreve o nome e idade fornecidos no arquivo.
   - `file.close()`: Fecha o arquivo após a escrita ter sido concluída.

2. `Append_InFile(file_Name, ip_address, city, region, data, horario)`: Essa função é usada para adicionar informações adicionais ao arquivo criado anteriormente. Ela acrescenta informações sobre o endereço IP, cidade, região, data e horário. Aqui está o que cada parte da função faz:
   - `filee = open(file_Name, "a")`: Abre o arquivo especificado para anexar informações, em vez de substituir o conteúdo existente.
   - `filee.write("-" * 20)`: Escreve uma linha de traços para criar uma barreira.
   - `filee.write("Endereco IP: ")` e `filee.write(ip_address)`: Adiciona o endereço IP ao arquivo.
   - `filee.write("Cidade: ")` e `filee.write(city)`: Adiciona a cidade ao arquivo.
   - `filee.write("Estado: ")` e `filee.write(region)`: Adiciona o estado ou região ao arquivo.
   - `filee.write(data)`: Adiciona a data atual.
   - `filee.write(horario)`: Adiciona o horário atual.
   - `filee.close()`: Fecha o arquivo após a escrita ter sido concluída.

Essas funções são úteis para criar um arquivo de texto e preenchê-lo com informações relevantes, tornando o projeto capaz de coletar informações, armazená-las e disponibilizá-las para consulta posterior. Isso pode ser útil em várias aplicações, como o rastreamento de informações de usuários ou registros de eventos.

## Notas

- Este código é um exemplo simples de como fazer solicitações de API e manipular dados em Python.
- Certifique-se de não compartilhar informações confidenciais, pois este código coleta informações sobre seu endereço IP.
- Lembre-se de que as chaves de autenticação da API devem ser mantidas em sigilo. Não compartilhe sua chave publicamente.

Este é um exemplo básico de código e pode ser expandido ou modificado para atender a diferentes requisitos ou integrado a outros projetos. Use-o com responsabilidade e de acordo com os termos de uso das APIs que você acessar.