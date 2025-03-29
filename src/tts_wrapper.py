import io
import json
import uuid
import base64
import openai
import streamlit as st

# Load audio cache
CACHE_FILE = "data/audio/audio_cache.json"

# Load cache from file
try:
     with open(CACHE_FILE, "r") as f:
        audio_cache = json.load(f)
        # Decode base64 strings when loading
        for key, value in audio_cache.items():
            audio_cache[key] = base64.b64decode(value)
except FileNotFoundError:
    audio_cache = {}


def generate_audio(text: str):
    """Generates audio using OpenAI TTS API."""
    if text in audio_cache:
        return audio_cache[text]  # Return cached audio

    try:
        response = openai.audio.speech.create(
            model="gpt-4o-mini-tts",  # ["tts-1", "tts-1-hd", "gpt-4o-mini-tts"]
            voice="shimmer",  # Recommended Japanese-compatible voice, other example: nova
            input=text,
            instructions="native speaker, calm, patient, like an instructor",
        )

        audio_data = response.content
        audio_cache[text] = audio_data  # Cache the audio data
        save_cache()  # Save the cache to file
        return audio_data
    except Exception as e:
        st.error(f"Error generating audio: {e}")
        return None

def save_cache():
    """Saves the audio cache to a local file."""
    try:
        # Encode base64 strings before saving
        encoded_cache = {key: base64.b64encode(value).decode('utf-8') for key, value in audio_cache.items()}
        with open(CACHE_FILE, "w") as f:
            json.dump(encoded_cache, f)
    except Exception as e:
        st.error(f"Error saving cache: {e}")


def speak_japanese(text, speed=1.0, conversation_id="", index=None):
    """Plays the Japanese text using OpenAI TTS API."""
    audio_data = generate_audio(text)
    
    if audio_data:
        if conversation_id not in st.session_state:
            st.session_state[conversation_id] = {}
        unique_key = f"{conversation_id}_{index}"  # Create a unique key
        st.session_state[conversation_id][unique_key] = audio_data  # Store audio data in session state
        st.session_state.audio_cache[unique_key] = audio_data

        # audio_url = f"data:audio/wav;base64,{base64.b64encode(st.session_state[conversation_id][unique_key]).decode()}"
        # audio_id = f"{conversation_id}_{str(uuid.uuid4())}"
        audio_url = f"data:audio/wav;base64,{base64.b64encode(audio_data).decode()}"
        audio_id = f"{conversation_id}_{str(uuid.uuid4())}"  # Unique ID for HTML element

        st.markdown(
            f"""
            <audio id="{audio_id}" controls speed="{speed}" style="width: 100px;">
                <source src="{audio_url}" type="audio/wav">
                Your browser does not support the audio element.
            </audio>
            """,
            unsafe_allow_html=True,
        )

