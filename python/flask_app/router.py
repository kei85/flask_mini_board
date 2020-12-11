from flask import Blueprint, request, jsonify
from models import users, boards


bp = Blueprint('router', __name__, url_prefix='/')

@bp.route('/')
def Hello():
    return "Hello, World"

@bp.route('users/add', methods=['POST'])
def add_user():
    users.create(request.json)
    return 'regist!'

@bp.route('users/edit/<int:id>', methods=['GET'])
def edit_user(id):
    usr = users.find_user(id)
    usr_schema = users.UserSchema()
    return jsonify({"user": usr_schema.dump(usr)})

@bp.route('users/edit/<int:id>', methods=['POST'])
def store_user(id):
    users.update(request.json, id)
    return 'update!'

@bp.route('boards/index/<int:uid>', methods=['GET'])
def index_board():
    brds = boards.find_all()
    brds_schema = boards.BoardSchema(many=True)
    return jsonify({"boards": brds_schema.dump(brds)})

@bp.route('boards/home/<int:uid>', methods=['GET'])
def index_person(uid):
    brds = boards.find_one(uid)
    brds_schema = boards.BoardSchema(many=True)
    return jsonify({"boards": brds_schema.dump(brds)})

@bp.route('boards/add/<int:uid>', methods=['POST'])
def add_board(uid):
    boards.create(request.json, uid)
    return 'send!'