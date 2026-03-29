### Tabela de Decisão Normal

| Condições (Causas)                        |  R1   |  R2   |  R3   |  R4   |  R5   |
| :---------------------------------------- | :---: | :---: | :---: | :---: | :---: |
| **C1.** Tamanho entre 6 e 10              | **V** |   F   |   V   |   V   |   V   |
| **C2.** Primeiro char alfanumérico ou "?" | **V** |   V   |   F   |   V   |   V   |
| **C3.** Sem caracteres de controle        | **V** |   V   |   V   |   F   |   V   |
| **C4.** Fora do dicionário de testes      | **V** |   V   |   V   |   V   |   F   |
| **Ações (Efeitos)**                       |       |       |       |       |       |
| **E1.** Senha Aceita                      | **X** |       |       |       |       |
| **E2.** Senha Rejeitada                   |       | **X** | **X** | **X** | **X** |

---

### Tabela de Decisão Reduzida

| Regra  | Condição Lógica       | Resultado          |
| :----- | :-------------------- | :----------------- |
| **R1** | C1 ∩ C2 ∩ C3 ∩ C4     | **Sucesso (True)** |
| **R2** | ¬C1 ∪ ¬C2 ∪ ¬C3 ∪ ¬C4 | **Falha (False)**  |
