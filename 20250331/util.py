from contextlib import contextmanager
import sqlite3

# Define o nome padrão do arquivo do banco de dados
DB_NAME = 'dados.db'

@contextmanager
def get_db_connection(db_name=DB_NAME):
    """
    Gerenciador de contexto para conexões com o banco de dados SQLite.
    Garante que a conexão seja fechada e as alterações commitadas.
    """
    conn = None  # Inicializa conn como None
    try:
        # Estabelece a conexão com o banco de dados
        conn = sqlite3.connect(db_name)
        # Habilita o uso de dicionários para os resultados das queries
        conn.row_factory = sqlite3.Row
        # Disponibiliza a conexão para ser usada dentro do bloco 'with'
        yield conn
    except sqlite3.Error as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        raise
    finally:
        # Este bloco é executado sempre, mesmo se ocorrerem erros
        if conn:
            # Confirma (commita) as transações pendentes
            conn.commit()
            # Fecha a conexão com o banco de dados
            conn.close()
