# Fluxo do Passageiro

## 1. Estados Identificados

1. **Passenger wishing to travel** (Desejando viajar)
2. **Passenger holding reservation** (Com reserva efetuada)
3. **Passenger Ready to travel** (Pronto para viajar / Aguardando check-in)
4. **Passenger with boarding card** (Com cartão de embarque)
5. **Completed passenger** (Viagem concluída)

---

## 2. Eventos (Transições)

Os gatilhos que alteram o estado do passageiro:

- **reservation**: Ato de realizar a reserva do voo.
- **request check-in**: Solicitação ou abertura do processo de check-in.
- **reschedule**: Reagendamento da viagem (retorna à reserva).
- **check-in**: Finalização do check-in e emissão do cartão de embarque.
- **complete flight**: Realização e conclusão do voo.
- **urge to fly**: Desejo de realizar uma nova viagem.

---

## 3. Tabela de Transição de Estados

Mapeamento lógico de como o passageiro se move pelo sistema.

| Estado Atual            | Evento           | Próximo Estado      |
| :---------------------- | :--------------- | :------------------ |
| **Wishing to travel**   | reservation      | Holding reservation |
| **Holding reservation** | request check-in | Ready to travel     |
| **Ready to travel**     | check-in         | With boarding card  |
| **Ready to travel**     | reschedule       | Holding reservation |
| **With boarding card**  | complete flight  | Completed passenger |
| **Completed passenger** | urge to fly      | Wishing to travel   |

---

## 4. Tabela de Testes de Transições Válidas

Verifica se as funcionalidades básicas estão operando conforme o desenho.

| ID    | Estado Inicial     | Evento de Entrada | Estado Esperado     |
| :---- | :----------------- | :---------------- | :------------------ |
| TV-01 | Wishing to travel  | reservation       | Holding reservation |
| TV-02 | Ready to travel    | reschedule        | Holding reservation |
| TV-03 | Ready to travel    | check-in          | With boarding card  |
| TV-04 | With boarding card | complete flight   | Completed passenger |

---

## 5. Tabela de Testes de Sequência de Estados (Caminhos)

Testa a continuidade do processo.

| ID    | Sequência de Estados Planejada                        | Resultado Esperado                    |
| :---- | :---------------------------------------------------- | :------------------------------------ |
| TS-01 | Wishing -> Holding -> Ready -> With Card -> Completed | Ciclo de vida completo com sucesso    |
| TS-02 | Ready -> Holding -> Ready                             | Teste de reprocessamento (Reschedule) |
| TS-03 | Completed -> Wishing                                  | Início de um novo ciclo (Fidelidade)  |

---

## 6. Tabela de Testes de Transições Inválidas

Testa tentativas de pular etapas ou ações fora de contexto.

| ID    | Estado Atual        | Evento Tentado   | Resultado Esperado                     |
| :---- | :------------------ | :--------------- | :------------------------------------- |
| TI-01 | Wishing to travel   | check-in         | Bloqueado (Sem reserva)                |
| TI-02 | Holding reservation | complete flight  | Bloqueado (Sem check-in/embarque)      |
| TI-03 | With boarding card  | reservation      | Bloqueado (Já possui reserva e cartão) |
| TI-04 | Completed passenger | request check-in | Bloqueado (Voo já encerrado)           |

---

## 7. Casos de Teste Completos (5 Casos)

### CT-01: Ciclo de Viagem Perfeito

- **Pré-condição:** Usuário no estado inicial "Wishing to travel".
- **Passos:**
  1. Realizar reserva.
  2. Solicitar check-in.
  3. Finalizar check-in.
  4. Concluir o voo.
- **Resultado Esperado:** O passageiro deve chegar ao estado "Completed passenger" sem erros.

### CT-02: Fluxo de Reagendamento (Reschedule)

- \*\*Pré-
