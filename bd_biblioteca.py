

import sqlite3
def bd():
    conn = sqlite3.connect('biblioteca.db')
    return conn

def criar_tabela():
    conexao = bd()
    cursor = conexao.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS livros (
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        titulo VARCHAR(100) NOT NULL,
        autor VARCHAR(100) NOT NULL
    )
    ''')

    cursor.executemany('''
    INSERT INTO livros (titulo, autor) VALUES (?, ?)
    ''', [
        ('O Senhor dos Anéis', 'J.R.R. Tolkien'),
        ('1984', 'George Orwell'),
        ('A Revolução dos Bichos', 'George Orwell')
    ])

    conexao.commit()
    conexao.close()

def obter_livros():
    conexao = bd()
    cursor = conexao.cursor()
    cursor.execute('SELECT * FROM livros')
    livros = cursor.fetchall()
    conexao.close()
    lista_livros = []
    for livro in livros:
        lista_livros.append({
            'id': livro[0],
            'titulo': livro[1],
            'autor': livro[2]
        })
    return lista_livros