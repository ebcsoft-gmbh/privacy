# app.py

from flask import Flask, request, jsonify
import json

app = Flask(__name__)

# Load data from a JSON file
with open('auapp-version-badge.json', 'r') as file:
    data = json.load(file)

@app.route('/update_auapp_version', methods=['POST'])
def update_auapp_version():
    try:
        # Assuming the JSON structure has a key named 'property_to_update'
        data['message'] = request.json['new_version']
        
        # Save the updated data back to the file
        with open('auapp-version-badge.json', 'w') as file:
            json.dump(data, file, indent=4)

        return jsonify({'success': True, 'message': 'Property updated successfully'})

    except KeyError:
        return jsonify({'success': False, 'message': 'Invalid request format'})

if __name__ == '__main__':
    app.run(debug=True)