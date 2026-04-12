# Sistema ATM

**Objeto de Teste:** Fluxo de Transição de Estados da ATM
**Técnica Utilizada:** Teste Baseado em Transição de Estados (Cenários)

---

## 1. Identificação dos Estados e Eventos

- **Estados:** Reading Card, Reading Pin, Choosing Transaction, Performing Transaction, Ejecting Card.
- **Eventos:** Card read successfully, Invalid Card, Getting valid pin, Invalid Pin, Transaction choosen, Cancel transaction, Finished transaction, Another transaction.

---

## 2. Cenários de Teste (Casos de Uso)

### CT-01: Fluxo Principal (Caminho Feliz - Saque/Consulta Única)

- **Objetivo:** Verificar o funcionamento básico do sistema do início ao fim sem erros.
- **Cenário:** O usuário insere o cartão, digita a senha correta, realiza uma operação e encerra.
- **Passos:**
  1. Iniciar no estado inicial (Ponto Preto).
  2. Evento: `Card read successfully`.
  3. Evento: `Getting valid pin`.
  4. Evento: `Transaction choosen`.
  5. Evento: `Finished transaction`.
- **Resultado Esperado:** Transição final para o estado **Ejecting Card** e encerramento no ponto final.

### CT-02: Retenção/Rejeição por Cartão Inválido

- **Objetivo:** Validar a segurança e o fluxo de erro logo na entrada do sistema.
- **Cenário:** O usuário insere um cartão danificado ou de outro banco não aceito.
- **Passos:**
  1. Iniciar no estado **Reading Card**.
  2. Evento: `Invalid Card`.
- **Resultado Esperado:** Transição direta para o estado **Ejecting Card**. O sistema não deve permitir o acesso ao teclado numérico para senha.

### CT-03: Bloqueio por Senha Incorreta

- **Objetivo:** Verificar se o sistema impede o acesso a transações com credenciais inválidas.
- **Cenário:** O usuário possui cartão válido, mas erra a senha (PIN).
- **Passos:**
  1. Iniciar no estado **Reading Card**.
  2. Evento: `Card read successfully`.
  3. Evento: `Invalid Pin`.
- **Resultado Esperado:** Transição do estado **Reading Pin** diretamente para **Ejecting Card**.

### CT-04: Ciclo de Múltiplas Transações

- **Objetivo:** Testar a persistência da sessão e o retorno ao menu principal.
- **Cenário:** O usuário realiza uma transação e decide realizar outra logo em seguida.
- **Passos:**
  1. Estar no estado **Performing Transaction**.
  2. Evento: `Another transaction`.
  3. Evento: `Transaction choosen`.
  4. Evento: `Finished transaction`.
- **Resultado Esperado:** O sistema deve retornar ao estado **Choosing Transaction** após o primeiro serviço e só ejetar o cartão após o evento de finalização.

### CT-05: Cancelamento Voluntário da Operação

- **Objetivo:** Validar o botão de interrupção pelo usuário antes de concluir a transação.
- **Cenário:** O usuário chega à tela de seleção de serviços, mas decide desistir da operação.
- **Passos:**
  1. Estar no estado **Choosing Transaction**.
  2. Evento: `Cancel transaction`.
- **Resultado Esperado:** Transição imediata para o estado **Ejecting Card**, garantindo que o cartão seja devolvido ao usuário antes do encerramento da sessão.
