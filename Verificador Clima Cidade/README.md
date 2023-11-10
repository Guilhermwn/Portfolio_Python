# README - Verificador de Clima

Este é um programa Python chamado `Verificador de Clima`, que permite verificar o clima de uma cidade específica. O programa utiliza a API OpenWeatherMap.org para obter informações climáticas em tempo real.

## Funcionamento do Código

1. O programa começa perguntando se o usuário deseja um tutorial de como usá-lo. O tutorial é uma breve explicação sobre como inserir o nome da cidade para verificar o clima.

2. O código permite que o usuário escolha se deseja ou não o tutorial. Se escolher "Sim," o tutorial será exibido, caso contrário, o programa continuará sem ele.

3. Após o tutorial ou a mensagem de boas-vindas, o código entra em um loop infinito, onde o usuário pode verificar o clima de diferentes cidades.

4. O usuário insere o nome da cidade que deseja verificar o clima.

5. O código cria um link para verificar a cidade na API do OpenWeatherMap.org e obtém os dados climáticos em formato JSON.

6. Os dados do JSON são analisados, e informações sobre a cidade, clima, temperatura, umidade, vento e se é dia ou noite são exibidas na tela.

7. Após a exibição dos dados climáticos, o programa pergunta se o usuário deseja verificar o clima de outra cidade. Se a resposta for "Sim," o processo é repetido. Se a resposta for "Não," o programa agradece ao usuário e encerra.

## Exemplo de Saída

O programa exibirá informações como o nome da cidade, país, clima, temperatura, sensação térmica, umidade, velocidade do vento e se é dia ou noite na cidade escolhida. Aqui está um exemplo de saída:

```
Digite o nome da cidade a verificar o clima: São Paulo

☁️ LOCALIZAÇÃO☁️
Cidade: São Paulo
País: BR

☁️️️ ️️️️️CLIMA☁️
Clima: Nublado

☁️️️️ ️️️️️TEMPERATURA☁️
Temperatura atual: 23ºC
Sensação térmica: 23ºC

☁️️️️ ️️️️️EXTRAS☁️
Humidade: 60%
Vento: 8 Km/h
Em São Paulo está de dia agora

Deseja verificar o clima de outra cidade?
sim(y) ou Não(n)
```

## Observações

- O código possui uma opção para reiniciar a verificação do clima de outra cidade.
- Ele utiliza uma API do OpenWeatherMap.org, então é necessário ter uma conexão com a internet para funcionar.
- Certifique-se de ter a biblioteca `requests` instalada para fazer solicitações à API.

Este código é uma ferramenta útil para verificar o clima de cidades e pode ser personalizado e aprimorado conforme necessário.