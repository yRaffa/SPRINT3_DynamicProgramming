# **🌐 FIAP x DASA CHALLENGE 2025 - SPRINT 3**

# 🐍 Dynamic Programing (2ESA)

## 👥 Integrantes

```
RM 557709 | Augusto Ferreira Rogel de Souza             (2ESA)
RM 554823 | Heitor Anderson Prestes de Oliveira Filho   (2ESA)
RM 556668 | Lucca Ribeiro Cardinale                     (2ESA)
RM 554445 | Mohamed Afif                                (2ESA)
RM 554736 | Rafael Federici de Oliveira                 (2ESPH)
```

## 📕 Sobre o Projeto

### 📦 Sistema de Gerenciamento de Estoque de Insumos Médicos

Este projeto tem como objetivo aplicar conceitos de Dynamic Programing no desenvolvimento de um sistema de gerenciamento de estoque de insumos médicos, implementado em [Python](https://www.python.org/doc/).
O sistema roda via terminal, utiliza estruturas de dados simples e aplica técnicas de eficiência computacional para análise de algoritmos de busca e ordenação.

## 📂 Estrutura do Projeto

``` bash
SPRINT3_DynamicProgramming/
│── data/                       # Conjunto de dados de entrada
│── services/                   # Serviços auxiliares (módulos de lógica)
│── utils/                      # Funções utilitárias
│── gerenciamento_estoque.py    # Programa principal
│── relatorio.ipynb             # Notebook com comparações de algoritmos
│── README.md                   # Documentação do projeto
```

## ⚙️ Funcionalidades Principais

### 🔸 Visualizar Estoque

Exibe todos os insumos em formato de tabela (via Pandas).

### 🔸 Adicionar Novo Insumo

Permite o cadastro de um novo insumo no estoque, solicitando os seguintes dados:
- Nome do Insumo
- Quantidade em Estoque
- Estoque Ideal
- Custo Unitário

### 🔸 Modificar Estoque

Permite modificar (Excluir e Atualizar) dados ja cadastrados no estoque.

### 🔸 Adicionar / Retirar Quantidade

Permite ajustar quantidade de cada insumo, conforme movimentações no estoque.

### 🔸 Reabastecimento Automático

Automaticamente reabastece os insumos que estão abaixo do estoque ideal, gerando um relatório com o custo total.

### 🔸 Registro de Consumo Automático

Toda alteração foita no estoque é salva em estruturas de **Pilha** e **Fila**, garantindo rastreabilidade.

## 🎲 Estrutura dos Dados

Os dados dos insumos são armazenados no dicionário ``` insumos ```, onde cada chave representa um campo (coluna), e os valores são listas (linhas).

``` python
insumos = {
    'ID' : [0, 1, 2, 3, 4, 5],
    'Nome_Insumo' : ['Adrenalina', 'Dipirona', 'Gaze Esteril', 'Luvas Cirurgicas' , 'Mascaras N95', 'Seringas'],
    'Estoque' : [500, 1000, 3000, 2000, 300, 4000],
    'Estoque_Ideal' : [1000, 3000, 5000, 5000, 1000, 5000],
    'Custo_Unitario' : [5.00, 1.30, 0.40, 0.80, 4.30, 0.40]
}
```

O campo ``` 'ID' ``` é usado como chave primária para buscas e operações.

## ▶️ Como Executar

#### **Clone o repositório:**

``` bash
git clone <repo_url>
cd SPRINT3_DynamicProgramming
```

#### **Instale as dependências:**

``` bash
pip install -r requirements.txt
```

#### **Execute o sistema:**

``` bash
python gerenciamento_estoque.py
```

Ao executar o código em um terminal Python:
- Um menu será exibido com as opções principais.
- Digite o número da operação desejada.
- Siga as instruções no terminal para preencher ou visualizar os dados.

#### **Para visualizar relatório:**

``` bash
jupyter notebook relatorio.ipynb
```

## ⚠️ Observação

O código utiliza validação básica de entrada, mas não possui persistência de dados. Ao encerrar o programa, os dados são perdidos.
