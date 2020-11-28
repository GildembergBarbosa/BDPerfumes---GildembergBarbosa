import sqlite3
path = r"C:\SQLite\Nova pasta"
banco = sqlite3.connect(path + r"\perfumes.bd")
cursor = banco.cursor()
#Marca
cursor.execute("INSERT INTO Marca VALUES(1,'marca1')")
cursor.execute("INSERT INTO Marca VALUES(2,'marca2')")
#Fixações
cursor.execute("INSERT INTO Fixacoes VALUES(1,'fixações1')")
cursor.execute("INSERT INTO Fixacoes VALUES(2,'fixações2')")
#Perfumes
cursor.execute("INSERT INTO Perfumes VALUES(1,'perfume1',1,1,1,1)")
cursor.execute("INSERT INTO Perfumes VALUES(2,'perfume2',2,2,2,2)")
#Volume
cursor.execute("INSERT INTO Volumes VALUES(1,'volume1')")
cursor.execute("INSERT INTO Volumes VALUES(2,'volume2')")
#Essencia_perfume
cursor.execute("INSERT INTO Essencia_perfume VALUES(1,1)")
cursor.execute("INSERT INTO Essencia_perfume VALUES(2,2)")
#Essencias
cursor.execute("INSERT INTO Essencias VALUES(1,'essencia1')")
cursor.execute("INSERT INTO Essencias VALUES(2,'essencia2')")
banco.commit()