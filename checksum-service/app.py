from flask import Flask, request, jsonify
import hashlib

app = Flask(__name__)

@app.route('/checksum', methods=["POST"])
def compute_checksum():
    """
    Compute checksum for a given string using the specified algorithm (SHA256 or SHA512).
    """
    try:
        data = request.get_json()
        input_string = data.get("input_string")
        algorithm = data.get("algorithm", "sha256")

        if not input_string:
            return jsonify({"error": "Input string is required"}), 400

        if algorithm == "sha256":
            checksum = hashlib.sha256(input_string.encode()).hexdigest()
        elif algorithm == "sha512":
            checksum = hashlib.sha512(input_string.encode()).hexdigest()
        else:
            return jsonify({"error": "Unsupported algorithm"}), 400

        return jsonify({"checksum": checksum, "algorithm": algorithm}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5002)
