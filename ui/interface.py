import sqlite3
import tkinter as tk
from tkinter import messagebox
from db.database import adicionar, listar, concluir, remover

def listar_tarefas():
    """Exibir todas as tarefas na interface"""
    tarefas = listar()
    tarefas_lista = "\n".join([f"[{t[0]}] {t[1]} ({t[5]})" for t in tarefas])
    messagebox.showinfo("Lista de Tarefas", tarefas_lista if tarefas_lista else "Nenhuma tarefa encontrada.")

def atualizar_status():
    """Atualizar o status de uma tarefa para 'Concluída'"""
    tarefa_id = entry_id.get().strip()
    if not tarefa_id.isnumeric():
        messagebox.showerror("Erro", "Digite um ID válido.")
        return
    
    concluir(int(tarefa_id))
    messagebox.showinfo("Sucesso", f"Tarefa ID {tarefa_id} marcada como concluída.")

def deletar_tarefa():
    """Excluir uma tarefa pelo ID"""
    tarefa_id = entry_id.get().strip()
    if not tarefa_id.isnumeric():
        messagebox.showerror("Erro", "Digite um ID válido.")
        return
    
    remover(int(tarefa_id))
    messagebox.showinfo("Sucesso", f"Tarefa ID {tarefa_id} excluída.")

def adicionar_tarefa():
    """Abrir janela para adicionar tarefa"""
    def salvar_tarefa():
        """Salvar nova tarefa no banco de dados"""
        nome = entry_nome.get().strip()
        categoria = entry_categoria.get().strip()
        data_limite = entry_data.get().strip()
        prioridade = entry_prioridade.get().strip()

        if not nome or not categoria or not data_limite or not prioridade:
            messagebox.showerror("Erro", "Todos os campos devem ser preenchidos.")
            return

        adicionar(nome, categoria, data_limite, prioridade)
        messagebox.showinfo("Sucesso", f"Tarefa '{nome}' adicionada.")
        janela_add.destroy()

    # Criar janela secundária para entrada de dados
    janela_add = tk.Toplevel()
    janela_add.title("Adicionar Nova Tarefa")
    janela_add.geometry("300x250")

    tk.Label(janela_add, text="Nome da Tarefa:").pack()
    entry_nome = tk.Entry(janela_add)
    entry_nome.pack()

    tk.Label(janela_add, text="Categoria:").pack()
    entry_categoria = tk.Entry(janela_add)
    entry_categoria.pack()

    tk.Label(janela_add, text="Data Limite (YYYY-MM-DD):").pack()
    entry_data = tk.Entry(janela_add)
    entry_data.pack()

    tk.Label(janela_add, text="Prioridade (Alta, Média, Baixa):").pack()
    entry_prioridade = tk.Entry(janela_add)
    entry_prioridade.pack()

    tk.Button(janela_add, text="Salvar", command=salvar_tarefa).pack(pady=10)

def iniciar_interface():
    """Criar interface gráfica"""
    janela = tk.Tk()
    janela.title("Planner de Tarefas")
    janela.geometry("400x350")

    tk.Label(janela, text="Bem-vinda ao Planner", font=("Arial", 14)).pack(pady=10)
    
    global entry_id
    tk.Label(janela, text="Digite o ID da Tarefa:").pack()
    entry_id = tk.Entry(janela)
    entry_id.pack(pady=5)

    tk.Button(janela, text="Listar Tarefas", command=listar_tarefas).pack(pady=5)
    tk.Button(janela, text="Adicionar Tarefa", command=adicionar_tarefa).pack(pady=5)
    tk.Button(janela, text="Atualizar Status", command=atualizar_status).pack(pady=5)
    tk.Button(janela, text="Deletar Tarefa", command=deletar_tarefa).pack(pady=5)
    tk.Button(janela, text="Fechar", command=janela.destroy).pack(pady=10)

    janela.mainloop()
