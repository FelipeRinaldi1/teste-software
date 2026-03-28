| ID   | Classe de Entrada      | Input | Oráculo                             | Resultado Obtido   | Status |
| :--- | :--------------------- | :---- | :---------------------------------- | :----------------- | :----- |
| CE01 | Inválida (Negativa)    | -5    | "Entrada Inválida"                  | "Entrada Inválida" | Passou |
| CE02 | Válida (0 a 15)        | 10    | "Não empregar"                      | "Não empregar"     | Passou |
| CE03 | Válida (16 a 17)       | 16    | "Pode ser empregado tempo parcial"  | "Pode ser..."      | Passou |
| CE04 | Válida (18 a 54)       | 30    | "Pode ser empregado tempo integral" | "Pode ser..."      | Passou |
| CE05 | Válida (55 a 98)       | 70    | "Não empregar"                      | "Não empregar"     | Passou |
| CE06 | Inválida (Acima de 98) | 100   | "Entrada Inválida"                  | "Entrada Inválida" | Passou |
