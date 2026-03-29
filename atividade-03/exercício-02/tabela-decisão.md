### Tabela de Decisão Normal

Esta tabela apresenta o cenário de sucesso e as falhas individuais de cada requisito.

| Condições (Causas)       | R1 (Sucesso) |  R2   |  R3   |  R4   |  R5   |  R6   |
| :----------------------- | :----------: | :---: | :---: | :---: | :---: | :---: |
| **C1.** Tamanho $\ge$ 8  |    **V**     |   F   |   V   |   V   |   V   |   V   |
| **C2.** Possui Maiúscula |    **V**     |   V   |   F   |   V   |   V   |   V   |
| **C3.** Possui Minúscula |    **V**     |   V   |   V   |   F   |   V   |   V   |
| **C4.** Possui Número    |    **V**     |   V   |   V   |   V   |   F   |   V   |
| **C5.** Possui Símbolo   |    **V**     |   V   |   V   |   V   |   V   |   F   |
| **Ações (Efeitos)**      |              |       |       |       |       |       |
| **E1.** Senha Forte      |    **X**     |       |       |       |       |       |
| **E2.** Senha Fraca      |              | **X** | **X** | **X** | **X** | **X** |

---

### Tabela de Decisão Reduzida

Lógica simplificada focada no resultado binário do sistema.

| Regra  | Condição Lógica                         | Resultado (Efeito) |
| :----- | :-------------------------------------- | :----------------- |
| **R1** | C1, C2, C3, C4 e C5 são **Verdadeiros** | **Senha Forte**    |
| **R2** | Qualquer condição (C1 a C5) é **Falsa** | **Senha Fraca**    |
