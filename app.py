from flask import Flask, request, jsonify, json
from flask_restful import Api
from models import db, ma
from resources import StatusResource, DepartamentoResource, UsuarioResource, AcaoResource, DocumentoResource


app = Flask (__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
api = Api(app)
db.init_app (app)
ma.init_app (app)

with app.app_context():
    db.create_all()

api.add_resource (StatusResource, '/status', '/status/<int:status_id>')
api.add_resource (DepartamentoResource, '/departamento', '/departamento/<int:departamento_id>')
api.add_resource (UsuarioResource, '/usuario', '/usuario/<int:usuario_id>')
api.add_resource (AcaoResource, '/acao', '/acao/<int:acao_id>')
api.add_resource (DocumentoResource, '/documento', '/documento/<int:documento_id>')

if __name__ == '__main__': 
    app.run(debug=True)