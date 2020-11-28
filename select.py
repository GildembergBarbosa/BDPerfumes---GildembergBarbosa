import sqlite3
def titulo(n,s):
    print('='*n)
    print(f'{s}'.center(n))
    print('=' * n)

path = r"C:\SQLite\Nova pasta"
banco = sqlite3.connect(path + r"\perfumes.bd")
cursor = banco.cursor()

#Marca
cursor.execute("SELECT * FROM Marca")
tabela = cursor.fetchall()
titulo(78,'Marca')
print('ID'.ljust(5)+'Nome')
for linha in tabela:
    print(str(linha[0]).ljust(5),end="")
    print(linha[1])

#Fixações
cursor.execute("SELECT * FROM Fixacoes")
tabela = cursor.fetchall()
titulo(78,'Fixações')
print('ID'.ljust(5)+'Nome')
for linha in tabela:
    print(str(linha[0]).ljust(5),end="")
    print(linha[1])

#Perfumes
cursor.execute("SELECT * FROM Perfumes")
tabela = cursor.fetchall()
titulo(78,'Perfumes')
print('ID'.ljust(5)+'Nome'.ljust(15)+'quantidade'.ljust(14)+'marca'.ljust(16)+'fixação'.ljust(17)+'volume')
for linha in tabela:
    print(str(linha[0]).ljust(5),end="")
    print(str(linha[1]).ljust(15), end="")
    print(str(linha[2]).ljust(14), end="")
    print(str(linha[3]).ljust(16), end="")
    print(str(linha[4]).ljust(17), end="")
    print(linha[5])

#Essencia_perfume
cursor.execute("SELECT * FROM Essencia_perfume")
tabela = cursor.fetchall()
titulo(78,'Essencia_perfume')
print('essencia_FK'.ljust(15)+'perfume_FK')
for linha in tabela:
    print(str(linha[0]).ljust(15),end="")
    print(linha[1])

#Essencias
cursor.execute("SELECT * FROM Essencias")
tabela = cursor.fetchall()
titulo(78,'Essencias')
print('ID'.ljust(5)+'Nome')
for linha in tabela:
    print(str(linha[0]).ljust(5),end="")
    print(linha[1])




