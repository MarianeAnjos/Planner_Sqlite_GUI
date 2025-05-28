# **Planner Automatizado em Python com SQLite**

Projeto desenvolvido com foco em organização de tarefas, automação com banco de dados SQLite e interface gráfica com Tkinter.

---

## **Tecnologias e Ferramentas**
- Python 3.12 
- SQLite (armazenamento local de dados)  
- Tkinter (interface gráfica)  
- Git + GitHub  

---

## **Objetivo**
> A aplicação permite:  
Adicionar tarefas com nome, categoria, data limite e prioridade  
Listar tarefas pendentes, organizadas por prioridade (**Alta → Média → Baixa**)  
Atualizar tarefas como concluídas 
Remover tarefas do banco de dados  
Interagir via interface gráfica Tkinter e terminal  

---

## **Estrutura do Projeto**

planner_sqlite_gui/
├── main.py           → Arquivo principal que executa o programa
├── db/               → Pasta para gerenciamento do banco de dados
│   ├── database.py   → Configuração do SQLite e funções CRUD (Create, Read, Update, Delete)
├── ui/               → Pasta para interface gráfica
│   ├── interface.py  → Interface Tkinter para interagir com as tarefas
├── models/           → Pasta opcional para representar a estrutura de uma Tarefa
│   ├── tarefa.py     → Classe Tarefa
├── tarefas.db        → Banco de dados SQLite (gerado automaticamente)
├── README.md         → Documentação do projeto


---

## **Observações**
> Este projeto usa SQLite** como banco de dados local, ideal para projetos simples e sem dependência de servidores.  
> Interface gráfica desenvolvida com Tkinter, permitindo interação visual com as tarefas.  
> Foco no aprendizado e na organização de código, com separação entre banco, lógica e UI.  

---

## **Como Executar**
- Clone este repositório:  
   ```bash
   git clone https://github.com/MarianeAnjos/Planner_Sqlite_GUI

- Navegue até a pasta do projeto:
    cd planner_sqlite_gui

- Execute o scpirt principal:
    python3 main.py

- A interface gráfica pode ser iniciada pelo menu do terminal ou diretamente com interface.py.
- Este projeto foi desenvolvido como parte de um estudo prático, aprimorando habilidades em Python, automação e manipulação de banco de dados.