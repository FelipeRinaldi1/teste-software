| ID   | Fronteira Testada       | Input | Oráculo                             | Resultado Obtido   | Status |
| :--- | :---------------------- | :---- | :---------------------------------- | :----------------- | :----- |
| VL01 | Limite Mínimo           | 0     | "Não empregar"                      | "Não empregar"     | Passou |
| VL02 | Transição (Fim Faixa 1) | 15    | "Não empregar"                      | "Não empregar"     | Passou |
| VL03 | Transição (Ini Faixa 2) | 16    | "Pode ser empregado tempo parcial"  | "Pode ser..."      | Passou |
| VL04 | Transição (Fim Faixa 2) | 17    | "Pode ser empregado tempo parcial"  | "Pode ser..."      | Passou |
| VL05 | Transição (Ini Faixa 3) | 18    | "Pode ser empregado tempo integral" | "Pode ser..."      | Passou |
| VL06 | Transição (Fim Faixa 3) | 54    | "Pode ser empregado tempo integral" | "Pode ser..."      | Passou |
| VL07 | Transição (Ini Faixa 4) | 55    | "Não empregar"                      | "Não empregar"     | Passou |
| VL08 | Transição (Fim Faixa 4) | 98    | "Não empregar"                      | "Não empregar"     | Passou |
| VL09 | Limite Máximo Excedido  | 99    | "Entrada Inválida"                  | "Entrada Inválida" | Passou |
