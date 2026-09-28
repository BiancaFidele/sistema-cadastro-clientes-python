# 🗂️ Sistema de Cadastro de Clientes

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Concluído-brightgreen)
![Licença](https://img.shields.io/badge/Licença-MIT-lightgrey)

Sistema de cadastro de clientes via terminal, desenvolvido em Python com Programação Orientada a Objetos (POO), validação de duplicidade e busca por nome.

> Projeto desenvolvido como exercício prático do curso **Programação Python com Machine Learning, NLP, Visão Computacional, Automações e Projetos Práticos com Streamlit**, como parte da consolidação dos fundamentos de Python antes de avançar para tópicos de IA.

---

## 📑 Sumário

- [Sobre o projeto](#-sobre-o-projeto)
- [Problema](#-problema)
- [Objetivo](#-objetivo)
- [Demonstração](#-demonstração)
- [Funcionalidades](#-funcionalidades)
- [Tecnologias utilizadas](#-tecnologias-utilizadas)
- [Conhecimentos aplicados](#-conhecimentos-aplicados)
- [Como funciona](#-como-funciona)
- [Como executar](#-como-executar)
- [Decisões de design](#-decisões-de-design)
- [Principais aprendizados](#-principais-aprendizados)
- [Possíveis melhorias](#-possíveis-melhorias)

---

## 📖 Sobre o projeto

Este projeto simula um sistema simples de cadastro de clientes para uma pequena empresa de serviços, rodando inteiramente no terminal. Ele foi construído como o desafio de maior complexidade de uma sequência de três exercícios progressivos (baixo, médio e alto), aplicando de forma combinada os fundamentos de Python estudados no curso.

## ❓ Problema

Pequenas empresas frequentemente precisam de uma forma simples de registrar clientes, evitando cadastros duplicados e permitindo consultar rapidamente quem já está na base, sem depender de planilhas ou sistemas complexos.

## 🎯 Objetivo

Criar um sistema de terminal que permita cadastrar, listar e buscar clientes, impedindo duplicidade de cadastro e organizando as informações de forma clara para quem opera o sistema.

## 🎬 Demonstração

<img width="1920" height="1080" alt="demo" src="https://github.com/user-attachments/assets/64f98fa5-b455-426c-8b21-123cb8e7d593" />

## ⚙️ Funcionalidades

- ✅ Cadastrar novo cliente (nome, idade, telefone, CPF, CEP, cidade, endereço, estado)
- ✅ Impedir cadastro duplicado, validando pelo CPF

- ✅ Listar todos os clientes cadastrados
- ✅ Buscar um cliente específico pelo nome (sem diferenciar maiúsculas/minúsculas)
- ✅ Menu interativo em loop, until o usuário optar por sair

## 🛠️ Tecnologias utilizadas

- **Python 3.12** (biblioteca padrão, sem dependências externas)

## 🧠 Conhecimentos aplicados

- Programação Orientada a Objetos (classes, `__init__`, atributos, métodos)
- Listas para armazenar múltiplos objetos
- Funções com parâmetros e `return`
- Estruturas condicionais (`if`/`elif`/`else`)
- Laços de repetição (`for`, `while`)
- Formatação de strings com f-strings
- Validação de dados de entrada

## 🔄 Como funciona

```
              ┌────────────────────┐
              │   Menu principal   │
              └─────────┬──────────┘
                         │
       ┌─────────┬───────┴───────┬─────────┐
       ▼         ▼               ▼         ▼
  Cadastrar   Listar          Buscar      Sair
       │      clientes       por nome       │
       ▼                                    ▼
 Verifica CPF                          Encerra
 já existente                          o programa
       │
  ┌────┴────┐
  ▼         ▼
Duplicado  Novo cliente
 (erro)    adicionado à lista
```

## ▶️ Como executar

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/sistema-cadastro-clientes-python.git

# Acesse a pasta do projeto
cd sistema-cadastro-clientes-python

# Execute o programa
python cadastro_clientes.py
```

Não há dependências externas — basta ter o Python 3 instalado.

## 🧩 Decisões de design

O enunciado original do exercício pedia validação de duplicidade **pelo nome**. Optei por validar pelo **CPF** em vez disso, porque, em um cenário real, duas pessoas diferentes podem ter o mesmo nome, mas nunca terão o mesmo CPF. Um sistema que bloqueia cadastros apenas pelo nome poderia impedir, incorretamente, que um cliente novo com nome coincidente fosse cadastrado — ou, pior, permitir duplicidade real de uma mesma pessoa com uma pequena variação no nome digitado (ex: "Ana Silva" vs "ana silva"). Usar o CPF como identificador único é uma prática mais próxima do que se espera de um sistema real de cadastro.

## 💡 Principais aprendizados

- Diferença entre `print()` e `return` dentro de funções, e como capturar o valor devolvido por uma função para usá-lo fora dela
- Cuidado com nomes de variáveis repetidos dentro de laços (`for`), que podem sobrescrever outros objetos sem gerar erro aparente
- Como estruturar um programa em funções que compartilham uma mesma estrutura de dados (a lista de clientes), em vez de manter tudo em um único bloco de código
- Como percorrer uma lista de objetos comparando atributos específicos (CPF, nome) para implementar validações e buscas

## 🔧 Possíveis melhorias

- [ ] Validar a idade com `try/except`, evitando que o programa quebre com uma entrada não numérica
- [ ] Persistir os dados em um arquivo (`.json` ou `.csv`) ou banco de dados, já que hoje os clientes são perdidos ao fechar o programa
- [ ] Adicionar edição de cadastro existente
- [ ] Criar uma interface gráfica ou web (ex: com Streamlit, já previsto nas próximas etapas do curso)

---

*Projeto pessoal desenvolvido para fins de aprendizado e portfólio.*
