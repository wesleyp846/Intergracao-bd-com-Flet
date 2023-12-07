from classes import Dados

db=Dados('banco.db')
print(db.ler_dados())

db.salvar_dados('Judas','5487','adet@fvgsdf.com','rua de')
print(db.ler_dados())

db.editar_dados('Judas', 'Jonas')
print(db.ler_dados())

db.deletar_dados('João')
print(db.ler_dados())