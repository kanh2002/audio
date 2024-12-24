import os
import subprocess

def convert_mp4_to_wav(input_file, output_file):
    """
    Chuyển đổi file MP4 sang WAV bằng cách sử dụng FFmpeg.

    """
    if not os.path.exists(input_file):
        raise FileNotFoundError(f"Input file '{input_file}' does not exist.")

    # Xây dựng lệnh FFmpeg
    command = [
        "ffmpeg", "-i", input_file, "-ac", "1", "-ar", "16000", output_file
    ]

    try:
        # Chạy lệnh FFmpeg
        subprocess.run(command, check=True)
        print(f"Successfully converted '{input_file}' to '{output_file}'")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while converting file: {e}")

if __name__ == "__main__":
    # Đường dẫn file MP4 đầu vào và WAV đầu ra
    input_mp4 = "t4.m4a"
    output_wav = "output1_audio.wav"

    try:
        convert_mp4_to_wav(input_mp4, output_wav)
    except Exception as e:
        print(f"An error occurred: {e}")
