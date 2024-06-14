from flask import Blueprint, request
from app.database import get_db_reference

main_bp = Blueprint('main', __name__)

@main_bp.route('/add_score', methods=['POST'])
def add_score():
    data = request.get_json()
    username = data['username']
    score = data['score']

    user_ref = get_db_reference(f'users/{username}')
    user = user_ref.get()
    if not user:
        user_data = {'username': username, 'score': score}
        user_ref.set(user_data)
    else:
        user_ref.update({'score': score})

    return 'success', 201

@main_bp.route('/get_score', methods=['GET'])
def get_score():
    username = request.args.get('username')
    user_ref = get_db_reference(f'users/{username}')
    user = user_ref.get()

    if not user:
        return 'No data found', 404

    return str(user['score']), 200

@main_bp.route('/update_score', methods=['PUT'])
def update_score():
    data = request.get_json()
    username = data['username']
    new_score = data['new_score']

    user_ref = get_db_reference(f'users/{username}')
    user = user_ref.get()
    if not user:
        return 'User not found', 404

    user_ref.update({'score': new_score})
    return 'success', 200

@main_bp.route('/delete_score', methods=['DELETE'])
def delete_score():
    data = request.get_json()
    username = data['username']

    user_ref = get_db_reference(f'users/{username}')
    user = user_ref.get()
    if not user:
        return 'User not found', 404

    user_ref.delete()
    return 'success', 200

@main_bp.route('/top_scores', methods=['GET'])
def top_scores():
    users_ref = get_db_reference('users')
    users = users_ref.get()

    all_scores = [{'username': username, 'score': user_data['score']} for username, user_data in users.items()]

    all_scores.sort(key=lambda x: x['score'])
    top_scores = all_scores[:10]
    return str(top_scores), 200
