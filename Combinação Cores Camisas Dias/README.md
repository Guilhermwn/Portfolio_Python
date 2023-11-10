# README - Color-Coded Outfits for the Week

Este código Python gera uma combinação aleatória de cores para vestir camisas em cada dia da semana. Ele cria uma lista de cores e uma lista de dias da semana, embaralha a lista de cores aleatoriamente e, em seguida, atribui uma cor a cada dia da semana, imprimindo o resultado.

## Funcionamento do Código

1. Uma lista de cores (`cores`) é definida, contendo uma variedade de cores.
2. Uma lista de dias da semana (`dias_da_semana`) é definida, contendo os cinco primeiros dias úteis da semana.
3. Uma lista vazia (`cores_dias`) é inicializada para armazenar as cores atribuídas a cada dia.
4. A lista `cores` é aleatoriamente reorganizada usando a função `random.shuffle(cores)`.
5. O código entra em um loop `for` que itera através dos dias da semana, começando pela segunda-feira.
6. Em cada iteração do loop, o código atribui a cor correspondente ao dia da semana e imprime uma mensagem indicando qual cor deve ser usada para a camisa naquele dia.

## Exemplo de Saída

A saída do código será algo como:

```
Segunda-feira usarei camisa da cor Vermelho
Terça-feira usarei camisa da cor Laranja
Quarta-feira usarei camisa da cor Amarelo
Quinta-feira usarei camisa da cor Verde
Sexta-feira usarei camisa da cor Azul
```

Cada vez que o código é executado, as cores são atribuídas aleatoriamente aos dias da semana, proporcionando uma maneira divertida de escolher suas roupas para a semana.
