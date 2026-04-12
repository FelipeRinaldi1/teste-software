# Fluxo do Passageiro

**Objeto de Teste:** Ciclo de Vida do Passageiro Aéreo
**Técnica Utilizada:** Teste Baseado em Cenários (Transição de Estados)

---

## 1. Identificação dos Estados e Eventos

- **Estados:** Passenger wishing to travel, Passenger holding reservation, Passenger Ready to travel, Passenger with boarding card, Completed passenger.
- **Eventos:** reservation, request check-in, reschedule, check-in, complete flight, urge to fly.

---

## 2. Cenários de Teste (Casos de Uso)

### CT-01: Fluxo de Viagem Padrão (Caminho Feliz)

- **Objetivo:** Validar o sucesso do processo desde a intenção de viajar até a conclusão do voo.
- **Cenário:** O passageiro faz a reserva, solicita o check-in, obtém o cartão e voa.
- **Passos:**
  1. Iniciar em **Wishing to travel**.
  2. Realizar ação `reservation`.
  3. Realizar ação `request check-in`.
  4. Realizar ação `check-in`.
  5. Realizar ação `complete flight`.
- **Resultado Esperado:** O passageiro deve terminar o fluxo no estado **Completed passenger**.

### CT-02: Reagendamento de Voo (Fluxo de Retorno)

- **Objetivo:** Verificar se o sistema permite que um passageiro pronto para viajar retorne ao estado de reserva.
- **Cenário:** O passageiro decide mudar a data do voo após ter solicitado o check-in.
- **Passos:**
  1. Estar no estado **Passenger Ready to travel**.
  2. Realizar ação `reschedule`.
- **Resultado Esperado:** O estado deve retornar para **Passenger holding reservation**, invalidando a prontidão atual.

### CT-03: Ciclo de Fidelidade (Nova Viagem)

- **Objetivo:** Validar o reinício do ciclo de vida após a conclusão de uma jornada.
- **Cenário:** Um passageiro que já concluiu um voo sente a necessidade de viajar novamente.
- **Passos:**
  1. Estar no estado **Completed passenger**.
  2. Acionar o evento `urge to fly`.
- **Resultado Esperado:** O sistema deve colocar o passageiro novamente no estado inicial **Passenger wishing to travel**.

### CT-04: Processamento de Check-in em Duas Etapas

- **Objetivo:** Garantir que o cartão de embarque só seja emitido após a prontidão do passageiro.
- **Cenário:** O passageiro transita da reserva para a emissão do cartão passando pela triagem inicial.
- **Passos:**
  1. Estar no estado **Passenger holding reservation**.
  2. Executar `request check-in`.
  3. No estado **Ready to travel**, executar `check-in`.
- **Resultado Esperado:** O passageiro deve evoluir corretamente para o estado **Passenger with boarding card**.

### CT-05: Tentativa de Salto de Etapa (Transição Inválida)

- **Objetivo:** Validar a integridade das regras de negócio (negativo).
- **Cenário:** Tentar realizar o voo logo após a reserva, sem cartão de embarque.
- **Passos:**
  1. Estar no estado **Passenger holding reservation**.
  2. Tentar executar a ação `complete flight`.
- **Resultado Esperado:** O sistema deve bloquear a transição. O passageiro deve permanecer em seu estado atual até possuir um cartão de embarque válido.
