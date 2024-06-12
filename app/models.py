# models.py (for reference, not used directly with Firebase)
class User:
    def __init__(self, username, password=''):
        self.username = username
        self.password = password
        self.scores = []

class Score:
    def __init__(self, user_id, score):
        self.user_id = user_id
        self.score = score
