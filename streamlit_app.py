import openai
import streamlit as st
import os

# Set the Model of use
LAST_GPT = True

# Set OpenAI API key
if 'api_key' not in st.session_state:
    api_key = os.getenv("OPENAI_API_KEY")
    if api_key:
        openai.api_key = api_key
else:
    api_key = st.text_input("Add your OpenAI API Key", type="password")
    if api_key:
        openai.api_key = api_key
    else:
        st.warning("No OpenAI API Key has been found")

# Define the function to generate responses
def generate_response(message_log, prompt):
    if not message_log:
        # Return a default message if the conversation history is empty
        return "Hi, how can I help you today?"

    try:
        messages = message_log if message_log else [{"role": "user", "content": prompt}]
        
        if LAST_GPT:
            # Using GPT-4 or GPT-3.5-turbo models
            response = openai.ChatCompletion.create(
                model="gpt-4" if LAST_GPT else "gpt-3.5-turbo",
                messages=messages,
                max_tokens=100,
                temperature=0.3,  # The "creativity" of the generated response
                presence_penalty=2
            )
            message = response['choices'][0]['message']['content']
        else:
            # Using older models such as text-davinci-003
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=prompt,
                max_tokens=100,
                temperature=0.3,
                presence_penalty=2
            )
            message = response.choices[0].text.strip()

        # Add the chatbot's response to the conversation history
        message_log.append({"role": "assistant", "content": message})
        return message

    except Exception as e:
        st.warning(f"An error occurred while processing your request: {e}")
        return None

# Set up the Streamlit app
st.title("Chat with an AI")
if 'message_log' not in st.session_state:
    st.session_state['message_log'] = []

# Get the user input and generate responses
user_input = st.text_input("You:")
if user_input:
    st.session_state['message_log'].append({"role": "user", "content": user_input})
    ai_response = generate_response(st.session_state['message_log'], user_input)
    st.session_state['message_log'].append({"role": "assistant", "content": ai_response})

# Display the conversation history
if st.session_state['message_log']:
    st.write("---")
    for message in st.session_state['message_log']:
        if message["role"] == "user":
            st.write("You: " + message["content"])
        else:
            st.write("AI: " + message["content"])
    st.write("---")