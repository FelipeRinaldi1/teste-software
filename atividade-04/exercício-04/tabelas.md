# Resolução: Exercício 4 - Promoção de Frete (ADS Jacareí)

**Regra de Negócio:**

- C1: Mesma Cidade = Frete Grátis.
- C2 e C3: Outra Cidade + Quantidade > 3 + Valor >= 200 = Frete Grátis.

---

### a. Tabela de Decisão Normal

Mapeamento de todas as combinações ($2^3 = 8$).

| Condições                  |  R1   |  R2   |  R3   |  R4   |  R5   |  R6   |  R7   |  R8   |
| :------------------------- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **C1.** Mesma Cidade?      |   V   |   V   |   V   |   V   |   F   |   F   |   F   |   F   |
| **C2.** Quantidade > 3?    |   V   |   V   |   F   |   F   |   V   |   V   |   F   |   F   |
| **C3.** Valor Total >= 200 |   V   |   F   |   V   |   F   |   V   |   F   |   V   |   F   |
| **E1. Frete Grátis**       | **X** | **X** | **X** | **X** | **X** |       |       |       |
| **E2. Frete Pago**         |       |       |       |       |       | **X** | **X** | **X** |

---

### b. Tabela de Decisão Reduzida

Agrupamento por relevância das variáveis.

| Regra  | C1 (Cidade) | C2 (Qtd > 3) | C3 (Valor >= 200) | Resultado  |
| :----- | :---------: | :----------: | :---------------: | :--------- |
| **R1** |      V      |      —       |         —         | **Grátis** |
| **R2** |      F      |      V       |         V         | **Grátis** |
| **R3** |      F      |      V       |         F         | **Pago**   |
| **R4** |      F      |      F       |         V         | **Pago**   |
| **R5** |      F      |      F       |         F         | **Pago**   |

---

### c. Grafo de Causa-Efeito

O grafo utiliza um portão **E (^)** para as condições de quantidade e valor, e um portão **OU (V)** para integrar a condição de cidade.

- **Expressão Lógica:** $E1 = C1 \lor (C2 \wedge C3)$
- C2 e C3 entram em um conector **^**.
- O resultado de ^ e a causa C1 entram em um conector **V**.
- A saída do conector **V** gera o efeito E1 (Frete Grátis).

---

### d. Tabela de Decisão Otimizada (via Grafo)

Redução baseada no fluxo lógico do grafo (Short-circuit).

| Regra  | C1  | C2  | C3  | E1 (Frete Grátis) |
| :----- | :-: | :-: | :-: | :---------------: |
| **R1** |  V  |  —  |  —  |      **Sim**      |
| **R2** |  F  |  V  |  V  |      **Sim**      |
| **R3** |  F  |  F  |  —  |      **Não**      |
| **R4** |  F  |  —  |  F  |      **Não**      |

---

### e. Casos de Teste (CT)

| R      | CT   | I (Entrada: Cidade, Qtd, Valor) | S (Obtida) | O (Esperada) |
| :----- | :--- | :------------------------------ | :--------- | :----------- |
| **R1** | CT01 | (Sim, 1, 50.00)                 | True       | **True**     |
| **R2** | CT02 | (Não, 4, 200.00)                | True       | **True**     |
| **R3** | CT03 | (Não, 2, 300.00)                | False      | **False**    |
| **R4** | CT04 | (Não, 5, 150.00)                | False      | **False**    |
