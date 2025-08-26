# aplicção de cadastro , busca, atualiazação e exclusão de livros em bibliotecas.
# API isandos Flask e SQL.
import bd_biblioteca as livros
from flask import Flask, jsonify, request, make_response


livros.criar_tabela()
app = Flask(__name__)

#o metodo get deve retornar todos os livors da nossa base de dados
@app.route('/livros', methods=['GET'])
def mostra_livros():  
    livros_cadastrados = livros.obter_livros(id=None)
    if not livros_cadastrados :
        return make_response(jsonify({'mensagem':'Nenhum livro encontrado'}), 404)  
    return make_response(jsonify(livros_cadastrados),200)


#o metodo get vais retornar o livro referenciado no id
#o respota deve ser um livro encotrado com codigo 200 ou o erro comcodigo 404
@app.route("/livros/<int:id>", methods=['GET'])
def mostra_livros_id(id):
    try:
        livros_cadastrados = livros.obter_livros(id)
        if livros_cadastrados:
            return make_response(jsonify(livros_cadastrados), 200)
        return make_response(jsonify({'mensagem': 'O livro não foi encontrado'}), 404)
        

    except Exception as e:
        return make_response(jsonify({
            "mensagem": "Erro ao buscar livro",
            "erro": str(e)
        }), 500)


#o metodo post deve ler o novo livro no corpo da requisição usando request.get_json()
#depois adicionar o novo livro na base de dados, ou devolver uma mensagem de erro
@app.route('/livros', methods=['POST'])
def cadastrar_livros():
    try:
        novo_livro = request.get_json()
        novo_cadastro = livros.cadastrar_livoros(novo_livro)
        if novo_cadastro:
        
            return make_response(jsonify({"mensagem":"Novo livro cadastrado"},novo_cadastro),200)
        return make_response(jsonify({'mensagem':'Erro ao cadastrar livro'}), 400)
    except Exception as e:
        return make_response(jsonify({"mensagem":"Erro ao cadastrar livro", "erro": str(e)}), 500)
    
#metodo para editar um livro pelo id
#a requisição recebe o um request em json com os dados atualizados.
#o retorno deve ser o livro atualizado ou uma mensagem de erro
@app.route('/livros/<int:id>', methods =['PUT'])
def editar_livros(id):
    try:
        livro_atualizado = request.get_json()
        if not livro_atualizado:
            return make_response(jsonify({"mensagem": "Nenhum dado enviado"}), 400)
        autor = livro_atualizado.get('autor')
        titulo = livro_atualizado.get('titulo')
        livro = livros.editar_livros(id,titulo, autor)
        if livro:
                return make_response(jsonify({"mensagem":"Livro atualizado com sucesso"},{"livro": livro}), 200)
        return make_response(jsonify({'mensagem':'livro não encontrado'}), 404)
    except Exception as e:
        return make_response(jsonify({"mensagem":"Erro ao atualizar livro", "erro": str(e)}), 500)
    
# o metodo delete deve receber um id da requiseção e se encontrado o livro vais ser deletado
# o retorno deve ser uma mensagem de sucesso ou uma mensagem de erro
@app.route('/livros/<int:id>',methods = ['DELETE'])
def escluir_livro(id):
    try:        
        livro_excluido = livros.excluir_livro(id)
        if not livro_excluido:
            return make_response(jsonify({'mensagem':'livro não encontrado'}), 404)
        
        return make_response(jsonify({"mensagem":"Livro excluído com sucesso", "livro":livro_excluido}), 200)
        
    except Exception as e:
        return make_response(jsonify({"mensagem":"Erro ao excluir livro", "erro": str(e)}), 500)
    
if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000)

