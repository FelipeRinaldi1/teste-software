### 5.a) Tabela de Decisão Normal

| Condições (Causas)          |  R1   |  R2   |  R3   |  R4   |  R5   |  R6   |  R7   |  R8   |
| :-------------------------- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **C1.** Mesma Cidade?       |   V   |   V   |   V   |   V   |   F   |   F   |   F   |   F   |
| **C2.** Quantidade > 3?     |   V   |   V   |   F   |   F   |   V   |   V   |   F   |   F   |
| **C3.** Valor Total >= 200? |   V   |   F   |   V   |   F   |   V   |   F   |   V   |   F   |
| **Ações (Efeitos)**         |       |       |       |       |       |       |       |       |
| **E1.** Frete Grátis        | **X** | **X** | **X** | **X** | **X** |       |       |       |
| **E2.** Frete Pago          |       |       |       |       |       | **X** | **X** | **X** |

---

### 5.b) Tabela de Decisão Reduzida

| Regras Agrupadas | Condição Lógica                                    | Resultado        |
| :--------------- | :------------------------------------------------- | :--------------- |
| **R1 a R4**      | Mesma Cidade = **Sim** (Independente de Qtd/Valor) | **Frete Grátis** |
| **R5**           | Mesma Cidade = **Não** ∩ Qtd > 3 ∩ Valor >= 200    | **Frete Grátis** |
| **R6 a R8**      | Mesma Cidade = **Não** ∩ (Qtd <= 3 ∪ Valor < 200)  | **Frete Pago**   |
