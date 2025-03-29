import os
import uuid
import random
import streamlit as st
from tts_wrapper import speak_japanese
from vocab_wrapper import add_to_dictionary
from src.conv_wrapper import generate_conversation_data, load_conversation_from_file, save_conversation_to_file

vocabulary_path = "data/vocabulary/vocabulary.xlsx"
conversation_folder = "data/conversation"

# ==================== Add button to refresh ====================
def refresh_page():
    st.switch_page("app.py")  # Change to your script's filename

if st.button("Refresh"):
    refresh_page()

# ==================== Streamlit App ====================
st.title("Japanese Learning Companion")

# ==================== Generate a unique ID for the conversation ====================
conversation_id = str(uuid.uuid4())
st.session_state.conversation_id = conversation_id
st.session_state.conversation_data = None
if "audio_cache" not in st.session_state:
    st.session_state.audio_cache = {}  # Initialize session state cache

# ==================== Sidebar ====================
scenario = st.sidebar.selectbox("Scenario", ["Restaurant", "Airport", "Shopping", "Children", "Home Daily Life"])
conversation_source = st.sidebar.radio("Conversation Source", ["Upload Conversation", "Generate Conversation"])

if conversation_source == "Upload Conversation":
    uploaded_file = st.sidebar.file_uploader("Upload Conversation File (.json)", type=["json"])
    if uploaded_file is not None:
        st.session_state.conversation_data = load_conversation_from_file(uploaded_file)
        st.sidebar.success("Conversation loaded successfully!")
else:
    if "conversation_data" not in st.session_state:
        st.session_state.conversation_data = generate_conversation_data(scenario)

if st.sidebar.button("Generate"):
    st.session_state.conversation_data = generate_conversation_data(scenario)
    st.sidebar.success("Conversation generated successfully!")

if st.sidebar.button("Save Conversation"):
    if st.session_state.conversation_data:
        filedir = f"{conversation_folder}/{scenario}"
        if not os.path.exists(filedir):
            os.makedirs(filedir)
        filename = random.getrandbits(128)
        filepath = f"{filedir}/{filename}.json"
        save_conversation_to_file(st.session_state.conversation_data, filepath)


# ==================== Main Area ====================
if st.session_state.conversation_data:
    # Display Conversation
    st.header("Conversation")
    for i, turn in enumerate(st.session_state.conversation_data["conversation"]):
        col1, col2 = st.columns([0.8, 0.2])  # Create two columns
        with col1:
            st.markdown(f"**Japanese:** {turn['kanji']}")
            st.markdown(f"**Romaji:** {turn['romaji']}")
            st.markdown(f"**English:** {turn['english']}")
        with col2:
            speed = st.selectbox("Speed", ["1.0", "0.7", "1.5"],  key=f"speed_{conversation_id}_{i}")
            speak_japanese(turn['romaji'], float(speed), conversation_id, i)
        st.markdown("---")

    # Display Vocabulary
    with st.expander("Vocabulary"):
        st.header("Vocabulary")
        for j, word in enumerate(st.session_state.conversation_data["vocabulary"]):
            col1, col2 = st.columns([0.8, 0.2])
            with col1:
                st.subheader(f"{word['kanji']} ({word['romaji']}) - {word['english']}")
                for k, example in enumerate(word["examples"]):
                    st.markdown(f"- {example}")
            with col2:
                speak_japanese(word['romaji'], float(1.0), conversation_id, j)
                if st.button(f"Add to Dictionary", key=f"add_to_dict_{j}"):
                    if not os.path.exists(vocabulary_path):
                        directory_path = os.path.dirname(vocabulary_path)
                        os.makedirs(directory_path, exist_ok=True)
                    add_to_dictionary(word['english'], word['romaji'], word['kanji'], word['examples'], vocabulary_path)
            st.markdown("---")
        

    # Display Grammar Points
    with st.expander("Grammar Points"):
        st.header("Grammar Points")
        for grammar in st.session_state.conversation_data["grammar"]:
            st.subheader(grammar["grammar"])
            for example in grammar["examples"]:
                st.markdown(f"- {example}")
            st.markdown("---")

else:
    st.write("Select a scenario and generate or upload a conversation.")