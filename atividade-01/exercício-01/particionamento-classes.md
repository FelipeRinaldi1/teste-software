| ID   | Classe de Entrada       | Dado de Entrada (Input) | Resultado Esperado (Oráculo)        | Resultado Obtido |
| :--- | :---------------------- | :---------------------- | :---------------------------------- | :--------------- |
| CE01 | Inválida (Menor que 0)  | -1                      | "Entrada Inválida"                  | Passou           |
| CE02 | Válida (0 a 15)         | 10                      | "Não empregar"                      | Passou           |
| CE03 | Válida (16 a 17)        | 16                      | "Pode ser empregado tempo parcial"  | Passou           |
| CE04 | Válida (18 a 54)        | 35                      | "Pode ser empregado tempo integral" | Passou           |
| CE05 | Válida (55 a 99)        | 70                      | "Não empregar"                      | Passou           |
| CE06 | Inválida (Maior que 99) | 100                     | "Entrada Inválida"                  | Passou           |
