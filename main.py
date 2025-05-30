from db.database import criar_tabela, adicionar, listar, concluir, remover
from ui.interface import iniciar_interface

criar_tabela()

def mostrar_menu():
    print("\nMENU")
    print("1. Adicionar tarefa")
    print("2. Listar tarefas pendentes")
    print("3. Concluir tarefa")
    print("4. Remover tarefa")
    print("5. Abrir interface gráfica")
    print("6. Sair")

def main():
    while True:
        mostrar_menu()
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            nome = input("Nome da tarefa: ")
            categoria = input("Categoria (opcional): ")
            data = input("Data limite (YYYY-MM-DD): ")
            prioridade = input("Prioridade (Alta, Média, Baixa): ")
            adicionar(nome, categoria, data, prioridade)
            print("Tarefa adicionada!")

        elif escolha == "2":
            tarefas = listar()
            if tarefas:
                print("\nTarefas Pendentes:")
                for t in tarefas:
                    print(f"[{t[0]}] {t[1]} | Categoria: {t[2]} | Prazo: {t[3]} | Prioridade: {t[4]}")
            else:
                print("Nenhuma tarefa pendente!")

        elif escolha == "3":
            id_tarefa = input("Digite o ID da tarefa que deseja concluir: ")
            concluir(int(id_tarefa))
            print("Tarefa marcada como concluída!")

        elif escolha == "4":
            id_tarefa = input("Digite o ID da tarefa que deseja remover: ")
            remover(int(id_tarefa))
            print("Tarefa removida!")

        elif escolha == "5":
            iniciar_interface()

        elif escolha == "6":
            print("Saindo do programa.")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
