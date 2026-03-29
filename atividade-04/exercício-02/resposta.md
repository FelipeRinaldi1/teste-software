# Conclusão: Análise de Grafo de Causa-Efeito (CEG)

A lógica do grafo apresentado é definida pela expressão booleana: **E1 = C1 ∨ (¬C2)**.

### Por que a Alternativa A é a correta?

A Tabela **A** mapeia corretamente os cenários onde o efeito **E1** ocorre (marcado com **X**):

- **R1 (C1=V, C2=F):** Verdadeiro ∨ (Não Falso) = **Verdadeiro**.
- **R2 (C1=V, C2=V):** Verdadeiro ∨ (Não Verdadeiro) = **Verdadeiro**.
- **R3 (C1=F, C2=F):** Falso ∨ (Não Falso) = **Verdadeiro**.

### Cenário de Falha

O efeito **E1** só **não ocorre** quando ambas as entradas do portão "OU" (V) são falsas. Isso só acontece se:

- **C1 = F**
- **C2 = V** (pois o símbolo `~` inverte para Falso).

Como a Alternativa **A** é a única que não atribui o efeito E1 a essa combinação específica (F, V), ela é a representação lógica fiel do grafo.
