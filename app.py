# app.py

from flask import Flask, request, jsonify
from flask_bcrypt import Bcrypt
import base64
import json

app = Flask(__name__)
bcrypt = Bcrypt(app)

# Hardcoded user data for authentication
users = {
    'appuser': bcrypt.generate_password_hash('appuser').decode('utf-8')
}

# Load data from a JSON file
with open('auapp-version-badge.json', 'r') as file:
    data = json.load(file)

def extract_credentials(authorization_header):
    try:
        auth_type, encoded_credentials = authorization_header.split()
        credentials = base64.b64decode(encoded_credentials).decode('utf-8')
        username, password = credentials.split(':')
        return username, password
    except (ValueError, TypeError):
        return None, None

@app.route('/update_auapp_version', methods=['POST'])
def update_auapp_version():
    try:
        # Get credentials from the Authorization header
        auth_header = request.headers.get('Authorization')
        username, password = extract_credentials(auth_header)

        # Check if the credentials are valid
        if username == 'appuser' and bcrypt.check_password_hash(users['appuser'], password):
            # Assuming the JSON structure has a key named 'message'
            data['message'] = request.json['new_version']

            # Save the updated data back to the file
            with open('auapp-version-badge.json', 'w') as file:
                json.dump(data, file, indent=4)

            return jsonify({'success': True, 'message': 'Property updated successfully'}), 200
        else:
            return jsonify({'success': False, 'message': 'Invalid credentials'}), 401

    except KeyError:
        return jsonify({'success': False, 'message': 'Invalid request format'})

if __name__ == '__main__':
    app.run(debug=True)
