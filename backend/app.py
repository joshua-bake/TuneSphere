from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Example route
@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "Welcome to TuneSphere!"})

# Example API endpoint to get songs
@app.route('/api/songs', methods=['GET'])
def get_songs():
    # This is where you would fetch songs from a database or an external API
    songs = [
        {"id": 1, "title": "Song One", "artist": "Artist A"},
        {"id": 2, "title": "Song Two", "artist": "Artist B"},
    ]
    return jsonify(songs)

# Example API endpoint to add a song
@app.route('/api/songs', methods=['POST'])
def add_song():
    new_song = request.json  # Get the JSON data from the request
    
    # Validate input
    if not new_song or 'title' not in new_song or 'artist' not in new_song:
        return jsonify({"error": "Invalid input. Please provide title and artist."}), 400

    # Here you would typically add the new song to a database
    return jsonify(new_song), 201

# Run the app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)