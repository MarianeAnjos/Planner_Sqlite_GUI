class Tarefa:
    def __init__(self, id, nome, categoria, data_limite, prioridade, status="Pendente"):
        self.id = id
        self.nome = nome
        self.categoria = categoria
        self.data_limite = data_limite
        self.prioridade = prioridade
        self.status = status

    def __str__(self):
        return f"[{self.id}] {self.nome} | Categoria: {self.categoria} | Prazo: {self.data_limite} | Prioridade: {self.prioridade} | Status: {self.status}"
