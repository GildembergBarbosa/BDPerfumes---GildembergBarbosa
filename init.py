import sqlite3
path = r"C:\SQLite\Nova pasta"
banco = sqlite3.connect(path + r"\perfumes.bd")
cursor = banco.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS Marca (id integer,nome text)")
cursor.execute("CREATE TABLE IF NOT EXISTS Fixacoes(id integer,nome text)")
cursor.execute("CREATE TABLE IF NOT EXISTS Perfumes(id integer,nome text,quantidade integer,marca_FK integer,fixacoes_FK integer,volume integer)")
cursor.execute("CREATE TABLE IF NOT EXISTS Volumes (id integer,nome text)")
cursor.execute("CREATE TABLE IF NOT EXISTS Essencia_perfume(essencia_FK integer,perfume_FK integer)")
cursor.execute("CREATE TABLE IF NOT EXISTS Essencias(id integer,nome text)")
