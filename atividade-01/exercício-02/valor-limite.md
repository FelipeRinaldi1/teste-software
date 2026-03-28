| ID   | Fronteira Testada         | Dado de Entrada (Input) | Resultado Esperado (Oráculo)       | Resultado Obtido |
| :--- | :------------------------ | :---------------------- | :--------------------------------- | :--------------- |
| VL01 | Limite inferior (7 chars) | "Ab1@567"               | "Senha Fraca: Mínimo 8 caracteres" | Passou           |
| VL02 | Limite exato (8 chars)    | "Ab1@5678"              | "Senha Forte"                      | Passou           |
| VL03 | Acima do limite (9 chars) | "Ab1@56789"             | "Senha Forte"                      | Passou           |
| VL04 | Vazio                     | ""                      | "Senha Fraca: Mínimo 8 caracteres" | Passou           |
