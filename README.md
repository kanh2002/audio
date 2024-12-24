# Audio Processing Tools

This repository provides two tools for audio processing:
1. **Audio Diarization** - Identify and differentiate speakers in an audio file.
2. **Audio Conversion** - Convert MP4 audio files to WAV format.

---

## 1. Audio Diarization

### Overview
The Audio Diarization tool uses the `pyannote.audio` library to perform speaker diarization. It identifies when speakers are speaking and labels them uniquely.

### Features
- Pre-trained model for speaker diarization.
- GPU support for faster processing.
- Outputs speaker start and stop times with unique speaker labels.

### Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd speaker_diarization
   ```
2. Install dependencies:
   ```bash
   pip install torch pyannote.audio
   ```

### Usage
1. Update your Hugging Face authentication token in the script.
2. Run the script:
   ```bash
   python test_audio.py
   ```

### Example Output
```
Time taken for speaker diarization: 12.34 seconds
start=0.0s stop=5.2s speaker_1
start=5.3s stop=10.7s speaker_2
...
Number of unique speakers: 2
```

---

## 2. Audio Conversion

### Overview
The Audio Conversion tool converts MP4 audio files to WAV format using FFmpeg. The WAV file is output in mono format with a sampling rate of 16kHz.

### Features
- Converts MP4 to WAV.
- Ensures mono audio with 16kHz sampling rate, compatible with most audio processing tools.

### Prerequisites
- FFmpeg must be installed on your system:
  - **Linux**: `sudo apt install ffmpeg`
  - **macOS**: `brew install ffmpeg`
  - **Windows**: [Download FFmpeg]https://ffmpeg.org/download.html#build-windows.

### Installation
1. Install required Python packages:
   ```bash
   pip install subprocess os
   ```

### Usage
1. Place your MP4 file in the same directory or provide its full path.
2. Run the script:
   ```bash
   python convert_audio.py
   ```

### Example Output
```
Successfully converted 'input_audio.mp4' to 'output_audio.wav'
```

---

## Contributing
Feel free to fork this repository and submit pull requests to improve the tools or add new features.

## License
This project is licensed under the MIT License.
