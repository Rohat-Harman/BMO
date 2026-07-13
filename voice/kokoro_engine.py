import sounddevice as sd
from kokoro_onnx import Kokoro

MODEL_PATH = "models/tts/kokoro-v1.0.onnx"
VOICES_PATH = "models/tts/voices-v1.0.bin"

kokoro = Kokoro(MODEL_PATH, VOICES_PATH)


def generate_voice(text):
    samples, sample_rate = kokoro.create(
        text,
        voice="af_sarah",
        speed=1.0,
        lang="en-us"
    )

    sd.play(samples, sample_rate)
    sd.wait()