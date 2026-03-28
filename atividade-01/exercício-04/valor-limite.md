| ID   | Campo / Fronteira     | Dado de Entrada (Input) | Resultado Esperado (Oráculo)    | Resultado Obtido |
| :--- | :-------------------- | :---------------------- | :------------------------------ | :--------------- |
| VL01 | Cód. Área (2 dígitos) | "01"                    | "Erro: Código de área inválido" | Passou           |
| VL02 | Cód. Área (3 dígitos) | "011"                   | "Operação ... autorizada"       | Passou           |
| VL03 | Prefixo (3 dígitos)   | "344"                   | "Operação ... autorizada"       | Passou           |
| VL04 | Sufixo (3 dígitos)    | "259"                   | "Erro: Sufixo inválido"         | Passou           |
| VL05 | Sufixo (4 dígitos)    | "2598"                  | "Operação ... autorizada"       | Passou           |
| VL06 | Senha (5 chars)       | "abc12"                 | "Erro: Senha inválida"          | Passou           |
| VL07 | Senha (6 chars)       | "abc123"                | "Operação ... autorizada"       | Passou           |
| VL08 | Senha (7 chars)       | "abc1234"               | "Erro: Senha inválida"          | Passou           |
