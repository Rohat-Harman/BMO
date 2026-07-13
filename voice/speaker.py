from voice.kokoro_engine import generate_voice as generate_english_voice

def speak(text, language="en"):

    """
    Makes BMO speak.

    For now, it prints text.
    Later, this function will generate BMO's voice.

    """
    generate_english_voice(text)