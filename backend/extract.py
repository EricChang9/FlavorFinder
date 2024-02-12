import os
import firebase_admin
import input
import generateFoodText
import LLM2
from firebase_admin import credentials, storage
from flask import Flask, app, request, jsonify

# Initialize Firebase Admin SDK
cred = credentials.Certificate("/Users/aaronchanner/Documents/FlavorFinder/serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'storageBucket': 'meal-planning-cc508.appspot.com',
    'databaseURL': 'https://meal-planning-cc508-default-rtdb.firebaseio.com'
})

# Initialize Firebase Storage
bucket = storage.bucket()


def extract_from_database(destination_folder, default_name="image"):
    """
    Function to save the most recent image added to Firebase Storage to a local file.
    """
    # List all objects in the bucket
    blobs = bucket.list_blobs()

    # Sort blobs by their updated timestamps
    sorted_blobs = sorted(blobs, key=lambda x: x.updated, reverse=True)

    # Get the most recent blob (image)
    most_recent_blob = sorted_blobs[0]

    # Extract file extension
    # Assuming the file type is always PNG, you can change it accordingly
    file_extension = ".png"

    # Construct destination file path
    destination_file = os.path.join(
        destination_folder, default_name + file_extension)

    # Download the most recent image to the destination path
    most_recent_blob.download_to_filename(destination_file)

    print("Most recent image saved successfully:", destination_file)


    # Delete the image from Firebase Storage
    most_recent_blob.delete()

    print("Most recent image deleted from Firebase Storage")


if __name__ == "__main__":
    destination_folder = "./images/"  # Specify the destination folder
    extract_from_database(destination_folder)
    image_path = destination_folder + "image.png"  # Specify the image path
    api_key="AIzaSyDRB1lQaSNq84ZI2Gvaw_GeGinSWgFvigE"
    result = generateFoodText.generate_food_text_from_image(image_path, api_key)
    llmresult = LLM2.generate_recipe_from_ingredients(result)
    input.upload_text_to_firebase(llmresult, "/recipe")