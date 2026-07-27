from pydoc import text

from voice.kokoro_engine import generate_voice as generate_english_voice

def speak(text, language="en"):

   """
    Makes BMO speak using the Kokoro voice engine.
    """

generate_english_voice(text)