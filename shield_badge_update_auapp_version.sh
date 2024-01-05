#!/bin/bash

# Set the API endpoint URL
API_URL="http://127.0.0.1:5000/update_auapp_version"

# Set the username and password
USERNAME="appuser"
PASSWORD="appuser"

# Set the new version
NEW_VERSION="$1"  # Pass the new version as a command-line argument

# Use curl to send a POST request with Basic Authentication
curl -X POST \
     -H "Content-Type: application/json" \
     -H "Authorization: Basic $(echo -n $USERNAME:$PASSWORD | base64)" \
     -d "{\"new_version\": \"$NEW_VERSION\"}" \
     $API_URL