from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_image():
    try:
        image_data = request.get_data()  # Get binary image data from the request
        # Process and save the image data as needed

        return jsonify({'message': 'Image uploaded successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
