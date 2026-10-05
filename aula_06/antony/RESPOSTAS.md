# Atividade de Fixação Extraclasse - Aula 06
**Disciplina:** Matemática Computacional Aplicada - UniFG 2026.2

## Parte 1: Exercícios Teóricos de Teoria dos Conjuntos

### 1. Operações de Conjuntos
Dados $U = \{1, 2, 3, 4, 5, 6, 7, 8, 9, 10\}$, $A = \{2, 4, 6, 8, 10\}$ e $B = \{2, 3, 5, 7\}$:
- **(a)** $A \cup B = \{2, 3, 4, 5, 6, 7, 8, 10\}$
- **(b)** $A \cap B = \{2\}$
- **(c)** $A \setminus B = \{4, 6, 8, 10\}$
- **(d)** $(A \cup B)' = \{1, 9\}$

### 2. Simplificação da Expressão
$$(A \cap B) \cup (A \cap B') = A \cap (B \cup B') = A \cap U = A$$
**Resultado Simplificado:** $A$

### 3. Colisões de Hash e Complexidade no CPython
- **Tratamento de Colisões:** O CPython utiliza uma tabela hash com endereçamento aberto e sondagem pseudo-aleatória ($i = (5 \times i + 1 + \text{perturb}) \bmod \text{tamanho}$) na estrutura `set` para encontrar o próximo slot livre na memória.
- **Complexidade $O(1)$ Médio:** O CPython mantém o fator de carga (*load factor*) sempre abaixo de $66\%$. Se ultrapassado, a tabela redimensiona automaticamente, mantendo as colisões raras e a localização do elemento em tempo constante $O(1)$ no caso médio.

---

## Parte 2: Desafio Prático em Python

```python
from itertools import product

def detectar_rotas_circulares(linhas: dict[str, list[str]]) -> set[tuple[str, str]]:
    # Gera todas as conexões direcionadas (origem -> destino)
    arestas = {par for origem, destinos in linhas.items() for par in product({origem}, destinos)}
    
    # Gera as conexões invertidas (destino -> origem)
    arestas_invertidas = {(v, u) for (u, v) in arestas}
    
    # Interseção encontra conexões bidirecionais
    bidirecionais = arestas & arestas_invertidas
    
    # Normaliza em ordem alfabética para evitar duplicatas equivalentes
    return {tuple(sorted((u, v))) for u, v in bidirecionais if u != v}
