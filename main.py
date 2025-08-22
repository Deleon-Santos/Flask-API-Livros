from flask import Flask, jsonify, request, make_response
from bd_biblioteca import livros

app = Flask(__name__)

@app.route('/livros', methods=['GET'])
def mostra_livros():    
    return make_response(jsonify(livros))

@app.route("/livros/<int:id>",methods= ['GET'])
def mostra_livros_id(id):
    
    for livro in livros:
        if livro.get('id') == id:
            return make_response(jsonify(livro),200)
    return make_response(jsonify({'mensagem':'livro não encontrado'}), 404)

@app.route('/livros', methods=['POST'])
def cadastrar_livros():
    try:
        novo_livro = request.get_json()
        livros.append(novo_livro)
        return make_response(jsonify({"mensagem":"Novo livro cadastrado"},novo_livro),200)
    except Exception as e:
        return make_response(jsonify({"mensagem":"Erro ao cadastrar livro", "erro": str(e)}), 500)
app.run(debug=True, port =5000)

def editar_livros(id):
    try:
        livro_atualizado = request.get_json()
        for livro in livros:
            if livro.get('id') == id:
                livro.update(livro_atualizado)
                return make_response(jsonify({"mensagem":"Livro atualizado com sucesso"}, livro), 200)
        return make_response(jsonify({'mensagem':'livro não encontrado'}), 404)
    except Exception as e:
        return make_response(jsonify({"mensagem":"Erro ao atualizar livro", "erro": str(e)}), 500)