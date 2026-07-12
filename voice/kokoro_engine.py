import soundfile as sf
from kokoro_onnx import Kokoro

MODEL_PATH = "models/tts/kokoro-v1.0.onnx"
VOICES_PATH = "models/tts/voices-v1.0.bin"


def generate_voice(text):
    kokoro = Kokoro(MODEL_PATH, VOICES_PATH)

    samples, sample_rate = kokoro.create(
        text,
        voice="af_sarah",
        speed=1.0,
        lang="en-us"
    )

    sf.write("bmo_test.wav", samples, sample_rate)
    print("Created bmo_test.wav")