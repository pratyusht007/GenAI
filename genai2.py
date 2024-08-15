import streamlit as st
from dotenv import load_dotenv
import os
import google.generativeai as genai

# Load environment variables (assuming API key is stored there)
load_dotenv()

# Configure the GenerativeAI service with the API key
genai.configure(api_key ='your api key')


# Create a GenerativeAI model object (assuming "gemini-pro" is the correct model)
model = genai.GenerativeModel("gemini-pro")

# Start a chat session with the model
chat = model.start_chat(history=[])


def get_gemini_response(question):
    """Sends the question to the chat session and returns the response."""
    response = chat.send_message(question, stream=True)
    return response


# Initialize Streamlit app settings
st.set_page_config(page_title="PRATYUSH.AI")
st.header("PRATYUSH.AI")


# Initialize session state for chat history if it doesn't exist
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []


# User input and submit button
user_input = st.text_input("Input:", key="input")
submit = st.button("Ask the question")


# Process user input and display response
if submit and input:
    response = get_gemini_response(user_input)

    # Add user query and response to chat history
    st.session_state['chat_history'].append(("You", user_input))

    st.subheader("The Response is")
    for chunk in response:
        st.write(chunk.text)
        st.session_state['chat_history'].append(("Bot", chunk.text))


# Display chat history
st.subheader("The Chat history is")
for role, text in st.session_state['chat_history']:
    st.write(f"{role}: {text}")

