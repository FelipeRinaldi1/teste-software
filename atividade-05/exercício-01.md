# Síntese Técnica: Error Guessing (Adivinhação de Erros)

O **Error Guessing** é uma técnica de teste baseada na experiência, onde o testador utiliza sua intuição, conhecimento do sistema e histórico de falhas comuns para antecipar onde o software pode quebrar. Diferente de métodos matemáticos, ela em cenários que a lógica formal costuma ignorar.

---

### 1. Descrição da Técnica

A técnica consiste em prever erros que podem ocorrer em condições específicas. O testador não segue um roteiro rígido, mas sim uma "mentalidade de destruição", tentando imaginar situações onde o desenvolvedor possa ter esquecido de tratar uma exceção.

É amplamente utilizada para identificar casos de borda e comportamentos inesperados que técnicas como Partição de Equivalência nem sempre alcançam.

### 2. Características Principais

- **Empírica:** Totalmente dependente do repertório do profissional.
- **Complementar:** Funciona melhor quando usada junto com técnicas estruturadas.
- **Criativa:** Exige que o testador pense "fora da caixa" e simule usos atípicos.
- **Uso de Checklists:** É comum apoiar-se em listas de erros históricos (ex: campos vazios, estouro de caracteres, perda de conexão).

---

### 3. Vantagens e Desvantagens

| Vantagens                                                                        | Desvantagens                                                                 |
| :------------------------------------------------------------------------------- | :--------------------------------------------------------------------------- |
| **Agilidade:** Aplicação rápida sem necessidade de documentação exaustiva.       | **Subjetividade:** O resultado varia muito dependendo de quem testa.         |
| **Eficácia:** Encontra bugs complexos que passam despercebidos em testes padrão. | **Baixa Repetibilidade:** Difícil de padronizar ou automatizar com precisão. |
| **Baixo Custo:** Não exige ferramentas caras ou modelagem prévia.                | **Sem Métrica de Cobertura:** Não há como medir 100% de cobertura de código. |

---

### 4. Exemplo de Aplicação

**Cenário:** Teste de um formulário de transferência bancária.

Enquanto o teste formal validaria se o saldo é suficiente, o **Error Guessing** testaria:

1.  **Valor Negativo:** Tentar transferir `-R$ 50,00` para ver se o sistema "soma" o valor na conta de origem.
2.  **Spam de Cliques:** Clicar repetidamente no botão "Enviar" para tentar gerar duplicidade na transação.
3.  **Caracteres Especiais:** Inserir códigos ou emojis no campo de "Descrição".
4.  **Queda de Rede:** Cortar a internet exatamente no milissegundo em que a transação é processada.

---

### 5. Conclusão

O Error Guessing é essencial para garantir a resiliência do software no mundo real. Ele traz o fator humano e a imprevisibilidade para o processo de QA, sendo uma ferramenta indispensável para quem busca um produto final realmente robusto.
