import json
import openai
import streamlit as st
from conv_prompt import GEN_CONVERSATION_PROMPT

# Replace with your OpenAI API key
llm_model = "gpt-4o-mini"

def replace_placeholders(prompt, variables):
    for key, value in variables.items():
        placeholder = f"[{key}]"
        prompt = prompt.replace(placeholder, str(value))
    return prompt

def generate_conversation_data(scenario):
    # get prompt
    variables = {
        "scenario": scenario,
    }
    # prompt = template.format(**variables)
    prompt = replace_placeholders(GEN_CONVERSATION_PROMPT, variables)
    print(prompt)

    # get response
    completion = openai.chat.completions.create(
        model=llm_model,
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ]
    )
    response = completion.choices[0].message.content
    try:
        data = json.loads(response)
        return data
    except json.JSONDecodeError:
        st.error(f"Error decoding JSON. Check LLM output.\n{response}")
        return None

def load_conversation_from_file(file):
    try:
        data = json.load(file)
        return data
    except Exception as e:
        st.error(f"Error loading conversation: {e}")
        return None

def save_conversation_to_file(conversation, filepath):
    try:
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(conversation, f, ensure_ascii=False, indent=4)
        st.success(f"Conversation saved to {filepath}")
    except Exception as e:
        st.error(f"Error saving conversation: {e}")

def parse_llm_output(llm_output: str):
    llm_output_dict = json.loads(llm_output)
    conversation = llm_output_dict.get("conversation", [])
    vocabulary = llm_output_dict.get("vocabulary", [])
    grammar = llm_output_dict.get("grammar", [])
