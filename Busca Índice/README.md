# README - Buscador de Índice

Este é um programa Python que realiza uma busca em uma lista e retorna os índices onde um determinado número ocorre na lista.

## Funcionamento do Código

1. Uma lista chamada `lista` contendo números é definida no início do programa.
2. Uma função chamada `indiceSearch` é definida para realizar a busca. Ela recebe dois argumentos: a lista na qual a busca será feita e o número a ser procurado.
3. Dentro da função `indiceSearch`, um loop `for` itera por toda a lista. Cada elemento da lista é comparado com o número que estamos procurando.
4. Se o número da lista for igual ao número procurado, o índice onde esse número ocorre é adicionado a uma lista chamada `indices`.
5. Após o loop, a lista de índices é retornada pela função.
6. O programa principal solicita ao usuário que insira um número. Este número será o número que queremos buscar na lista.
7. O programa chama a função `indiceSearch` passando a lista `lista` e o número inserido pelo usuário como argumentos.
8. A função retorna os índices onde o número ocorre na lista e imprime-os na tela.

## Exemplo de Saída

Suponha que a lista `lista` seja `[7, 1, 2, 7, 0, 2, 8, 7]`, e o usuário insira o número `7`. A saída será:

```
7
[0, 3, 7]
```

Isso significa que o número `7` ocorre nos índices 0, 3 e 7 da lista.

## Observações

- Este código é útil quando você deseja encontrar a posição de todas as ocorrências de um número em uma lista.
- Pode ser personalizado para buscar outros tipos de elementos em uma lista.

## Evolução do Código

O código atual para busca de índices foi desenvolvido com base em um código criado quando o autor começou a estudar Python em 2022. O código original era assim:

```python
def indecx(lista, numero):
    if lista.count(numero) == 1:
        return lista.index(numero)
    elif lista.count(numero) > 1:
        for i in lista:
            return lista.index(numero), lista.index(numero, lista.index(numero) + 1)
```

Este código original fazia a busca, mas tinha algumas limitações. Ele só funcionava corretamente se houvesse uma única ocorrência do número na lista ou se o número se repetisse em pares. Além disso, não retornava todas as ocorrências.

Com o aprendizado posterior em Python, o autor decidiu aprimorar a funcionalidade do código e criar uma nova versão que pudesse lidar com múltiplas ocorrências do número na lista, retornando todos os índices onde o número fosse encontrado.

Assim, o código atual foi desenvolvido para oferecer uma solução mais versátil e eficaz para a busca de índices em uma lista.

## Exemplo de Uso

O código atual permite que você encontre todos os índices onde um número específico ocorre em uma lista, tornando-o mais flexível e útil em diversas situações.

Sinta-se à vontade para utilizar e personalizar este código de acordo com suas necessidades.
