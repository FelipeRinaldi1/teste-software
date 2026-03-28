# Síntese Técnica: Smoke Testing (Teste de Fumaça)

O **Smoke Testing** é um conjunto de testes preliminares realizados em uma nova build de software para verificar se as funcionalidades mais críticas do sistema estão operando minimamente bem. O termo vem da eletrônica/encanamento: ao ligar um aparelho ou abrir a água, se "sair fumaça" ou vazar logo de cara, você nem continua os testes; você para e conserta o básico.

---

### 1. Descrição da Técnica

Também conhecido como "Build Verification Testing" (BVT), o foco aqui não é encontrar bugs profundos, mas sim atuar como um **porteiro**. Se o sistema nem abre ou se a função principal (ex: login) falha, a build é considerada instável e é devolvida para os desenvolvedores imediatamente, poupando o tempo da equipe de QA.

### 2. Características Principais

- **Superficial e Amplo:** Cobre o sistema de ponta a ponta, mas sem entrar em detalhes.
- **Execução Rápida:** Geralmente leva de 15 a 60 minutos (se manual) ou poucos minutos (se automatizado).
- **Frequência Alta:** Deve ser executado toda vez que uma nova versão do código é gerada.
- **Critério de Aceitação:** O resultado é binário — ou a build "passa" e vai para testes exaustivos, ou "falha" e é rejeitada.

---

### 3. Vantagens e Desvantagens

| Vantagens                                                                                                         | Desvantagens                                                                                                       |
| :---------------------------------------------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------- |
| **Economia de Tempo:** Evita que o QA gaste horas testando algo que está fundamentalmente quebrado.               | **Superficialidade:** Um Smoke Test com sucesso não garante que o sistema está livre de bugs graves.               |
| **Feedback Rápido:** Os desenvolvedores sabem em minutos se a integração da build deu certo.                      | **Falsa Sensação de Segurança:** Pode mascarar erros de integração que só aparecem em fluxos longos.               |
| **Fácil Automação:** Por serem testes simples e repetitivos, são os melhores candidatos para scripts automáticos. | **Manutenção:** Se a interface mudar, o Smoke Test precisa ser atualizado imediatamente para não travar a esteira. |

---

### 4. Exemplo de Aplicação

**Cenário:** Teste de fumaça em um **Aplicativo de E-mail**.

Um roteiro típico de Smoke Test validaria apenas o "caminho feliz" básico:

1.  **Instalação/Acesso:** O aplicativo abre sem fechar sozinho?
2.  **Autenticação:** É possível fazer login com uma conta válida?
3.  **Composição:** O botão "Escrever" abre a janela de mensagem?
4.  **Envio:** Ao clicar em enviar, a mensagem sai da caixa de saída?
5.  **Recebimento:** O app atualiza e mostra um novo e-mail na caixa de entrada?

_Se qualquer um desses 5 pontos falhar, o teste de fumaça é considerado "falho" e a build é rejeitada._

---

### 5. Conclusão

O Smoke Testing é a primeira linha de defesa no controle de qualidade. Ele garante que a equipe de testes foque sua energia em encontrar bugs complexos e de lógica, em vez de perder tempo com erros básicos de infraestrutura ou integração que deveriam ter sido resolvidos antes da entrega da build.
