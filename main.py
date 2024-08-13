from flask import Flask, make_response, jsonify, request
from bd import Carros


app = Flask(__name__)
app.json.sort_keys = False #Para não ordenar


@app.route('/carros', methods=['GET'])
def get_carros():
    return make_response(       #Nesse caso simples, não seria necessário o uso do make_response e jsonify
        jsonify(Carros)         #já que somente com o return Carro a função rodaria.
    )

@app.route('/carros', methods=['POST'])
def create_carro():
    carro = request.json
    '''Verificar se o ID já existe na lista
    if any(c['id'] == carro['id'] for c in Carros):
        return make_response(jsonify(Mensagem='Erro, id já existente.'))'''
    Carros.append(carro)
    return make_response(
        jsonify(Mensagem = 'Carro cadastrado com sucesso.', Carro=carro)
    )       

@app.route('/carros/<int:id>', methods=['DELETE'])
def delete_carro(id):
    carro = next((carro for carro in Carros if carro['id'] == id), None)
    
    if carro is None:
        return make_response(
            jsonify(Mensagem='Carro não encontrado.')
        )
    
    Carros.remove(carro)
    return make_response(
        jsonify(Mensagem='Carro excluído com sucesso.', Carro=carro)
    )


app.run()