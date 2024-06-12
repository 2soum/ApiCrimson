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
        user_data = {'username': username, 'password': '', 'scores': []}
        user_ref.set(user_data)
        user = user_data

    scores_ref = user_ref.child('scores')
    new_score_ref = scores_ref.push({'score': score})
    return 'success', 201

@main_bp.route('/get_best_score', methods=['GET'])
def get_best_score():
    username = request.args.get('username')
    user_ref = get_db_reference(f'users/{username}')
    user = user_ref.get()

    if not user:
        return 'No data found', 404

    scores = user.get('scores', [])
    best_score = min([score['score'] for score in scores], default=None)
    return str(best_score), 200

@main_bp.route('/update_score', methods=['PUT'])
def update_score():
    data = request.get_json()
    username = data['username']
    old_score = data['old_score']
    new_score = data['new_score']

    user_ref = get_db_reference(f'users/{username}')
    user = user_ref.get()
    if not user:
        return 'User not found', 404

    scores_ref = user_ref.child('scores')
    scores = scores_ref.get()
    for key, score_data in scores.items():
        if score_data['score'] == old_score:
            scores_ref.child(key).update({'score': new_score})
            return 'success', 200

    return 'Score not found', 404

@main_bp.route('/delete_score', methods=['DELETE'])
def delete_score():
    data = request.get_json()
    username = data['username']
    score_to_delete = data['score']

    user_ref = get_db_reference(f'users/{username}')
    user = user_ref.get()
    if not user:
        return 'User not found', 404

    scores_ref = user_ref.child('scores')
    scores = scores_ref.get()
    for key, score_data in scores.items():
        if score_data['score'] == score_to_delete:
            scores_ref.child(key).delete()
            return 'success', 200

    return 'Score not found', 404

@main_bp.route('/top_scores', methods=['GET'])
def top_scores():
    users_ref = get_db_reference('users')
    users = users_ref.get()

    all_scores = []
    for username, user_data in users.items():
        scores = user_data.get('scores', [])
        for score_data in scores:
            all_scores.append({'username': username, 'score': score_data['score']})

    all_scores.sort(key=lambda x: x['score'])
    top_scores = all_scores[:10]
    return str(top_scores), 200
