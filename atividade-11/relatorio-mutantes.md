# Teste de Mutantes - Atividade 11

Equivalente ao Pitest (Java).

## Ferramenta `mutmut`

Para rodar o teste de mutantes em Python:

1. Ative o ambiente virtual.
2. Execute:
   ```bash
   mutmut run --paths-to-mutate atividade-11/exercicio-01
   ```
3. Veja os resultados:
   ```bash
   mutmut results
   ```

## Resultados Esperados

- Mutantes gerados em operadores lógicos (`==` -> `!=`, `>` -> `>=`).
- Mutantes em operações aritméticas (`%`, `+`, `-`).
- Os testes implementados devem matar 100% dos mutantes lógicos básicos.
