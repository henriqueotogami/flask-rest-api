from flask import Flask, jsonify, request
import json

app = Flask(__name__)

@app.route('/<int:id>')
def pessoa(id):
    soma =1 + int(id)
    return jsonify({'id': id, 'nome':'Rafael', 'profissao':'Desenvolvedor'})

#@app.route('/soma/<int:valor1>/<int:valor2>')
#def soma(valor1, valor2):
#    return jsonify({'soma':valor1 + valor2})

@app.route('/soma', method=['POST'])
def soma():
    if request.method == 'POST':
        dados = json.loads(request.data)
        total = sum(dados['valores'])
    elif request.method = 'GET':
        total = 10 + 10
    return jsonify({'soma': total})

if __name__ == '__main__':
    app.run()