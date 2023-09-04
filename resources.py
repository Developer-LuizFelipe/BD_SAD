from flask_restful import Resource, reqparse
from flask import jsonify 
from models import db, Status, Departamento, Usuario, Acao, Documento, StatusSchema, DepartamentoSchema, UsuarioSchema, AcaoSchema, DocumentoSchema

class StatusResource(Resource):
    def get(self, status_id=None):
        if status_id is None:
            status = Status.query.all() 
            return StatusSchema(many=True).dump(status), 200
    
        status = Status.query.get(status_id)
        return StatusSchema().dump (status), 200
    
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('descricao', type=str, required=True)
        args= parser.parse_args()
        status = Status (descricao=args['descricao'])
        db.session.add(status)
        db.session.commit()
        return StatusSchema().dump(status), 201
    
    def put(self, status_id):
        parser = reqparse.RequestParser()
        parser.add_argument('descricao', type=str, required=True)
        args= parser.parse_args()
        status = Status.query.get(status_id)
        status.descricao = args['descricao']
        db.session.commit()
        return StatusSchema().dump(status), 200
    
    def delete(self, status_id):
        status = Status.query.get(status_id)
        db.session.delete(status)
        db.session.commit()
        return jsonify({"msg":"Status excluido !"})
     
class DepartamentoResource(Resource):
    def get(self, departamento_id=None):
        if departamento_id is None:
            departamentos = Departamento.query.all() 
            return DepartamentoSchema(many=True).dump(departamentos), 200
    
        departamento = Departamento.query.get(departamento_id)
        return DepartamentoSchema().dump (departamento), 200
    
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('nome', type=str, required=True)
        args= parser.parse_args()
        departamento = Departamento (nome=args['nome'])
        db.session.add(departamento)
        db.session.commit()
        return DepartamentoSchema().dump(departamento), 201
    
    def put(self, departamento_id):
        parser = reqparse.RequestParser()
        parser.add_argument('nome', type=str, required=True)
        args= parser.parse_args()
        departamento = Departamento.query.get(departamento_id)
        departamento.nome = args['nome']
        db.session.commit()
        return DepartamentoSchema().dump(departamento), 200
    
    def delete(self, departamento_id):
        departamento = Departamento.query.get(departamento_id)
        db.session.delete(departamento)
        db.session.commit()
        return jsonify({"msg":"Departamento excluido !"})
        
class UsuarioResource(Resource):
    def get(self, usuario_id=None):
        if usuario_id is None:
            usuarios = Usuario.query.all() 
            return UsuarioSchema(many=True).dump(usuarios), 200
    
        usuario = Usuario.query.get(usuario_id)
        return UsuarioSchema().dump (usuario), 200
    
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('nome', type=str, required=True)
        parser.add_argument('cargo', type=str, required=True)
        parser.add_argument('email', type=str, required=True)
        parser.add_argument('senha', type=str, required=True)
        parser.add_argument('departamento_id', type=int, required=True)
        args= parser.parse_args()
        if not Departamento.query.get( parser.parse_args()['departamento_id']):
            return {"message": "Departamento não encontrado"}, 404
        usuario = Usuario (nome=args['nome'], cargo=args['cargo'], email=args['email'], senha=args['senha'], departamento_id=args['departamento_id'])
        db.session.add(usuario)
        db.session.commit()
        return UsuarioSchema().dump(usuario), 201
    
    def put(self, usuario_id):
        parser = reqparse.RequestParser()
        parser.add_argument('nome', type=str, required=True)
        parser.add_argument('cargo', type=str, required=True)
        parser.add_argument('email', type=str, required=True)
        parser.add_argument('senha', type=str, required=True)
        parser.add_argument('departamento_id', type=int, required=True)
        args= parser.parse_args()
        if not Departamento.query.get( parser.parse_args()['departamento_id']):
            return {"message": "Departamento não encontrado"}, 404
        usuario = Usuario.query.get(usuario_id)
        usuario.nome = args['nome']
        usuario.cargo = args['cargo']
        usuario.email = args['email']
        usuario.senha = args['senha']
        usuario.departamento_id = args['departamento_id']
        db.session.commit()
        return UsuarioSchema().dump(usuario), 200
    
    def delete(self, usuario_id):
        usuario = Usuario.query.get(usuario_id)
        db.session.delete(usuario)
        db.session.commit()
        return jsonify({"msg":"Usuario excluido !"})
    
