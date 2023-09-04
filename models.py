import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
db = SQLAlchemy()
ma = Marshmallow()



class Status(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  descricao = db.Column(db.String(100))
  documentos = db.relationship('Documento', backref='status', lazy=True)  

class Departamento(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  nome = db.Column(db.String(100))
  usuarios = db.relationship('Usuario', backref='departamento', lazy=True)

class Usuario(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  nome = db.Column(db.String(100))
  cargo = db.Column(db.String(100))
  email = db.Column(db.String(100))
  senha = db.Column(db.String(100))
  departamento_id = db.Column(db.Integer, db.ForeignKey('departamento.id'),  nullable=False)
  acoes = db.relationship('Acao', backref='usuario', lazy=True)
  

class Documento(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  num_protocolo = db.Column(db.Integer)
  assunto = db.Column(db.String(100))
  data_emissao = db.Column(db.String(100))
  remetente = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
  destinatario = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
  status_atual = db.Column(db.Integer, db.ForeignKey('status.id'), nullable=False)
  data_recebido = db.Column(db.String(100))
  comentarios = db.Column(db.String(100))
  acoes = db.relationship('Acao', backref='documento', lazy=True)  
  
  Documentos_remet = db.relationship('Usuario', foreign_keys=[remetente])
  Documentos_dest = db.relationship('Usuario', foreign_keys=[destinatario])

class Acao(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  data = db.Column(db.Date)
  usuario_responsavel = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
  comentario = db.Column(db.String(100))
  documento_id = db.Column(db.Integer, db.ForeignKey('documento.id'), nullable=False)

class StatusSchema (ma.Schema):
  class Meta:
    fields = ('id', 'descricao')
    
class DepartamentoSchema (ma.Schema):
  class Meta:
    fields = ('id', 'nome')

class UsuarioSchema (ma.Schema):
  class Meta:
    fields = ('id', 'nome', 'cargo', 'email', 'senha', 'departamento_id')

class DocumentoSchema (ma.Schema):
  class Meta:
    fields = ('id', 'num_protocolo', 'assunto', 'data_emissao', 'remetente', 'destinatario', 'status_atual', 'data_recebido', 'comentarios')

class AcaoSchema (ma.Schema):
  class Meta:
    fields = ('id', 'data', 'usuario_responsavel', 'comentario', 'documento_id')
     
  
    