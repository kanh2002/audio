# server.py

import logging
from flask import Flask, request, jsonify
from speaker_diarization import AudioDiarization
import os

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.DEBUG)

# Replace 'YOUR_AUTH_TOKEN' with your Hugging Face token
auth_token = "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"
diarizer = AudioDiarization(auth_token)

@app.route('/')
def index():
    return "Welcome to the Speaker Diarization API"

@app.route('/diarize', methods=['POST'])
def diarize():
    if 'file' not in request.files:
        app.logger.debug("No file part in the request")
        return jsonify({"error": "No file part"}), 400

    file = request.files['file']
    if file.filename == '':
        app.logger.debug("No selected file")
        return jsonify({"error": "No selected file"}), 400

    if file and file.filename.endswith('.wav'):
        file_path = os.path.join('/tmp', file.filename)
        file.save(file_path)
        app.logger.debug(f"File saved to {file_path}")

        elapsed_time, diarization = diarizer.process_audio(file_path)
        results = []
        for turn, _, speaker in diarization.itertracks(yield_label=True):
            results.append(f"start={turn.start:.1f}s stop={turn.end:.1f}s speaker_{speaker}")

        # Save results to a text file
        output_file = file_path.replace('.wav', '_output.txt')
        with open(output_file, 'w') as f:
            for result in results:
                f.write(result + '\n')

        app.logger.debug("Diarization process completed")
        return jsonify({"elapsed_time": elapsed_time, "results": results, "output_file": output_file})

    app.logger.debug("Invalid file format, only WAV files are accepted")
    return jsonify({"error": "Invalid file format, only WAV files are accepted"}), 400

if __name__ == '__main__':
    app.run(host = "localhost" ,debug=False)