| ID   | Regra / Cenário  | Input (Idade) | Oráculo (Esperado) | Resultado Obtido   | Status |
| :--- | :--------------- | :------------ | :----------------- | :----------------- | :----- |
| TC01 | T1: Idade >= 18  | 20            | "Sim"              | "Sim"              | Passou |
| TC02 | T1: Limite Exato | 18            | "Sim"              | "Sim"              | Passou |
| TC03 | T2: Idade < 18   | 10            | "Não"              | "Não"              | Passou |
| TC04 | T2: Limite Exato | 17            | "Não"              | "Não"              | Passou |
| TC05 | Entrada Inválida | -1            | "Entrada Inválida" | "Entrada Inválida" | Passou |
| TC06 | Entrada Inválida | "vinte"       | "Entrada Inválida" | "Entrada Inválida" | Passou |
