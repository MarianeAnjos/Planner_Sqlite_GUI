import sqlite3

def abrir_db():
    return sqlite3.connect("tarefas.db")

def criar_tabela():
    with abrir_db() as db:
        c = db.cursor()
        c.execute("""
            CREATE TABLE IF NOT EXISTS tarefas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                categoria TEXT,
                data_limite TEXT,
                prioridade TEXT,
                status TEXT DEFAULT 'Pendente'
            )
        """)
        db.commit()

def adicionar(nome, categoria, data, prioridade):
    with abrir_db() as db:
        c = db.cursor()
        c.execute("""
            INSERT INTO tarefas (nome, categoria, data_limite, prioridade, status)
            VALUES (?, ?, ?, ?, 'Pendente')
        """, (nome, categoria, data, prioridade))
        db.commit()

def listar():
    with abrir_db() as db:
        c = db.cursor()
        c.execute("""
            SELECT * FROM tarefas
            WHERE status = 'Pendente'
            ORDER BY
                CASE prioridade
                    WHEN 'Alta' THEN 1
                    WHEN 'Média' THEN 2
                    WHEN 'Baixa' THEN 3
                    ELSE 4
                END
        """)
        return c.fetchall()

def concluir(id):
    with abrir_db() as db:
        c = db.cursor()
        c.execute("UPDATE tarefas SET status = 'Concluída' WHERE id = ?", (id,))
        db.commit()

def remover(id):
    with abrir_db() as db:
        c = db.cursor()
        c.execute("DELETE FROM tarefas WHERE id = ?", (id,))
        db.commit()
