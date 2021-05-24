from flask import Blueprint, Response, request, jsonify
from empregado.database import db_session
from empregado.models.Empregado import Empregado
import json

from empregado.exceptions import Exceptions, EmpregadoNotFound, AllFieldsMustBeFilled

empregado_routes_blueprint = Blueprint('empregado_routes_blueprint', __name__)

@empregado_routes_blueprint.errorhandler(Exceptions)
def error_handler(error):
    return jsonify({"message": error.message}), error.code

@empregado_routes_blueprint.route('/empregados', methods=["GET"])
def seleciona_empregados():
    limit = request.headers.get('limit', 1000)
    offset = request.headers.get('offset', 0)
    empregados_obj = get_empregados(limit=limit, offset=offset)
    empregados_json = [empregado.to_json() for empregado in empregados_obj]
    return response(200, "empregados", empregados_json)


@empregado_routes_blueprint.route('/empregado/<id>', methods=["GET"])
def seleciona_empregado(id):
    empregado = get_empregado_by_id(id)
    if empregado is None:
        raise EmpregadoNotFound
    else:
        empregado_json = empregado.to_json()
    return response(200, "empregado", empregado_json)

@empregado_routes_blueprint.route('/empregado', methods=["POST"])
def insere_empregado():
    body = request.get_json()
    try:
        empregado_obj = post_empregado(nome=body["nome"], sexo=body["sexo"], data_criacao=body["data_criacao"], idade=body["idade"], salario=body["salario"])
        empregado_json = empregado_obj.to_json()
        return response(200, "empregado", empregado_json)
    except:
        raise AllFieldsMustBeFilled

@empregado_routes_blueprint.route('/empregado/<id>', methods=["PUT"])
def atualiza_empregado(id):
    body = request.get_json()
    empregado_obj = put_empregado(id, body)
    empregado_json = empregado_obj.to_json()
    return response(200, "empregado", empregado_json)

@empregado_routes_blueprint.route('/empregado/<id>', methods=["DELETE"])
def excluir_empregado(id):
    empregado_obj = delete_empregado(id)
    empregado_json = empregado_obj.to_json()
    if not empregado_obj:
        raise EmpregadoNotFound
    return response(204, "empregado", empregado_json)

def get_empregado_by_id(id):
    empregado = db_session.query(Empregado).filter(id == Empregado.id).first()
    return empregado

def get_empregados(limit=1000, offset=0):
    empregados = db_session.query(Empregado).limit(limit).offset(offset)
    return empregados

def post_empregado(nome, sexo, data_criacao, idade, salario):
    id = None
    empregado_obj = Empregado(id, nome, sexo, data_criacao, idade, salario)
    db_session.add(empregado_obj)
    db_session.commit()
    return empregado_obj

def put_empregado(id, body):
    empregado_obj = get_empregado_by_id(id)
    if not empregado_obj:
        raise EmpregadoNotFound
    if ("nome" in body):
        empregado_obj.nome = body['nome']
    if ("sexo" in body):
        empregado_obj.sexo = body['sexo']
    if ("data_criacao" in body):
        empregado_obj.data_criacao = body['data_criacao']
    if ("idade" in body):
        empregado_obj.idade = body['idade']
    if ("salario" in body):
        empregado_obj.salario = body['salario']
    db_session.add(empregado_obj)
    db_session.commit()
    return empregado_obj

def delete_empregado(id):
    empregado_obj = get_empregado_by_id(id)
    if not empregado_obj:
        raise EmpregadoNotFound
    db_session.delete(empregado_obj)
    db_session.commit()
    return empregado_obj

def response(status, nome_do_conteudo, conteudo, mensagem=False):
    body = {}
    body[nome_do_conteudo] = conteudo

    if(mensagem):
        body["mensagem"] = mensagem

    return Response(json.dumps(body), status=status, mimetype="application/json")