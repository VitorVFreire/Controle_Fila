# Modelo M/M/1 - Teoria das Filas

Este projeto implementa funções baseadas na Teoria das Filas para um sistema M/M/1, utilizando parâmetros como taxa de chegada e taxa de atendimento.

## 📌 Descrição

O código calcula métricas de desempenho do sistema de filas, como:

- Probabilidade do sistema estar vazio `P(0)`
- Probabilidade de haver `n` clientes no sistema `P(n)`
- Taxa de utilização do servidor `ρ`
- Probabilidade de haver mais que `n` clientes no sistema
- Número médio de clientes no sistema
- Tempo médio de permanência e espera na fila

## 📊 Fórmulas Utilizadas

- **Taxa de Utilização:**  
  \[
  ρ = \frac{λ}{μ}
  \]

- **Probabilidade do sistema estar vazio:**  
  \[
  P(0) = 1 - ρ
  \]

- **Probabilidade de haver n clientes:**  
  \[
  P(n) = P(0) \cdot ρ^n
  \]

- **Probabilidade de mais que `n` clientes:**  
  \[
  P(N > n) = 1 - ρ^{n+1}
  \]

- **Número médio de clientes no sistema:**  
  \[
  L = \frac{λ}{μ - λ}
  \]

- **Número médio na fila:**  
  \[
  L_q = \frac{λ^2}{μ(μ - λ)}
  \]

- **Tempo médio no sistema:**  
  \[
  W = \frac{1}{μ - λ}
  \]

- **Tempo médio na fila:**  
  \[
  W_q = \frac{λ}{μ(μ - λ)}
  \]

## ▶️ Execução

Atualmente, os parâmetros são definidos diretamente no código (veja `if __name__ == "__main__"`), mas há preparação para entrada por linha de comando com `argparse`.

Exemplo de execução com os valores definidos:

```bash
python main.py
