import firebase_admin
from firebase_admin import credentials, db

# Fetch the service account key JSON file contents
cred = credentials.Certificate("./serviceAccountKey.json")

# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://crimsondb-27483-default-rtdb.firebaseio.com/'
})

def get_db_reference(reference_path):
    return db.reference(reference_path)
