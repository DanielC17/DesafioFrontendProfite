from application import app
from application.model.dao.produtosDAO import ProdutosDAO
from flask import Flask, render_template, redirect, url_for, jsonify


lista_produtos_arquivo = ProdutosDAO()
lista_produtos_json = lista_produtos_arquivo.lista_produtos_json()
print(lista_produtos_json)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/produtos")
def produtos():
    return render_template("produtos.html", lista_produtos_json=lista_produtos_json[0:4])
