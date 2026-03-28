| ID   | Fronteira Testada       | Dado de Entrada (Input) | Resultado Esperado (Oráculo)             | Resultado Obtido |
| :--- | :---------------------- | :---------------------- | :--------------------------------------- | :--------------- |
| VL01 | Comprimento 5 (abaixo)  | "12345"                 | "Erro: Tamanho inválido (deve ser 6-10)" | Passou           |
| VL02 | Comprimento 6 (mínimo)  | "123456"                | "Senha Válida"                           | Passou           |
| VL03 | Comprimento 10 (máximo) | "A123456789"            | "Senha Válida"                           | Passou           |
| VL04 | Comprimento 11 (acima)  | "A1234567890"           | "Erro: Tamanho inválido (deve ser 6-10)" | Passou           |
| VL05 | Primeiro char: Letra    | "Abcdef"                | "Senha Válida"                           | Passou           |
| VL06 | Primeiro char: Número   | "1bcdef"                | "Senha Válida"                           | Passou           |
| VL07 | Primeiro char: "?"      | "?bcdef"                | "Senha Válida"                           | Passou           |
