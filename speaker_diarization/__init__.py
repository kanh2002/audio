# audio_diarization/__init__.py

import time
from pyannote.audio import Pipeline
import torch

class AudioDiarization:
    def __init__(self, auth_token, model_name="pyannote/speaker-diarization-3.1"):
        """
        Khởi tạo AudioDiarization với model đã tải sẵn.

        :param auth_token: Hugging Face authentication token.
        :param model_name: Tên của mô hình diarization trên Hugging Face.
        """
        self.auth_token = auth_token
        self.model_name = model_name

        # Load pre-trained diarization model
        self.pipeline = Pipeline.from_pretrained(model_name, use_auth_token=auth_token)

        if self.pipeline is None:
            raise ValueError("Failed to load the pipeline. Check your token and repository access.")

        # Set device to CUDA if available
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.pipeline.to(self.device)

    def process_audio(self, audio_file):
        """
        Thực hiện tách giọng trên file âm thanh.

        :param audio_file: Đường dẫn đến file âm thanh (WAV, mono, 16kHz).
        :return: Thời gian xử lý và kết quả diarization.
        """
        start_time = time.time()
        diarization = self.pipeline(audio_file)
        end_time = time.time()

        elapsed_time = end_time - start_time
        print(f"Time taken for speaker diarization: {elapsed_time:.2f} seconds")
        return elapsed_time, diarization

    def print_results(self, diarization):

        unique_speakers = set()

        for turn, _, speaker in diarization.itertracks(yield_label=True):
            print(f"start={turn.start:.1f}s stop={turn.end:.1f}s speaker_{speaker}")
            unique_speakers.add(speaker)

        print(f"Number of unique speakers: {len(unique_speakers)}")
        return unique_speakers
