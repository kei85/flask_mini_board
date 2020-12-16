from flask import Blueprint, request, jsonify
from models import users, boards


bp = Blueprint('router', __name__, url_prefix='/')

@bp.route('/')
def Hello():
    return "Hello, World"

@bp.route('/api/users/add', methods=['POST'])
def add_user():
    users.create(request.json)
    return request.json

@bp.route('/api/users/edit/<int:id>', methods=['GET'])
def edit_user(id):
    usr = users.find_user(id)
    usr_schema = users.UserSchema()
    return jsonify({"user": usr_schema.dump(usr)})

@bp.route('/api/users/edit/<int:id>', methods=['POST'])
def store_user(id):
    users.update(request.json, id)
    return 'update!'

@bp.route('/api/boards/index', methods=['GET'])
def index_board():
    brds = boards.find_all()
    brds_schema = boards.BoardSchema(many=True)
    usrs = users.find_AllUser()

    brds_dict = brds_schema.dump(brds)

    for bd in brds_dict:
        for u in usrs:
            if bd['uid'] == u.id:
                bd['name'] = u.name
            
    return jsonify({"boards": brds_dict})

@bp.route('/api/boards/myindex/<int:uid>', methods=['GET'])
def index_person(uid):
    brds = boards.find_one(uid)
    brds_schema = boards.BoardSchema(many=True)
    return jsonify({"boards": brds_schema.dump(brds)})

@bp.route('/api/boards/add/<int:uid>', methods=['POST'])
def add_board(uid):
    boards.create(request.json, uid)
    return 'send!'

@bp.route('/api/users/login', methods=['POST'])
def login():
    data = request.json
    usr = users.find_mail(data['mail'])
    usr_schema = users.UserSchema()
    if usr.pwd == data['pwd']:
        return jsonify({"user": usr_schema.dump(usr), "state": True})
    return {"state": False}