# Conclusão: Grafo de Causa-Efeito (E / NÃO)

O grafo utiliza o conector **^ (E)** e uma negação **~ (NÃO)** na entrada C3.
A lógica resultante é: **E1 = C1 AND C2 AND (NOT C3)**.

### Por que a Alternativa C?

Para que um portão **E** (AND) seja verdadeiro, todas as suas entradas devem ser verdadeiras.

- Entrada 1 (C1): deve ser **V**.
- Entrada 2 (C2): deve ser **V**.
- Entrada 3 (~C3): para ser verdadeira, o valor original de C3 deve ser **F**.

A **Regra 1 (R1)** da Alternativa **C** é a única que apresenta a combinação exata **{V, V, F}** para disparar o efeito **E1**.
