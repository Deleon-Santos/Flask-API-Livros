

import sqlite3

def bd():
    conn = sqlite3.connect('biblioteca.db')
    return conn

def criar_tabela():
    try:
        conexao = bd()
        cursor = conexao.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS livros (
            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            titulo VARCHAR(100) NOT NULL,
            autor VARCHAR(100) NOT NULL
        )
        ''')
        conexao.commit()
        conexao.close()
    except Exception as e:
        print(f"Erro ao criar tabela: {e}") 
        
def obter_livros(id):
    try:
        conexao = bd()
        cursor = conexao.cursor()
        
        if id is None:
            cursor.execute('SELECT * FROM livros')
            livros = cursor.fetchall()
            return [
                {'id': livro[0], 'titulo': livro[1], 'autor': livro[2]}
                for livro in livros
            ]
        else:
            cursor.execute('SELECT * FROM livros WHERE id = ?', (id,))
            livro = cursor.fetchone()
            if livro:
                return {'id': livro[0], 'titulo': livro[1], 'autor': livro[2]}
            return None

    except Exception as e:
        print(f"Erro ao obter livros: {e}")
        return [] if id is None else None

    finally:
        try:
            conexao.close()
        except:
            pass
        
def cadastrar_livoros(novo_livro):
    try:
        conexao = bd()
        cursor = conexao.cursor()
        cursor.execute('INSERT INTO livros (titulo, autor) VALUES (?, ?)', (novo_livro['titulo'], novo_livro['autor']))
        conexao.commit()
        cadastro = cursor.lastrowid
        cursor.execute('SELECT * FROM livros WHERE id = ?', (cadastro,))
        livro = cursor.fetchone()
        return {'id': livro[0], 'titulo': livro[1], 'autor': livro[2]}  
    except Exception as e:
        return None
    finally:    
        try:
            conexao.close()
        except:
            pass
        
def editar_livros(id,titulo, autor):
    try:
        conexao = bd()
        cursor= conexao.cursor()
        cursor.execute('UPDATE livros SET titulo = ? , autor = ? WHERE id =?', (titulo, autor, id,))
        conexao.commit()
        if cursor.rowcount == 0:
            return None 
        cursor.execute('SELECT * FROM livros WHERE id = ?', (id,))
        livro = cursor.fetchone()   
        return {'id': livro[0], 'titulo': livro[1], 'autor': livro[2]}
    except Exception as e:
        return None 
    finally:    
        try:
            conexao.close()
        except:
            pass
        

def excluir_livro(id):
    try:
        conexao= bd ()
        cursor= conexao.cursor()
        cursor.execute('SELECT * FROM livros WHERE id = ?', (id,))
        livro = cursor.fetchone()
        if not livro:
            return None
        cursor.execute('DELETE FROM livros WHERE id = ?' , (id,))
        conexao.commit()
        return {'id': livro[0], 'titulo': livro[1], 'autor': livro[2]}
        
        
            
    except Exception as e:
        return {"mensagem": "Erro ao excluir livro", "erro": str(e)}
    finally:    
        try:
            conexao.close()
        except:
            pass
        