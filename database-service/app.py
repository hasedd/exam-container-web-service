from flask import Flask, request, jsonify
import sqlite3
import os

app = Flask(__name__)

# Ensure database directory exists
db_path = os.path.join(os.path.dirname(__file__), "/data/checksums.db")
os.makedirs(os.path.dirname(db_path), exist_ok=True)

# Initialize database schema
def init_db():
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS checksums (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                string TEXT NOT NULL,
                checksum TEXT NOT NULL
            )
        ''')
        conn.commit()

init_db()


@app.route('/save-checksum', methods=['POST'])
def save_checksum():
    """Store a checksum into the database."""
    try:
        data = request.get_json()
        string = data.get('string')
        checksum = data.get('checksum')

        if not string or not checksum:
            return jsonify({"error": "Invalid input"}), 400

        with sqlite3.connect(db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('INSERT INTO checksums (string, checksum) VALUES (?, ?)', (string, checksum))
            conn.commit()
        return jsonify({"message": "Checksum saved"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/get-checksums', methods=['GET'])
def get_checksums():
    """Retrieve all stored checksums."""
    try:
        with sqlite3.connect(db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM checksums')
            rows = cursor.fetchall()
            data = [{"id": row[0], "string": row[1], "checksum": row[2]} for row in rows]

        return jsonify({"data": data}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