class AcaoResource(Resource):
    def get(self, acao_id=None):
        if acao_id is None:
            acoes = Acao.query.all() 
            return AcaoSchema(many=True).dump(acoes), 200
    
        acao = Acao.query.get(acao_id)
        return AcaoSchema().dump (acao), 200
    
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('data', type=str, required=True)
        parser.add_argument('usuario_responsavel', type=int, required=True)
        parser.add_argument('comentario', type=str, required=True)
        parser.add_argument('documento_id', type=int, required=True)
        args= parser.parse_args()
        if not Usuario.query.get( args['usuario_responsavel']):
            return {"message": "Usuario não encontrado"}, 404
        elif not Documento.query.get( args['documento_id']):
            return {"message": "Documento não encontrado"}, 404
        acao = Acao (data=args['data'], usuario_responsavel=args['usuario_responsavel'], comentario=args['comentario'], documento_id=args['documento_id'])
        db.session.add(acao)
        db.session.commit()
        return AcaoSchema().dump(acao), 201
    
    def delete(self, acao_id):
        acao = Acao.query.get(acao_id)
        db.session.delete(acao)
        db.session.commit()
        return jsonify({"msg":"Açao excluida !"})

class DocumentoResource(Resource):
    def get(self, documento_id=None):
        if documento_id is None:
            documentos = Documento.query.all() 
            return DocumentoSchema(many=True).dump(documentos), 200
    
        documento = Documento.query.get(documento_id)
        return DocumentoSchema().dump (documento), 200
    
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('num_protocolo', type=int, required=True)
        parser.add_argument('assunto', type=str, required=True)
        parser.add_argument('data_emissao', type=str, required=True)
        parser.add_argument('remetente', type=int, required=True)
        parser.add_argument('destinatario', type=int, required=True)
        parser.add_argument('status_atual', type=int, required=True)
        parser.add_argument('data_recebido', type=str, required=True)
        parser.add_argument('comentarios', type=str, required=True)
        args= parser.parse_args()        
        if not Usuario.query.get( args['destinatario']):
            return {"message": "Destinatario nao encontrado"}, 404
        elif not Usuario.query.get( args['remetente']):
            return {"message": "Remetente não encontrado"}, 404
        elif not Status.query.get( args['status_atual']):
            return {"message": "Status não encontrado"}, 404     
        documento = Documento (num_protocolo=args['num_protocolo'], assunto=args['assunto'], data_emissao=args['data_emissao'], remetente=args['remetente'], destinatario=args['destinatario'], status_atual=args['status_atual'], data_recebido=args['data_recebido'], comentarios=args['comentarios'])
        db.session.add(documento)
        db.session.commit()
        return DocumentoSchema().dump(documento), 201
    
    def put(self, documento_id):
        parser = reqparse.RequestParser()
        parser.add_argument('status_atual', type=int, required=True)
        parser.add_argument('data_recebido', type=str, required=True)
        parser.add_argument('comentarios', type=str, required=True)
        args= parser.parse_args()
        documento = Documento.query.get(documento_id)
        documento.status_atual = args['status_atual']
        documento.data_recebido = args['data_recebido']
        documento.comentarios = args['comentarios']
        db.session.commit()
        return DocumentoSchema().dump(documento), 200
        
    def delete(self, documento_id):
        documento = Documento.query.get(documento_id)
        db.session.delete(documento)
        db.session.commit()
        return jsonify({"msg":"Documento excluido !"})
