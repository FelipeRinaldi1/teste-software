# Teste de Software

## Por que Docker?

O Docker garante que o ambiente de execução seja idêntico ao utilizado no desenvolvimento e padroniza a execução dos testes.

## Como Executar

### 1. Iniciar o container em segundo plano

```bash
docker build -t teste-software .
docker run -d --name lab-teste teste-software
```

### 2. Rodar um exercício específico

```bash
docker exec lab-teste python atividade-09/exercicio-01/item-a/compute.py
```

### 3. Rodar todos os testes de uma pasta

```bash
docker exec lab-teste pytest atividade-09/
```

### 4. Gerar Fluxograma

```bash
docker exec lab-teste python gerar_grafo.py atividade-08/exercicio-01/item-a/compute.py
```

Copie o resultado e cole em: https://adrai.github.io/flowchart.js/

### 5. Parar o container

```bash
docker stop lab-teste
docker rm lab-teste
```
