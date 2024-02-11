import firebase_admin
from firebase_admin import credentials, db

# Initialize Firebase Admin SDK
cred = credentials.Certificate("../serviceAccountKey.json")


def upload_text_to_firebase(text_data, database_path):
    """
    Function to upload text data to Firebase Realtime Database.
    """
    # Get a reference to the specified database path
    ref = db.reference(database_path)

    # Upload the text data to Firebase Realtime Database
    ref.set(text_data)

    print("Text data uploaded successfully to Firebase Database:", database_path)


