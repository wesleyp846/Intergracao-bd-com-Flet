import sqlite3

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
