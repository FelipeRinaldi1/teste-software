| ID   | Cenário                   | Input (Tempo, Saldo) | Oráculo                   | Status |
| :--- | :------------------------ | :------------------- | :------------------------ | :----- |
| TC01 | T1: Ambas condições OK    | 3 anos, R$ 2500      | "Sim"                     | Passou |
| TC02 | T1: Limites exatos        | 2 anos, R$ 2000      | "Sim"                     | Passou |
| TC03 | T2: Tempo OK, Saldo Baixo | 2 anos, R$ 1999      | "Não"                     | Passou |
| TC04 | T3: Tempo Baixo, Saldo OK | 1 ano, R$ 3000       | "Não"                     | Passou |
| TC05 | T4: Ambos Baixos          | 1 ano, R$ 500        | "Não"                     | Passou |
| TC06 | Inválido: Valor Negativo  | -1 ano, R$ 2000      | "Erro: Valores Negativos" | Passou |
| TC07 | Inválido: Tipo de dado    | "2 anos", 2000       | "Erro: Entrada Inválida"  | Passou |
