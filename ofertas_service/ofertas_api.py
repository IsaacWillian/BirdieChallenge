from flask import Flask, request
from flask import jsonify
from flask_pymongo import PyMongo
import re

app = Flask(__name__)

mongo = PyMongo(app,"mongodb://localhost:27017/dados")

@app.route('/',methods=['GET'])
def init():
    infos = "Ola, bem vindo!"

    return jsonify(infos)

@app.route('/all',methods=['GET'])
def all():
    result = []
    all_items = mongo.db.ofertas.find({},{"_id":0})
    
    for item in all_items:
        result.append(item)
    return jsonify(result)


@app.route('/productName',methods=['GET'])
def productName():
    nameproduct = request.args.get('name')
    result = []
    regx = re.compile(nameproduct, re.IGNORECASE)
    query = {'name':{"$regex":regx}}
    items = mongo.db.ofertas.find(query,{"_id":0})
    for item in items:
        print(item['price'])
        result.append(item)

    return jsonify(result)


@app.route('/price',methods=['GET'])
def productPrice():
    result = []
    priceMin = request.args.get('min')
    priceMax = request.args.get('max')

    priceMin = float(priceMin) if priceMin != None else 0.0
    priceMax = float(priceMax) if priceMax != None else 100000000.00

    items = mongo.db.ofertas.find({"price" : {"$gte":priceMin,"$lte":priceMax}},{"_id":0})
    
    for item in items:  
        result.append(item)

    return jsonify(result)

@app.route('/store',methods=['GET'])
def productStore():
    store = request.args.get('store')
    result = []
    regx = re.compile(store, re.IGNORECASE)
    query = {'store':{"$regex":regx}}
    items = mongo.db.ofertas.find(query,{"_id":0})
    for item in items:
        result.append(item)

    return jsonify(result)

