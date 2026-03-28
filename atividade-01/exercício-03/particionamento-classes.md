| ID   | Classe de Entrada    | Dado de Entrada (Input) | Resultado Esperado (Oráculo)                      | Resultado Obtido |
| :--- | :------------------- | :---------------------- | :------------------------------------------------ | :--------------- |
| CE01 | Válida (Tudo OK)     | "Senha123"              | "Senha Válida"                                    | Passou           |
| CE02 | Tamanho Insuficiente | "Abc1"                  | "Erro: Tamanho inválido (deve ser 6-10)"          | Passou           |
| CE03 | Tamanho Excessivo    | "SenhaMuitoLonga"       | "Erro: Tamanho inválido (deve ser 6-10)"          | Passou           |
| CE04 | Início Inválido      | "@senha1"               | "Erro: Primeiro caractere inválido"               | Passou           |
| CE05 | Caractere Controle   | "Senha" + chr(10)       | "Erro: Contém caracteres de controle"             | Passou           |
| CE06 | Termo Restrito       | "funcional"             | "Erro: Senha consta na lista de termos restritos" | Passou           |
| CE07 | Tipo Inválido        | 123456                  | "Entrada Inválida"                                | Passou           |
