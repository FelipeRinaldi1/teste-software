# Documentação de Teste de Software: Internet Banking

**Objeto de Teste:** Sistema de Transições de Estados - Internet Banking
**Técnica Utilizada:** Teste Baseado em Cenários (Caminhos de Execução)

---

## 1. Identificação de Estados e Fluxos

Este sistema possui um estado central de autenticação (**Enter LOGIN Credentials**) que ramifica para quatro fluxos principais:

- **Consulta de Saldo** (Balance)
- **Transações Financeiras** (Transactions)
- **Serviços de Cheque** (Cheque)
- **Serviços de E-Banking** (Smart Card)

---

## 2. Cenários de Teste (Casos de Uso)

### CT-01: Fluxo de Transação Financeira com Retorno

- **Objetivo:** Validar a execução de uma transferência e o retorno automático para verificação de saldo.
- **Cenário:** Usuário loga, realiza um pagamento e volta para conferir o saldo atualizado.
- **Passos:**
  1. No estado **Enter LOGIN Credentials**, disparar `Credentials Verified`.
  2. No estado **Check Balance**, disparar `Not Check Balance`.
  3. No estado **Initiate Transaction**, disparar `Transaction Initiated`.
  4. Seguir por **Select Account** -> **Enter Amount**.
  5. Disparar `Transaction Executed`.
- **Resultado Esperado:** O sistema deve retornar ao estado **Check Balance**.

### CT-02: Recuperação de Erro e Bloqueio por OTP

- **Objetivo:** Validar a resiliência do login e o encerramento de sessão por falha de segurança.
- **Cenário:** Usuário erra a senha, tenta novamente, mas falha no segundo fator de autenticação (OTP).
- **Passos:**
  1. No login, disparar `Incorrect Credentials`.
  2. No estado **Display Error "Retry"**, disparar `Error Message Sent`.
  3. Retornar ao login e disparar `Incorrect Credentials` novamente.
  4. No erro, disparar `Incorret OTP`.
- **Resultado Esperado:** O sistema deve transitar para o estado Final (Sessão Encerrada).

### CT-03: Fluxo de Depósito/Processamento de Cheque

- **Objetivo:** Validar a cadeia de aprovação e atualização de conta via cheque.
- **Cenário:** Usuário acessa o serviço de cheques e completa o fluxo de depósito.
- **Passos:**
  1. Logar no sistema.
  2. Acessar o estado **Get Cheque Details** (através de `Credentials Verified`).
  3. Transitar: **Approve Cheque** (`Cheque Accessed`) -> **Accept Cheque** (`Details Verified`).
  4. Avançar para **Update Account Details**.
- **Resultado Esperado:** O sistema deve atualizar os detalhes da conta e encerrar o processo no ponto final.

### CT-04: Solicitação de Smart Card (E-Banking Services)

- **Objetivo:** Validar o acesso a serviços administrativos e atualização cadastral.
- **Cenário:** Usuário navega pelos serviços de E-Banking para solicitar um novo cartão inteligente.
- **Passos:**
  1. Logar e acessar **E-Banking Services**.
  2. Disparar `Get Card` para entrar em **Get Smart Card**.
  3. Disparar `Process Initiated` para **Enter Details**.
  4. Disparar `Details Accepted` para **Update Account Details**.
- **Resultado Esperado:** O sistema deve processar a solicitação e transitar para a atualização de conta e finalização.

### CT-05: Consulta Rápida de Saldo (Caminho Curto)

- **Objetivo:** Verificar a funcionalidade mais simples e frequente do sistema.
- **Cenário:** Usuário loga apenas para visualizar o saldo e sai.
- **Passos:**
  1. Logar com sucesso.
  2. No estado **Check Balance**, disparar `User Account Details Accessed`.
  3. No estado **Display Balance**, disparar `Balance Entered`.
- **Resultado Esperado:** O sistema deve exibir o saldo e transitar diretamente para o encerramento da sessão (ponto final superior direito).
