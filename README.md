# AI Language Learning UI for Japanese  

This project is a **Streamlit-based UI** designed to help users **learn Japanese** through interactive conversations in various real-world scenarios. The app allows users to review past conversations, generate new ones with an LLM, explore vocabulary and grammar, and listen to native pronunciation.  

## Features  

### 1. Scenario-Based Conversations  
- Users can **select a scenario** (e.g., restaurant, airport, shopping, etc.) to practice relevant conversations.  
- The UI generates a **5-turn dialogue** in Japanese based on the selected scenario.  

### 2. Conversation Review & Generation  
- Users can **upload previous conversations** to review.  
- Alternatively, an **LLM generates new dialogues** dynamically.  

### 3. Multi-Language Display  
- Conversations are displayed in:  
  - **Kanji (漢字)**  
  - **Romaji (Romanized Japanese)**  
  - **English translation**  

### 4. Vocabulary Learning  
- Extracts **important words** from the conversation.  
- Provides **example sentences** for each word to reinforce learning.  

### 5. Grammar Breakdown  
- Identifies key **grammar structures** from the conversation.  
- Offers **detailed explanations** with extra example sentences.  

### 6. Save & Load Conversations  
- Users can **save conversations, vocabulary, and grammar explanations** in a local folder.  
- Supports **reloading saved files** for review.  

### 7. Native-Like Pronunciation  
- The app includes **text-to-speech (TTS)** functionality to pronounce Japanese sentences like a native speaker.  

## Installation  

1. **Clone the repository**  
   ```sh
   git clone https://github.com/purplebear-cai/AILanguage.git
   cd AILanguage
   ```

2. **Install dependencies**
    ```sh
    pip install -r requirements.txt
    ```

3. **Environment Setup**

    Set up environment: To run the repository, you need to set up your OpenAI API key, and save it in the .env file.
    ```sh
    OPENAI_API_KEY={Your_OpenAI_API_key}
    ```

    Set up your PYTHONPATH:
    ```sh
    export PYTHONPATH=PATH_TO_AILanguage_FOLDER
    ```

4. **Run the Streamlit app**
    ```sh
    streamlit run src/app.py
    ```

## Contributing

Feel free to open issues or submit PRs to enhance the app!

🚀 Start your Japanese learning journey today! 🎌