# 🐛 Python Debug Academy

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-green)
![Status](https://img.shields.io/badge/Status-Em%20Desenvolvimento-yellow)

> **Bem-vindo(a) à Python Debug Academy!** 🕵️‍♂️
> Aqui você não vai aprender a escrever código do zero. Você vai aprender a habilidade mais importante (e mais ignorada) de qualquer programador: **LER MENSAGENS DE ERRO E CONSERTAR CÓDIGO QUEBRADO.**

---

## 💼 A Sua Missão (O Cenário)

Parabéns, você acabou de ser **contratado(a)** como **Desenvolvedor(a) Júnior** na *DebugCorp*, uma empresa fictícia de tecnologia.

Na sua primeira semana, você recebeu uma pilha de **notebooks escritos por estagiários** que saíram da empresa às pressas. Os códigos estão cheios de bugs, variáveis erradas, sintaxe quebrada e DataFrames mal construídos.

**Sua missão é simples:** consertar todos os códigos para que eles rodem sem erros. Cada notebook resolvido é um "cliente salvo".

---

## 📚 O Que Você Vai Aprender

Ao longo desses desafios, você vai treinar a leitura e correção dos erros mais comuns do Python:

- ✅ `SyntaxError` - Erros de escrita (faltou aspas, vírgula, dois pontos...)
- ✅ `NameError` - Usar uma variável que ainda não existe.
- ✅ `TypeError` - Somar texto com número, por exemplo.
- ✅ `IndexError` - Tentar acessar um índice que não existe na lista.
- ✅ `AttributeError` - Chamar um método que não pertence àquele objeto.
- ✅ `IndentationError` - Esquecer de indentar um bloco de código.
- ✅ `KeyError` - Acessar uma chave/coluna que não existe em um Dicionário ou DataFrame.
- ✅ `ValueError` - Passar valores incompatíveis para uma função.

---

## 🗂️ Estrutura do Repositório

O projeto está dividido em **dois níveis de dificuldade**, cada um com um arquivo de **exercícios** e um de **gabarito**.

```text
📁 python-debug-academy/
│
├── 📄 README.md  (Você está aqui!)
│
├── 📁 01_basico/  (Nível 1 - Erros Básicos)
│   ├── Exercicios_Debug_Python.ipynb
│   └── Gabarito_Debug_Python.ipynb
│
└── 📁 02_pandas/  (Nível 2 - Dicionários e DataFrames)
    ├── Exercicios_Debug_Nivel_2.ipynb
    └── Gabarito_Debug_Nivel_2.ipynb
```

---

## 🚀 Como Começar (Passo a Passo)

### 1. Clone este repositório
Abra o seu terminal e digite:
```bash
git clone https://github.com/seu-usuario/python-debug-academy.git
cd python-debug-academy
```

### 2. Instale as bibliotecas necessárias
O projeto usa apenas `pandas` e `jupyter`. Você pode instalar via pip:
```bash
pip install pandas notebook
```
Ou, se preferir usar o arquivo `requirements.txt` (recomendado):
```bash
pip install -r requirements.txt
```

### 3. Inicie o Jupyter Notebook
```bash
jupyter notebook
```

### 4. Comece pelo Nível 1
Abra a pasta `01_basico` e comece pelo arquivo `Exercicios_Debug_Python.ipynb`.

---

## 📖 Como Resolver Cada Exercício

Cada exercício segue o mesmo padrão:

1.  **Leia o enunciado** na célula de texto (Markdown).
2.  **Rode a célula de código.** Você vai ver uma mensagem de erro (Traceback).
3.  **Leia o Traceback com atenção.** Ele diz exatamente:
    - **Qual o tipo do erro** (`SyntaxError`, `NameError`, etc.).
    - **Em qual linha** aconteceu.
    - **O que o Python esperava**.
4.  **Edite o código** para corrigir o erro.
5.  **Rode novamente.** Repita até a célula rodar sem erros.
6.  **Só depois de resolver**, olhe o arquivo `Gabarito_...` para comparar a sua solução com a proposta.

> 💡 **Dica de Ouro:** Não tenha medo de errar! O erro é a melhor ferramenta de aprendizado que existe.

---

## 🎯 Lista de Desafios

### 🟢 Nível 1: Erros Básicos (`01_basico/`)
Focado em problemas do dia a dia com variáveis, strings e listas.

| # | Erro a ser combatido | Descrição Curta |
|---|----------------------|-----------------|
| 1 | `SyntaxError` | Faltou aspas em um texto. |
| 2 | `NameError` | Uso de variável não definida. |
| 3 | `TypeError` | Soma de `str` com `int`. |
| 4 | `TypeError` | Concatenação de texto com número. |
| 5 | `Erro de Lógica` | Índice errado em uma lista. |
| 6 | `AttributeError` | Método inexistente para listas. |
| 7 | `IndentationError` | Falta de indentação em um `if`. |
| 8 | `NameError` | Variável fora do escopo. |
| 9 | `TypeError` | Múltiplos erros combinados. |
| 10 | `SyntaxError + Lógica` | Desafio final do nível. |

### 🟡 Nível 2: Dicionários e Pandas (`02_pandas/`)
Focado em estruturação de dados e DataFrames.

| # | Erro a ser combatido | Descrição Curta |
|---|----------------------|-----------------|
| 1 | `SyntaxError` | Faltou vírgula em um dicionário. |
| 2 | `KeyError` | Chave inexistente (case-sensitive). |
| 3 | `ValueError` | Listas de tamanhos diferentes em um DataFrame. |
| 4 | `AttributeError` | Erro no nome da função `DataFrame`. |
| 5 | `KeyError` | Coluna errada em um DataFrame. |
| 6 | `TypeError` | Média de uma coluna de texto. |
| 7 | `SyntaxError + KeyError` | Múltiplos erros em um dicionário. |
| 8 | `KeyError` | Uso correto de `.get()` como boa prática. |
| 9 | **Boss Fight** | Combinação de 3 erros diferentes. |
| 10 | `KeyError` | Erro ao ordenar um DataFrame. |

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.8+**
- **Jupyter Notebook**
- **Pandas** (para manipulação de DataFrames)

---

## 📄 Arquivo `requirements.txt`

Crie um arquivo chamado `requirements.txt` na raiz do projeto com o seguinte conteúdo:

```text
pandas
notebook
```

---

## 🤝 Como Contribuir

Este é um projeto educacional. Se você tem ideias de novos exercícios, encontrou um erro em algum gabarito ou quer melhorar as explicações:

1. Faça um **Fork** do projeto.
2. Crie uma **Branch** para sua modificação (`git checkout -b feature/novo-exercicio`).
3. Faça um **Commit** das suas alterações (`git commit -m 'Adiciona exercício sobre loops'`).
4. Faça um **Push** para a branch (`git push origin feature/novo-exercicio`).
5. Abra um **Pull Request**.

---

## 📜 Licença

Este projeto é de uso livre para fins educacionais. Sinta-se à vontade para usar em salas de aula, cursos de programação ou estudos pessoais.

---

## 💡 Frase Motivacional

> *"Todo programador experiente não é aquele que nunca erra, mas aquele que sabe ler a mensagem de erro, respirar fundo e corrigir. Você está no caminho certo."* 🚀

**Bons estudos, e que a caça aos bugs comece!** 🐛🔍
