| ID | Campo | Entrada Testada | Resultado Esperado (Oráculo) | Resultado Obtido |
| :--- | :--- | :--- | :--- | :--- |
| CE01 | Todos | "011", "344", "2598", "abc123", "c" | "Operação Cheque autorizada" | Passou |
| CE02 | Cód. Área | "111" (Não inicia com 0) | "Erro: Código de área inválido" | Passou |
| CE03 | Cód. Área | "" (Vazio) | "Operação ... autorizada" | Passou |
| CE04 | Prefixo | "044" (Inicia com 0) | "Erro: Prefixo inválido" | Passou |
| CE05 | Sufixo | "ABCD" (Não numérico) | "Erro: Sufixo inválido" | Passou |
| CE06 | Senha | "ab@123" (Caractere especial) | "Erro: Senha inválida" | Passou |
| CE07 | Comando | "x" (Não existente) | "Erro: Comando inválido" | Passou |