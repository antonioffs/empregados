from flask import Blueprint, Response, request, jsonify
from empregado.database import db_session
from empregado.models.Empregado_Endereco import Empregado_endereco
import json

from empregado.exceptions import Exceptions, EmpregadoEnderecoNotFound, AllFieldsMustBeFilled

empregado_end_routes_blueprint = Blueprint('empregado_end_routes_blueprint', __name__)

@empregado_end_routes_blueprint.errorhandler(Exceptions)
def error_handler(error):
    return jsonify({"message": error.message}), error.code

@empregado_end_routes_blueprint.route('/empregados-end', methods=["GET"])
def seleciona_empregados_end():
    limit = request.headers.get('limit', 1000)
    offset = request.headers.get('offset', 0)
    empregados_end_obj = get_empregados_end(limit=limit, offset=offset)
    empregados_end_json = [empregado_end.to_json() for empregado_end in empregados_end_obj]
    return response(200, "empregados-endereço", empregados_end_json)


@empregado_end_routes_blueprint.route('/empregado-end/<id>', methods=["GET"])
def seleciona_empregado_end(id):
    empregado_end = get_empregado_end_by_id(id)
    if empregado_end is None:
        raise EmpregadoEnderecoNotFound
    else:
        empregado_end_json = empregado_end.to_json()
    return response(200, "empregados-endereço", empregado_end_json)

@empregado_end_routes_blueprint.route('/empregado-end', methods=["POST"])
def insere_empregado():
    body = request.get_json()
    try:
        empregado_end_obj = post_empregado_end(id_empregado=body["id_empregado"],
                                               logradouro=body["logradouro"],
                                               bairro=body["bairro"],
                                               cidade=body["cidade"],
                                               estado=body["estado"],
                                               numero=body["numero"],
                                               cep=body["cep"],)
        empregado_end_json = empregado_end_obj.to_json()
        return response(200, "empregados-endereço", empregado_end_json)
    except:
        raise AllFieldsMustBeFilled

@empregado_end_routes_blueprint.route('/empregado-end/<id>', methods=["PUT"])
def atualiza_empregado(id):
    body = request.get_json()
    empregado_end_obj = put_empregado_end(id, body)
    empregado_end_json = empregado_end_obj.to_json()
    return response(200, "empregados-endereço", empregado_end_json)

@empregado_end_routes_blueprint.route('/empregado-end/<id>', methods=["DELETE"])
def excluir_empregado(id):
    empregado_end_obj = delete_empregado_end(id)
    empregado_end_json = empregado_end_obj.to_json()
    if not empregado_end_obj:
        raise EmpregadoEnderecoNotFound
    return response(204, "empregados-endereço", empregado_end_json)

def get_empregados_end(limit=1000, offset=0):
    empregados_end = db_session.query(Empregado_endereco).limit(limit).offset(offset)
    return empregados_end

def get_empregado_end_by_id(id):
    empregado_end = db_session.query(Empregado_endereco).filter(id == Empregado_endereco.id).first()
    return empregado_end

def post_empregado_end(id_empregado, logradouro, bairro, cidade, estado, numero, cep):
    id = None
    empregado_end_obj = Empregado_endereco(id, id_empregado, logradouro, bairro, cidade, estado, numero, cep)
    db_session.add(empregado_end_obj)
    db_session.commit()
    return empregado_end_obj

def put_empregado_end(id, body):
    empregado_end_obj = get_empregado_end_by_id(id)
    if(not empregado_end_obj):
        raise EmpregadoEnderecoNotFound
    if("logradouro" in body):
       empregado_end_obj.nome = body['logradouro']
    if("bairro" in body):
       empregado_end_obj.sexo = body['bairro']
    if("cidade" in body):
       empregado_end_obj.data_criacao = body['cidade']
    if("estado" in body):
       empregado_end_obj.idade = body['estado']
    if("numero" in body):
       empregado_end_obj.salario = body['numero']
    if("cep" in body):
        empregado_end_obj.salario = body['cep']
    db_session.add(empregado_end_obj)
    db_session.commit()
    return empregado_end_obj

def delete_empregado_end(id):
    empregado_end_obj = get_empregado_end_by_id(id)
    if not empregado_end_obj:
        raise EmpregadoEnderecoNotFound
    db_session.delete(empregado_end_obj)
    db_session.commit()
    return empregado_end_obj

def response(status, nome_do_conteudo, conteudo, mensagem=False):
    body = {}
    body[nome_do_conteudo] = conteudo

    if(mensagem):
        body["mensagem"] = mensagem

    return Response(json.dumps(body), status=status, mimetype="application/json")