### Tabela de Decisão Normal

| Condições (Causas)                        |  R1   |  R2   |  R3   |  R4   |  R5   |  R6   |
| :---------------------------------------- | :---: | :---: | :---: | :---: | :---: | :---: |
| **C1.** Cód. Área (Vazio ou 3 dgt inc. 0) | **V** |   F   |   V   |   V   |   V   |   V   |
| **C2.** Prefixo (3 dgt não inc. 0)        | **V** |   V   |   F   |   V   |   V   |   V   |
| **C3.** Sufixo (4 dgt)                    | **V** |   V   |   V   |   F   |   V   |   V   |
| **C4.** Senha (6 dgt alfanuméricos)       | **V** |   V   |   V   |   V   |   F   |   V   |
| **C5.** Operação (c, d, e)                | **V** |   V   |   V   |   V   |   V   |   F   |
| **Ações (Efeitos)**                       |       |       |       |       |       |       |
| **E1.** Interface Aceita                  | **X** |       |       |       |       |       |
| **E2.** Interface Rejeitada               |       | **X** | **X** | **X** | **X** | **X** |

---

### Tabela de Decisão Reduzida

| Regra  | Condição Lógica             | Resultado       |
| :----- | :-------------------------- | :-------------- |
| **R1** | C1 ∩ C2 ∩ C3 ∩ C4 ∩ C5      | **Sucesso (V)** |
| **R2** | ¬C1 ∪ ¬C2 ∪ ¬C3 ∪ ¬C4 ∪ ¬C5 | **Falha (F)**   |
