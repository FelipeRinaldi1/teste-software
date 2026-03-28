| ID   | Classe de Entrada        | Dado de Entrada (Input) | Resultado Esperado (Oráculo)         | Resultado Obtido |
| :--- | :----------------------- | :---------------------- | :----------------------------------- | :--------------- |
| CE01 | Válida (Atende tudo)     | "Ab1@5678"              | "Senha Forte"                        | Passou           |
| CE02 | Inválida (Curta)         | "Ab1@5"                 | "Senha Fraca: Mínimo 8 caracteres"   | Passou           |
| CE03 | Inválida (Sem maiúscula) | "ab1@5678"              | "Senha Fraca: Falta letra maiúscula" | Passou           |
| CE04 | Inválida (Sem minúscula) | "AB1@5678"              | "Senha Fraca: Falta letra minúscula" | Passou           |
| CE05 | Inválida (Sem número)    | "Abc@efgh"              | "Senha Fraca: Falta número"          | Passou           |
| CE06 | Inválida (Sem símbolo)   | "Ab125678"              | "Senha Fraca: Falta símbolo"         | Passou           |
| CE07 | Inválida (Sem letras)    | 12345678                | "Entrada Inválida"                   | Passou           |
