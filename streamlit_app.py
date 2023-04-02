import openai
import streamlit as st
import os

# Set OpenAI API key
if 'api_key' in globals():
    api_key = os.getenv("OPENAI_API_KEY")
    openai.api_key = api_key
else:
    try:
        api_key = st.text_input("Add your OpenAI API Key")
        openai.api_key = api_key
    except Exception as e:
        st.warning("No OpenAI API Key has been found")

    # If no response with text is found, return the first response's content (which may be empty)
    return response.choices[0].message.content
  
# Define the function to generate responses
def generate_response(message_log):
    # Use OpenAI's Completion API to get the chatbot's response
    completions = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # The name of the OpenAI chatbot model to use
        prompt=message_log[-1]["content"],  # The last message in the conversation history as the prompt
        #max_tokens=1024,  # The maximum number of tokens (words or subwords) in the generated response
        #n=1,  # The number of responses to generate
        #stop=None,  # The stopping sequence for the generated response, if any (not used here)
        temperature=0.7,  # The "creativity" of the generated response (higher temperature = more creative)
    )
    
    # Find the first response from the chatbot that has text in it (some responses may not have text)
    for choice in completions.choices:
        if "text" in choice:
            return choice.text

    # Get the first response from the chatbot that has text in it (some responses may not have text)
    # Or, if no response with text is found, return the first response's content (which may be empty)
    message = completions.choices[0].text.strip()
    #message = completions.choices[0].message.content

    # Add the chatbot's response to the conversation history
    message_log.append({"role": "assistant", "content": message})
    return message

# Set up the Streamlit app
st.title("Chat with an AI")
if 'message_log' not in st.session_state:
    st.session_state['message_log'] = []

# Get the user input and generate responses
user_input = st.text_input("You:")
if user_input:
    st.session_state['message_log'].append({"role": "user", "content": user_input})
    ai_response = generate_response(st.session_state['message_log'])

# Display the conversation history
if st.session_state['message_log']:
    st.write("---")
    for message in st.session_state['message_log']:
        if message["role"] == "user":
            st.write("You: " + message["content"])
        else:
            st.write("AI: " + message["content"])
    st.write("---")
