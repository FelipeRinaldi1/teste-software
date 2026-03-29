### Tabela de Decisão Padrão (Normal)

Esta tabela mapeia todas as condições exclusivas individualmente.

| Condições (Causas)                   |  R1   |  R2   |  R3   |  R4   |
| :----------------------------------- | :---: | :---: | :---: | :---: |
| **C1.** $0 \le \text{idade} \le 15$  | **V** |   F   |   F   |   F   |
| **C2.** $16 \le \text{idade} \le 17$ |   F   | **V** |   F   |   F   |
| **C3.** $18 \le \text{idade} \le 54$ |   F   |   F   | **V** |   F   |
| **C4.** $55 \le \text{idade} \le 99$ |   F   |   F   |   F   | **V** |
| **Ações (Efeitos)**                  |       |       |       |       |
| **E1.** Não empregar                 | **X** |       |       | **X** |
| **E2.** Tempo Parcial                |       | **X** |       |       |
| **E3.** Tempo Integral               |       |       | **X** |       |

---

### Tabela de Decisão Reduzida

| Regras Agrupadas | Condição Lógica                          | Efeito (Ação)                         |
| :--------------- | :--------------------------------------- | :------------------------------------ |
| **R1 + R4**      | $\text{idade} \in [0, 15] \cup [55, 99]$ | **Não empregar**                      |
| **R2**           | $\text{idade} \in [16, 17]$              | **Pode ser empregado tempo parcial**  |
| **R3**           | $\text{idade} \in [18, 54]$              | **Pode ser empregado tempo integral** |
