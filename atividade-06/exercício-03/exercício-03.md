# Internet Banking

## 1. Estados Identificados

1. **Enter LOGIN Credentials**
2. **Display Error "Retry"**
3. **Check Balance**
4. **Display Balance**
5. **Initiate Transaction**
6. **Select Account**
7. **Enter Amount**
8. **Get Cheque Details**
9. **Approve Cheque**
10. **Accept Cheque**
11. **E-Banking Services**
12. **Get Smart Card**
13. **Enter Details**
14. **Update Account Details**

---

## 2. Eventos (Transições Principais)

- **Credentials Verified**: Login bem-sucedido.
- **Incorrect Credentials**: Erro de login.
- **Error Message Sent**: Retorno para nova tentativa de login.
- **Incorrect OTP**: Erro no código de segurança (encerra sessão).
- **User Account Details Accessed**: Solicitação de visualização de saldo.
- **Transaction Initiated**: Início de transferência/pagamento.
- **Account - Current or Savings**: Seleção do tipo de conta.
- **Transaction Executed**: Finalização da transação.
- **Cheque Accessed**: Início do fluxo de cheque.
- **Details Verified / Accepted**: Validação de informações.
- **Explore**: Acesso a serviços adicionais.

---

## 3. Tabela de Transição de Estados

| Estado Atual                | Evento                        | Próximo Estado                                 |
| :-------------------------- | :---------------------------- | :--------------------------------------------- |
| **Enter LOGIN Credentials** | Credentials Verified          | Check Balance / Get Cheque Details / E-Banking |
| **Enter LOGIN Credentials** | Incorrect Credentials         | Display Error "Retry"                          |
| **Display Error "Retry"**   | Error Message Sent            | Enter LOGIN Credentials                        |
| **Display Error "Retry"**   | Incorrect OTP                 | Final (Sessão Encerrada)                       |
| **Check Balance**           | User Account Details Accessed | Display Balance                                |
| **Initiate Transaction**    | Transaction Initiated         | Select Account                                 |
| **Select Account**          | Account - Current or Savings  | Enter Amount                                   |
| **Enter Amount**            | Transaction Executed          | Check Balance                                  |
| **Get Cheque Details**      | Cheque Accessed               | Approve Cheque                                 |
| **Approve Cheque**          | Details Verified              | Accept Cheque                                  |
| **Accept Cheque**           | (Automático)                  | Update Account Details                         |
| **E-Banking Services**      | Get Card                      | Get Smart Card                                 |
| **Enter Details**           | Details Accepted              | Update Account Details                         |

---

## 4. Tabela de Testes de Transições Válidas

| ID    | Estado Inicial          | Evento de Entrada             | Estado Esperado                    |
| :---- | :---------------------- | :---------------------------- | :--------------------------------- |
| TV-01 | Enter LOGIN Credentials | Credentials Verified          | Check Balance (ou outros serviços) |
| TV-02 | Check Balance           | User Account Details Accessed | Display Balance                    |
| TV-03 | Enter Amount            | Transaction Executed          | Check Balance                      |
| TV-04 | Get Smart Card          | Process Initiated             | Enter Details                      |
| TV-05 | Approve Cheque          | Details Verified              | Accept Cheque                      |

---

## 5. Tabela de Testes de Sequência de Estados

| ID    | Sequência de Estados Planejada                                              | Resultado Esperado                      |
| :---- | :-------------------------------------------------------------------------- | :-------------------------------------- |
| TS-01 | LOGIN -> Check Balance -> Display Balance                                   | Consulta de saldo simples               |
| TS-02 | LOGIN -> Initiate Trans. -> Select Account -> Enter Amount -> Check Balance | Fluxo de transferência completa         |
| TS-03 | LOGIN -> Get Cheque Details -> Approve -> Accept -> Update Account          | Fluxo de depósito/compensação de cheque |
| TS-04 | Enter LOGIN -> Display Error -> Enter LOGIN                                 | Recuperação de erro de senha            |

---

## 6. Tabela de Testes de Transições Inválidas

| ID    | Estado Atual            | Evento Tentado        | Resultado Esperado                             |
| :---- | :---------------------- | :-------------------- | :--------------------------------------------- |
| TI-01 | Enter LOGIN Credentials | Transaction Initiated | Bloqueado (Requer login prévio)                |
| TI-02 | Display Balance         | Transaction Executed  | Ação Inválida (Estado de apenas leitura)       |
| TI-03 | Select Account          | Error Message Sent    | Ação Inválida (Evento exclusivo do Login)      |
| TI-04 | Update Account Details  | Incorrect Credentials | Fluxo impossível (Estado de pós-processamento) |

---

## 7. Casos de Teste Completos (5 Casos)

### CT-01: Login e Consulta de Saldo

- **Passos:** Inserir credenciais válidas -> Clicar em "Check Balance" -> Acessar detalhes da conta.
- **Resultado Esperado:** Transição final para "Display Balance".

### CT-02: Execução de Transferência Bancária

- **Passos:** Login -> Initiate Transaction -> Selecionar Conta Corrente -> Inserir Valor -> Confirmar.
- **Resultado Esperado:** O sistema deve executar a transição "Transaction Executed" e retornar o usuário para "Check Balance" para conferência.

### CT-03: Falha Crítica de Segurança (OTP)

- **Passos:** Inserir senha incorreta -> No estado de erro, inserir um OTP (One Time Password) inválido.
- **Resultado Esperado:** O sistema deve transitar para o estado Final (encerrar a aplicação).

### CT-04: Fluxo de Solicitação de Smart Card

- **Passos:** Login -> E-Banking Services -> Get Card -> Inserir Detalhes do Pedido -> Aceitar.
- **Resultado Esperado:** Transição para "Update Account Details" e posterior finalização.

### CT-05: Processamento de Cheque

- **Passos:** Login -> Get Cheque Details -> Preencher dados -> Aprovar Cheque.
- **Resultado Esperado:** Transição sequencial: Approve Cheque -> Accept Cheque -> Update Account Details -> Fim.
