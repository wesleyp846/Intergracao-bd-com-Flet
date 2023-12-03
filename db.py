import sqlite3

class dbcomando:
    def __init__(self, nome_banco_dados):
        # Conectar ao banco de dados
        self.conexao = sqlite3.connect(nome_banco_dados)
        self.comando = self.conexao.cursor()

    def criar_tabela(self, tabela,colunat,colunan, colunate):
        self.comando.execute(
            f"""CREATE TABLE IF NOT EXISTS {tabela} (
                id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                {colunat} TEXT NOT NULL, {colunan} INTEGER, {colunate} TEXT
                )"""
            )
        self.conexao.commit()

    def inserir_dados(self, dados):
        # Inserir dados na tabela
        self.comando.executemany("INSERT INTO tabela1 (nome) VALUES (?)", dados)
        self.conexao.commit()

    def ler_dados(self):
        # Consultar todos os dados da tabela
        self.comando.execute("SELECT * FROM tabela1")
        return self.comando.fetchall()

    def atualizar_dados(self, novos_dados):
        # Atualizar dados na tabela
        for pessoa in novos_dados:
            self.comando.execute("UPDATE tabela1 SET nome = ? WHERE id = ?", pessoa)
        self.conexao.commit()

    def excluir_dados(self, dado_a_excluir):
        # Excluir dados da tabela
        self.comando.execute("DELETE FROM tabela1 WHERE nome = ?", (dado_a_excluir,))
        self.conexao.commit()

    def fechar_conexao(self):
        # Fechar a conexão com o banco de dados
        self.conexao.close()

# Exemplo de uso
if __name__ == "__main__":
    # Criar uma instância da classe
    manipulador_bd = dbcomando("seu_banco_de_dados.db")

    # Exemplo de inserção
    dados_inserir = [('Mariana',), ('Jonas',)]
    manipulador_bd.inserir_dados(dados_inserir)

    # Exemplo de leitura
    dados_lidos = manipulador_bd.ler_dados()
    print("Dados lidos:", dados_lidos)

    # Exemplo de atualização
    novos_dados_atualizar = [('Jesebel', 1), ('Emanual', 2)]
    manipulador_bd.atualizar_dados(novos_dados_atualizar)

    # Exemplo de exclusão
    dado_a_excluir = 'Jesebel'
    manipulador_bd.excluir_dados(dado_a_excluir)

    # Fechar a conexão com o banco de dados
    manipulador_bd.fechar_conexao()

# #CRUD (Criar e inserir [CREAT])
# conexao = sqlite3.connect('banco.db')
# comando = conexao.cursor()

# #Criação
# comando.execute(
#     """CREATE TABLE IF NOT EXISTS tabela1 (
#         id INTEGER PRIMARY KEY AUTOINCREMENT NOT NUll, 
#         nome TEXT NOT NUll
#     )"""
# )

# conexao.close()

# #Inserção
# dado = [
#     ('Maria'),
# ]
# comando.execute("""INSERT INTO tabela1 (nome) VALUES (?)""", dado)
# conexao.commit()

# #Inserção dupla
# dado = [
#     ('Mariana',), 
#     ('Jonas',)
# ]

# comando.executemany("""INSERT INTO tabela1 (nome) VALUES (?)""", dado)
# conexao.commit()

# #CRUD (Ler [READ])
# def ler_banco():
#     conexao = sqlite3.connect('banco.db')
#     comando = conexao.cursor()

#     comando.execute("""SELECT * FROM tabela1""")
#     consulta=comando.fetchall()
#     print(consulta)
#     #Para melhor visibilidade usamos um for
#     for pessoa in consulta:
#         print(pessoa[1])

#     conexao.close()

# #CRUD (Editar dados [UPDATE])
# conexao = sqlite3.connect('banco.db')
# comando = conexao.cursor()

# dado_antigo='Julia'
# dado='Maria'
# comando.execute(
#     """UPDATE tabela1 SET nome = ? WHERE nome = ?""", 
#     (dado, dado_antigo),
# )
# conexao.commit()
# conexao.close()
# #ler_banco()

# Edição dupla
# conexao = sqlite3.connect('banco.db')
# comando = conexao.cursor()

# novos_dados = [
#     ('Jesebel', 1), 
#     ('Emanual', 2)
# ]
# # Iterar sobre os novos dados e executar a atualização
# for pessoa in novos_dados:
#     comando.execute(
#         """UPDATE tabela1 SET nome = ? WHERE id = ?""",
#         pessoa
#     )
# conexao.commit()
# conexao.close()
# #ler_banco()

# #CRUD (Apagar dados [DELITE])
# conexao = sqlite3.connect('banco.db')
# comando = conexao.cursor()
# # Dado a ser excluído
# dado_a_excluir = 'Mariana'
# comando.execute(
#     """DELETE FROM tabela1 WHERE nome = ?""",
#     (dado_a_excluir,))

# conexao.commit()
# conexao.close()
# ler_banco()

