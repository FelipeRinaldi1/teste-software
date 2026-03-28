# Síntese Técnica: Monkey Testing vs. Gorilla Testing

AS técnicas possuem focos opostos: enquanto o **Monkey Testing** busca o caos e a aleatoriedade em todo o sistema, o **Gorilla Testing** foca na exaustão de um único módulo específico.

---

## 1. Monkey Testing

O **Monkey Testing** consiste em fornecer entradas aleatórias ao sistema para observar se ele trava ou apresenta comportamento anormal.

### Características do Monkey Testing

- **Dumb Monkeys:** O testador não conhece o sistema. Apenas envia inputs aleatórios.
- **Smart Monkeys:** Têm um conhecimento básico do fluxo e tentam quebrar o sistema com intenção, mas ainda de forma desordenada.
- **Foco em Estabilidade:** O objetivo não é validar requisitos, mas sim encontrar momentos em que o sistema crasha e vazamentos de memória.

### Vantagens e Desvantagens

| Vantagens                                                                 | Desvantagens                                                 |
| :------------------------------------------------------------------------ | :----------------------------------------------------------- |
| **Simplicidade:** Não exige planejamento ou casos de teste.               | **Caótico:** Muito difícil de reproduzir o erro encontrado.  |
| **Eficaz para UI:** Ótimo para testar a resistência de interfaces mobile. | **Superficial:** Não valida a lógica de negócio do software. |

**Exemplo:** Abrir um aplicativo de delivery e começar a clicar freneticamente em todos os ícones, botões de "voltar" e campos de texto simultaneamente para ver se o app encerra sozinho.

---

## 2. Gorilla Testing

O **Gorilla Testing** é uma técnica de teste de unidade/módulo exaustiva. Aqui, um único componente do sistema é testado repetidamente com todas as variações possíveis de dados até que o testador tenha certeza de que ele é "inquebrável".

### Características do Gorilla Testing

- **Foco Cirúrgico:** Diferente do Monkey, o Gorilla não olha para o sistema todo, apenas para uma peça.
- **Manual e Repetitivo:** Geralmente feito por testadores humanos que "martelam" uma funcionalidade específica.
- **Profundidade:** Busca encontrar bugs de lógica profunda que testes superficiais ignoram.

### Vantagens e Desvantagens

| Vantagens                                                                          | Desvantagens                                                                |
| :--------------------------------------------------------------------------------- | :-------------------------------------------------------------------------- |
| **Alta Confiabilidade:** Garante que módulos críticos sejam extremamente robustos. | **Custo de Tempo:** Exige muito tempo para testar apenas uma pequena parte. |
| **Precisão:** Identifica exatamente onde a lógica do módulo falha.                 | **Visão Limitada:** Pode ignorar erros de integração entre os módulos.      |

---

### 3. Diferença Rápida para sua Apresentação

- **Monkey Testing:** "Vou clicar em tudo aleatoriamente para ver se o sistema cai." foca em Amplitude
- **Gorilla Testing:** "Vou testar este botão de login de todas as formas possíveis até ele quebrar." Foca em Profundidade

---

### 4. Conclusão

Ambas as técnicas são essenciais para garantir a robustez. O Monkey Testing é excelente para fases iniciais de QA em interfaces, enquanto o Gorilla Testing é indispensável para componentes críticos (como checkout, pagamentos ou segurança) antes de um lançamento importante.
