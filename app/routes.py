from flask import Blueprint, request, jsonify
from app.models import User, Score
from app.database import db

main_bp = Blueprint('main', __name__)


@main_bp.route('/add_score', methods=['POST'])
def add_score():
    data = request.get_json()
    username = data['username']
    score = data['score']

    user = User.query.filter_by(username=username).first()
    if not user:
        user = User(username=username, password='')  # Mot de passe vide pour l'instant
        db.session.add(user)
        db.session.commit()

    new_score = Score(user_id=user.id, score=score)
    db.session.add(new_score)
    db.session.commit()
    return jsonify({'status': 'success'})


@main_bp.route('/get_best_score', methods=['GET'])
def get_best_score():
    username = request.args.get('username')
    user = User.query.filter_by(username=username).first()

    if not user:
        return jsonify({'username': username, 'best_score': None})

    best_score = db.session.query(db.func.min(Score.score)).filter(Score.user_id == user.id).scalar()
    return jsonify({'username': username, 'best_score': best_score})


@main_bp.route('/update_score', methods=['PUT'])
def update_score():
    data = request.get_json()
    username = data['username']
    old_score = data['old_score']
    new_score = data['new_score']

    user = User.query.filter_by(username=username).first()
    if not user:
        return jsonify({'status': 'user not found'}), 404

    score = Score.query.filter_by(user_id=user.id, score=old_score).first()
    if not score:
        return jsonify({'status': 'score not found'}), 404

    score.score = new_score
    db.session.commit()
    return jsonify({'status': 'success'})


@main_bp.route('/delete_score', methods=['DELETE'])
def delete_score():
    data = request.get_json()
    username = data['username']
    score_to_delete = data['score']

    user = User.query.filter_by(username=username).first()
    if not user:
        return jsonify({'status': 'user not found'}), 404

    score = Score.query.filter_by(user_id=user.id, score=score_to_delete).first()
    if not score:
        return jsonify({'status': 'score not found'}), 404

    db.session.delete(score)
    db.session.commit()
    return jsonify({'status': 'success'})

@main_bp.route('/top_scores', methods=['GET'])
def top_scores():
    top_scores = db.session.query(User.username, Score.score).join(Score).order_by(Score.score).limit(10).all()
    result = [{'username': username, 'score': score} for username, score in top_scores]
    return jsonify(result)