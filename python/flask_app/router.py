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

@bp.route('boards/index', methods=['GET'])
def index_board():
    data = boards.find_all()
    return data

@bp.route('boards/home', methods=['GET'])
def index_person():
    data = boards.find_one(id)
    return data

@bp.route('boards/add', methods=['POST'])
def add_board():
    boards.create(request.json, id)
    return 'send!'