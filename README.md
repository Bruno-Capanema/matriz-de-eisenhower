# Matriz de Eisenhower - Organizador de Atividades

Este programa organiza atividades com base na **Matriz de Eisenhower**, ajudando na priorização de tarefas de acordo com sua **importância** e **urgência**. Ele classifica as atividades em quatro categorias:

1. **Alta prioridade** (Muito importante e urgente)
2. **Planejamento** (Muito importante e não urgente)
3. **Delegável** (Menos importante e urgente)
4. **Eliminável** (Menos importante e não urgente)

## Funcionalidades

- Recebe atividades inseridas pelo usuário.
- Pergunta sobre a **importância** e **urgência** de cada atividade.
- Organiza as atividades automaticamente nas categorias da matriz.
- Exibe os resultados ao final, agrupando as tarefas por prioridade.

## Como usar o programa

### Requisitos

- **Python 3.7 ou superior**

### Passos para execução

1. **Clone ou baixe este repositório**.
2. Salve o arquivo como `matriz_eisenhower.py`.
3. Abra um terminal ou uma IDE e execute o programa:
   ```bash
   python matriz_eisenhower.py
   ```
4. Siga as instruções fornecidas pelo programa:
   - Insira as atividades uma por vez.
   - Responda às perguntas sobre importância e urgência (sim/não).
   - Digite **"acabou"** para finalizar a coleta de dados.
5. O programa irá exibir as atividades classificadas por prioridade.

## Estrutura do Programa

### Funções

1. **`coletar_atividades()`**:
   - Coleta as atividades do usuário.
   - Pergunta sobre a importância e urgência de cada atividade.
   - Classifica as atividades em uma das quatro categorias da matriz de Eisenhower.

2. **`exibir_resultados(categorias)`**:
   - Exibe as atividades organizadas por categoria.
   - Mostra uma lista clara e organizada com as tarefas inseridas.

### Classificação

As atividades são classificadas com base nas respostas:
- **Muito importante e urgente**: Alta prioridade.
- **Muito importante e não urgente**: Planejamento.
- **Menos importante e urgente**: Delegável.
- **Menos importante e não urgente**: Eliminável.

## Exemplo de Execução

```plaintext
Bem-vindo ao programa de priorização baseado na Matriz de Eisenhower!
Você será perguntado sobre as atividades que deseja organizar e suas prioridades.
Para encerrar a coleta, digite 'acabou'.

Digite a atividade (ou 'acabou' para finalizar): Finalizar relatório financeiro
Essa atividade é muito importante? (sim/nao): sim
Essa atividade é urgente? (sim/nao): sim

Digite a atividade (ou 'acabou' para finalizar): Estudar novo curso de Python
Essa atividade é muito importante? (sim/nao): sim
Essa atividade é urgente? (sim/nao): nao

Digite a atividade (ou 'acabou' para finalizar): Responder e-mails
Essa atividade é muito importante? (sim/nao): nao
Essa atividade é urgente? (sim/nao): sim

Digite a atividade (ou 'acabou' para finalizar): Ver redes sociais
Essa atividade é muito importante? (sim/nao): nao
Essa atividade é urgente? (sim/nao): nao

Digite a atividade (ou 'acabou' para finalizar): acabou

===== RESULTADOS =====

Alta prioridade (Muito importante e Urgente):
 - Finalizar relatório financeiro

Planejamento (Muito importante e Não urgente):
 - Estudar novo curso de Python

Delegável (Menos importante e Urgente):
 - Responder e-mails

Eliminável (Menos importante e Não urgente):
 - Ver redes sociais
```

## Personalização

- Você pode adicionar novas categorias ou modificar os critérios de classificação.
- Para alterar as perguntas ou respostas aceitas (“sim/não”), edite a função `coletar_atividades()`.

## Autor

Este programa foi desenvolvido como um exemplo prático de organização de tarefas baseado na matriz de Eisenhower. Se você tiver sugestões ou melhorias, fique à vontade para contribuir!

---

**Boa organização!**

