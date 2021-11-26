from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

bebidas = [
    {"texto": "Coca-cola ", "concluida": ' R$ 4,10'},
    {"texto": "Roller ", "concluida": ' R$ 2,49'},
    {"texto": "Sprite ", "concluida": ' R$ 2,40'},
]

@app.route('/') 
def index():
    return render_template('index.html', lista=bebidas)


@app.route('/create')
def create():
    return render_template('create.html')

@app.route('/save', methods=['POST'])  # <form action="/save" method="POST">
def save():
    texto = request.form['texto']      # <input name="texto"/>
    preco = request.form['preco']
    bebi = { "texto": texto, "concluida": preco }
    bebidas.append(bebi)

    return redirect('https://5000-red-rattlesnake-a9wqju4e.ws-us17.gitpod.io')

@app.route('/busca', methods=['POST'])  
def busca():
    texto = request.form['pesquisa']
    texto = texto.lower()      
    lista = list()
    for bebi in bebidas:
        if texto in bebi['texto'].lower():
            lista.append(bebi)
    if not texto or not lista:
      return render_template('erro.html')

    return render_template('busca.html', lista2=lista)

@app.route('/delete', methods=['POST'])  
def delete():
    deletar_item = request.form['deletar']
    for bebi in bebidas:
        if deletar_item == bebi['texto']:
            bebidas.remove(bebi)
    #if not deletar_item:
      #return render_template('erro.html')

    return render_template('index.html', lista=bebidas)

@app.route('/criar')  
def criar():
    return render_template('delete.html')

app.run(debug=True)