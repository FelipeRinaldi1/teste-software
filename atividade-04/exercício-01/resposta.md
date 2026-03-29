# Análise do Grafo de Causa-Efeito

A interpretação do grafo baseia-se na lógica booleana dos conectores apresentados:

- **~ (C2):** Representa a negação de C2 ($\neg C2$).
- **V (C1, ~C2):** Representa o operador OU ($\lor$).

A expressão lógica resultante é: **E1 = C1 ∨ (¬C2)**.

### Tabela Verdade

| C1    | C2    | ¬C2   | E1 (C1 ∨ ¬C2) | Resultado      |
| :---- | :---- | :---- | :------------ | :------------- |
| V     | V     | F     | **V**         | Ocorre         |
| V     | F     | V     | **V**         | Ocorre         |
| F     | F     | V     | **V**         | Ocorre         |
| **F** | **V** | **F** | **F**         | **Não Ocorre** |

### Resposta Correta

Com base na análise, o único cenário onde o efeito **E1 não ocorre** é quando C1 é falso e C2 é verdadeiro.

**Alternativa:** "Para que E1 não ocorra é preciso {C1=.F., C2=.V.}"
