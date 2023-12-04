from db import dbcomando

# # Criar uma instância da classe
db = dbcomando('banco.db')
db.criar_tabela('contatos', 'nome', 'tel', 'email', 'endereco')

# Exemplo de inserção
dados_inserir = [('Mariana', '549874563621', 'mariana@jupira.com', 'Av.Calhamaço',), 
                 ('Jonas', '59748572134', 'mariana@jupira.com', 'Rua Terebentina')]

db.inserir_dados('contatos', 'nome', 'tel', 'email', 'endereco', dados_inserir)

# # Exemplo de leitura
# dados_lidos = manipulador_bd.ler_dados()
# print("Dados lidos:", dados_lidos)

# # Exemplo de atualização
# novos_dados_atualizar = [('Jesebel', 1), ('Emanual', 2)]
# manipulador_bd.atualizar_dados(novos_dados_atualizar)

# # Exemplo de exclusão
# dado_a_excluir = 'Jesebel'
# manipulador_bd.excluir_dados(dado_a_excluir)

# # Fechar a conexão com o banco de dados
# manipulador_bd.fechar_conexao()
