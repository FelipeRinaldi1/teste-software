# Estratégia de Teste - Atividade 09

Objetivo: 100% Cobertura de Código.

## Itens Analisados

### Item A: `compute(x, y)`

- **Classes de Equivalência:**
  - `y == 0`
  - `y != 0` e `x == 0`
  - `y != 0` e `x > 0`
- **Cobertura:**
  - Teste 1: `(10, 0)` -> Cobre `if (y == 0)`
  - Teste 2: `(0, 5)` -> Cobre `else if (x == 0)`
  - Teste 3: `(5, 2)` -> Cobre loop e `i % y == 0`
  - Teste 4: `(1, 2)` -> Cobre loop sem entrar no `if` interno

### Item B: `lookup(vector, key, n)`

- **Estratégia:** Busca Binária.
- **Cobertura:**
  - Chave no meio.
  - Chave na metade inferior.
  - Chave na metade superior.
  - Chave não encontrada.

### Item C: `CoverageCodeExample`

- **Estratégia:** Exercitar ramos de exceção e condições booleanas.
- **Cobertura:**
  - `condition = True`
  - `condition = False` com strings iguais/diferentes.
  - `input_data` curto para forçar `IndexError` e cobrir blocos `except`.

### Item D: `m(i, obj)`

- **Cobertura:**
  - `obj is None`.
  - `i` ímpar (entra no `if i % 2 == 1`).
  - `i` par.
  - `i <= 0` (pula loop).

### Item E: `doSomething(x, vec)`

- **Cobertura:**
  - `x > 100` (status "less than 100").
  - `x <= 100` e `x > 0`.
  - `x <= 0`.
  - Diferentes valores de `vec[0]` para o `switch`.

### Item F: `contains(x, a, b)`

- **Cobertura:**
  - `a > b` (intervalo vazio).
  - Ponto interior, exterior (baixo/alto) e limites (fronteira).
