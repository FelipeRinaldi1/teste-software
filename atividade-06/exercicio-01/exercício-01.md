# Sistema ATM

## 1. Estados da ATM

Com base no diagrama, os estados identificados são:

1. **Reading Card** (Lendo Cartão)
2. **Reading Pin** (Lendo Senha)
3. **Choosing Transaction** (Escolhendo Transação)
4. **Performing Transaction** (Realizando Transação)
5. **Ejecting Card** (Ejetando Cartão)

---

## 2. Eventos (Transições)

Os gatilhos que provocam a mudança de estado:

- **Card read successfully**: Sucesso na leitura do cartão.
- **Invalid Card**: Cartão inválido ou erro de leitura.
- **Getting valid pin**: Senha digitada corretamente.
- **Invalid Pin**: Senha incorreta.
- **Transaction choosen**: Seleção de um serviço (saque, saldo, etc.).
- **Cancel transaction**: Usuário desiste da operação.
- **Finished transaction**: Conclusão do serviço atual.
- **Another transaction**: Usuário opta por realizar nova operação.

---

## 3. Tabela de Transição de Estados

Organiza a relação entre Estado Atual, Evento e Próximo Estado.

| Estado Atual               | Evento                 | Próximo Estado         |
| :------------------------- | :--------------------- | :--------------------- |
| **Reading Card**           | Card read successfully | Reading Pin            |
| **Reading Card**           | Invalid Card           | Ejecting Card          |
| **Reading Pin**            | Getting valid pin      | Choosing Transaction   |
| **Reading Pin**            | Invalid Pin            | Ejecting Card          |
| **Choosing Transaction**   | Transaction choosen    | Performing Transaction |
| **Choosing Transaction**   | Cancel transaction     | Ejecting Card          |
| **Performing Transaction** | Finished transaction   | Ejecting Card          |
| **Performing Transaction** | Another transaction    | Choosing Transaction   |
| **Ejecting Card**          | (Finalização)          | Final (Círculo Alvo)   |

---

## 4. Tabela de Testes de Transições Válidas

Focada em cobrir todos os caminhos permitidos pelo diagrama.

| ID    | Estado Inicial         | Evento de Entrada      | Estado Esperado        |
| :---- | :--------------------- | :--------------------- | :--------------------- |
| TV-01 | Reading Card           | Card read successfully | Reading Pin            |
| TV-02 | Reading Pin            | Getting valid pin      | Choosing Transaction   |
| TV-03 | Choosing Transaction   | Transaction choosen    | Performing Transaction |
| TV-04 | Performing Transaction | Finished transaction   | Ejecting Card          |
| TV-05 | Reading Card           | Invalid Card           | Ejecting Card          |

---

## 5. Tabela de Testes de Sequência de Estados

Focada no fluxo lógico de ponta a ponta (Caminhos Felizes e Alternativos).

| ID    | Sequência de Estados Planejada                                                                 | Resultado Esperado           |
| :---- | :--------------------------------------------------------------------------------------------- | :--------------------------- |
| TS-01 | Reading Card -> Reading Pin -> Choosing Transaction -> Performing Transaction -> Ejecting Card | Sucesso total                |
| TS-02 | Reading Card -> Ejecting Card                                                                  | Cartão rejeitado de imediato |
| TS-03 | Reading Card -> Reading Pin -> Ejecting Card                                                   | Senha inválida               |
| TS-04 | Choosing Transaction -> Performing Transaction -> Choosing Transaction                         | Loop de "Nova Transação"     |

---

## 6. Tabela de Testes de Transições Inválidas

Testa o que o sistema **não** deve permitir.

| ID    | Estado Atual           | Evento Tentado         | Resultado Esperado       |
| :---- | :--------------------- | :--------------------- | :----------------------- |
| TI-01 | Reading Card           | Transaction choosen    | Ação bloqueada (Ignorar) |
| TI-02 | Reading Pin            | Finished transaction   | Ação bloqueada           |
| TI-03 | Performing Transaction | Getting valid pin      | Ação bloqueada/Erro      |
| TI-04 | Ejecting Card          | Card read successfully | Ação bloqueada           |

---

## 7. Casos de Teste Completos (5 Casos)

### CT-01: Fluxo Padrão de Saque com Sucesso

- **Pré-condição:** ATM em estado inicial (Reading Card).
- **Passos:**
  1. Inserir cartão válido.
  2. Digitar senha correta.
  3. Selecionar "Saque".
  4. Confirmar conclusão.
- **Resultado Esperado:** Transição sequencial até "Ejecting Card" e fim do processo.

### CT-02: Erro de Cartão

- **Pré-condição:** ATM em estado inicial.
- **Passos:**
  1. Inserir cartão danificado ou inválido.
- **Resultado Esperado:** Transição direta de "Reading Card" para "Ejecting Card".

### CT-03: Cancelamento pelo Usuário

- **Pré-condição:** Usuário no estado "Choosing Transaction".
- **Passos:**
  1. Pressionar o botão "Cancelar" na tela de seleção.
- **Resultado Esperado:** O sistema deve transitar para "Ejecting Card".

### CT-04: Múltiplas Transações

- **Pré-condição:** Usuário terminou uma transação (Performing Transaction).
- **Passos:**
  1. Após o término, selecionar a opção "Realizar outra operação".
- **Resultado Esperado:** O sistema deve retornar para "Choosing Transaction" em vez de ejetar o cartão.

### CT-05: Senha Incorreta

- **Pré-condição:** Cartão lido com sucesso (Reading Pin).
- **Passos:**
  1. Digitar uma senha inválida.
- **Resultado Esperado:** Transição de "Reading Pin" para "Ejecting Card".
