from flask import Flask, request, jsonify
import hashlib
import requests

app = Flask(__name__)

@app.route('/compute-checksum', methods=["POST"])
def compute_checksum():
    """
    Route to compute checksum (SHA256 or SHA512).
    - Accepts a string and computes its checksum using the selected algorithm.
    - Saves the checksum to the database service.
    """
    try:
        data = request.get_json()
        string = data.get('string')
        algorithm = data.get('algorithm', 'sha256')

        if not string:
            return jsonify({"error": "Please send a valid string to compute checksum"}), 400

        # Compute checksum using the checksum service
        response = requests.post(
            "http://checksum-service:5002/checksum",
            json={"input_string": string, "algorithm": algorithm}
        )

        if response.status_code != 200:
            return jsonify({"error": "Failed to compute checksum"}), response.status_code

        checksum_data = response.json()

        # Save the computed checksum to database-service
        save_response = requests.post(
            "http://database-service:5000/save-checksum",
            json={"string": string, "checksum": checksum_data['checksum']}
        )

        if save_response.status_code == 201:
            return jsonify(checksum_data), 200
        else:
            return jsonify({"error": "Unable to save checksum"}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/list-checksums', methods=["GET"])
def list_checksums():
    """
    Route to get all checksums from the database service.
    """
    try:
        response = requests.get("http://database-service:5000/get-checksums")
        if response.status_code == 200:
            return jsonify(response.json()), 200
        else:
            return jsonify({"error": "Unable to retrieve checksums"}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
